"""Provide common utilities that spaz uses for his bots."""
from __future__ import annotations

import io
import logging
import logging.config
import sys
import warnings
from typing import TYPE_CHECKING, List, Optional, Tuple

import praw
import psycopg2
import sentry_sdk
from credmgr import CredentialManager
from psycopg2 import extensions
from psycopg2.extras import NamedTupleCursor

log = logging.getLogger(__name__)
dev_mode = sys.platform == "darwin"

if TYPE_CHECKING:  # pragma: no cover
    import asyncpraw as _asyncpraw
    from sqlalchemy.orm import declarative_base, scoped_session


class BotServices:
    """Provide services for bots."""

    def __init__(self, bot_name: str, api_token: Optional[str] = None):
        """Initialize the bot services.

        :param bot_name: The name of the bot.
        :param api_token: The API token to pass to credmgr.

        """
        self.bot_name = bot_name
        self.server = None
        self.credmgr = CredentialManager(api_token=api_token)
        self.bot = self.credmgr.bot(bot_name)
        self._reddit_instances = {}

    def reddit(
        self,
        username: str,
        *,
        asyncpraw: bool = False,
        bot_name: Optional[str] = None,
        reddit_class: Optional[praw.Reddit | _asyncpraw.Reddit] = None,
        use_cache=True,
    ) -> praw.Reddit | _asyncpraw.Reddit:
        """Provide an authenciated reddit instance.

        :param username: Redditor to authenticate as.
        :param asyncpraw: Whether to use asyncpraw.
        :param bot_name: Specify a different bot name than what is set at the instance
            scope.
        :param reddit_class: An alternate reddit class. If this is specified,
            ``asyncpraw`` will be ignored.
        :param use_cache: Whether to use the cached reddit instance.

        :returns: A Reddit instance.

        """
        if not self._reddit_instances.get(username, None) or not use_cache:
            if not reddit_class:
                if asyncpraw:
                    import asyncpraw

                    reddit_class = asyncpraw.Reddit
                else:

                    reddit_class = praw.Reddit
            if bot_name:
                return self.credmgr.bot(bot_name).reddit_app.reddit(
                    username, reddit_class=reddit_class, use_cache=False
                )
            else:
                self._reddit_instances[username] = self.bot.reddit_app.reddit(
                    username, reddit_class=reddit_class, use_cache=False
                )
        return self._reddit_instances.get(username)

    def _getDbConnectionSettings(self, *args, **kwargs) -> dict[str, str]:
        warnings.warn(
            "This method is deprecated. Use ``get_db_connection_settings`` instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.get_db_connection_settings(*args, **kwargs)

    def get_db_connection_settings(
        self, bot_name: Optional[str] = None
    ) -> dict[str, str]:
        """Provide the database connection settings.

        :param bot_name: Specify a different bot name than what is set at the instance
            scope.

        :returns: A dictionary of database connection settings.

        """
        if bot_name:
            settings = self.credmgr.bot(bot_name).database_credential
        else:
            settings = self.bot.database_credential
        params = {
            "database": settings.database,
            "user": settings.database_username,
            "password": settings.database_password,
            "host": settings.database_host,
            "port": settings.database_port,
        }
        if settings.use_ssh:
            from sshtunnel import SSHTunnelForwarder

            if not self.server:
                if settings.useSshKey:
                    auth_params = {
                        "ssh_pkey": io.StringIO(settings.private_key),
                        "ssh_private_key_password": settings.private_key_passphrase,
                    }
                else:
                    auth_params = {"ssh_password": settings.ssh_password}
                self.server = SSHTunnelForwarder(
                    (settings.ssh_host, settings.ssh_port),
                    ssh_username=settings.ssh_username,
                    **auth_params,
                    remote_bind_address=(
                        settings.database_host,
                        settings.database_port,
                    ),
                    logger=log,
                )
            self.server.start()
            log.debug("server connected")
            params["port"] = self.server.local_bind_port
        return params

    def postgres(
        self,
        bot_name: Optional[str] = None,
        cursor_factory: extensions.cursor = NamedTupleCursor,
        max_attempts: int = 5,
    ) -> extensions.cursor:
        """Provide an authenicated PostgreSQL cursor.

        :param bot_name: Specify a different bot name than what is set at the instance
            scope.
        :param cursor_factory: An alternate cursor factory.
        :param max_attempts: The maximum number of attempts to connect to the database.

        :returns: A psycopg2 cursor.

        """
        params = self.get_db_connection_settings(bot_name)
        attempts = 0
        cursor = None
        try:
            while not cursor and attempts < max_attempts:
                attempts += 1
                try:
                    postgres = psycopg2.connect(**params, cursor_factory=cursor_factory)
                    postgres.autocommit = True
                    return postgres.cursor()
                except Exception as error:
                    log.exception(error)
        except Exception as error:
            log.exception(error)

    def sqlalc(
        self,
        bot_name: Optional[str] = None,
        flavor: str = "postgresql",
        scoped: bool = False,
        schema: Optional[str] = None,
        engine_kwargs: Optional[dict] = None,
        session_kwargs: Optional[dict] = None,
        base_class: type = object,
        create_all: bool = False,
    ) -> scoped_session | declarative_base():
        """Provide a sqlalchemy session or scoped Base.

        :param bot_name: Specify a different bot name than what is set at the instance
            scope.
        :param flavor: The flavor of the database.
        :param scoped: Whether to return a scoped Base.
        :param schema: The schema to use.
        :param engine_kwargs: Additional kwargs to pass to the engine.
        :param session_kwargs: Additional kwargs to pass to the session.
        :param base_class: The base class to use.
        :param create_all: Whether to create all the tables.

        :returns: A sqlalchemy session or scoped Base.

        """
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        params = self.get_db_connection_settings(bot_name)
        if flavor == "postgres":
            flavor = "postgresql"
        url = f"{flavor}://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
        session_kwargs = session_kwargs or {}
        engine_kwargs = engine_kwargs or {}
        engine = create_engine(url, **engine_kwargs)
        Session = sessionmaker(bind=engine, **session_kwargs)
        session = Session()
        if scoped:
            from sqlalchemy import event
            from sqlalchemy.ext.declarative import declarative_base
            from sqlalchemy.orm import mapper, scoped_session

            DBSession = scoped_session(Session)
            base_class = base_class or object

            @event.listens_for(mapper, "init")
            def auto_add(target, args, kwargs):
                for k, v in kwargs.items():
                    setattr(target, k, v)
                DBSession.merge(target)
                if not DBSession.autocommit:
                    DBSession.commit()

            class _Base(base_class):
                query = DBSession.query_property()
                if schema:
                    __table_args__ = {"schema": schema}

                @classmethod
                def get(cls, ident):
                    return cls.query.get(ident)

            Base = declarative_base(bind=session.bind, cls=_Base)
            if create_all:
                Base.metadata.create_all()
            return Base
        else:
            return Session()

    def logger(
        self,
        bot_name: Optional[str] = None,
        enable_loggers: Optional[List[Tuple[str, str]]] = None,
    ) -> logging.Logger:
        """Provide a logging instance.

        :param bot_name: Specify a different bot name than what is set at the instance
            scope.
        :param enable_loggers: A list of tuples of packages and logging level names,
            e.g., ``[("discord", "INFO")]``.

        :returns: A logging instance.

        """
        if not enable_loggers:
            enable_loggers = []
        try:
            if bot_name:
                settings = self.credmgr.bot(bot_name).sentry_token
            else:
                settings = self.bot.sentry_token
        except Exception:
            settings = None
        log_colors = {
            "DEBUG": "bold_cyan",
            "INFO": "bold_green",
            "WARNING": "bold_yellow",
            "ERROR": "bold_red",
            "CRITICAL": "bold_purple",
        }
        secondary_log_colors = {
            "message": {
                "DEBUG": "bold_cyan",
                "INFO": "bright_white",
                "WARNING": "bold_yellow",
                "ERROR": "bold_red",
                "CRITICAL": "bold_purple",
            }
        }
        colors = {
            "log_colors": log_colors,
            "secondary_log_colors": secondary_log_colors,
        }
        formatter = {
            "style": "{",
            "()": "colorlog.ColoredFormatter",
            "format": "{asctime} [{log_color}{levelname:^9}{reset}] [{cyan}{name}{reset}] [{blue}{funcName}{reset}] [{yellow}{filename}:{lineno}{reset}] {message_log_color}{message}{reset}",
            "datefmt": "%m/%d/%Y %I:%M:%S %p",
            **colors,
        }
        config = {
            "disable_existing_loggers": False,
            "version": 1,
            "formatters": {"default": formatter},
            "handlers": {
                "consoleHandler": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {
                bot_name: {"level": "INFO", "handlers": ["consoleHandler"]},
                __name__: {
                    "level": "DEBUG",
                    "handlers": ["consoleHandler"],
                },
                **{
                    logger_name: {
                        "level": level.upper(),
                        "handlers": ["consoleHandler"],
                    }
                    for logger_name, level in enable_loggers
                },
            },
        }
        if not dev_mode and settings:
            sentry_sdk.init(
                dsn=settings.dsn,
                attach_stacktrace=True,
                send_default_pii=True,
                environment="production",
            )
        logging.config.dictConfig(config)
        return logging.getLogger(bot_name)


if __name__ == "__main__":
    credmgr = CredentialManager()
    name = "SiouxBot"
    services = BotServices(name)
    sql = services.postgres()
    log = services.logger()
    log.info("test")
    reddit = services.reddit("siouxsie_siouxv2")
    sql.execute("select 1")
    results = sql.fetchall()
    log.info(results)
    log.info(reddit.user.me())
