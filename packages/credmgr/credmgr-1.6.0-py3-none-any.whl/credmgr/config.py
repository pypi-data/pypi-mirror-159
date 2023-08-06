"""Provides the code to load credmgr's configuration file `~/.credmgr.ini`."""
import configparser
import os
import sys
import warnings
from pathlib import Path
from threading import Lock


class Config:
    """Class for loading credmgr's config."""

    _config = None
    _lock = Lock()

    @staticmethod
    def _append_file_name(dirname):
        return os.path.join(dirname, ".credmgr.ini")

    @classmethod
    def _load_config(cls):
        """Attempt to load settings from various .credmgr.ini files."""
        config = configparser.ConfigParser()
        root_dir = os.path.dirname(sys.modules[__name__].__file__)
        locations = [
            cls._append_file_name(root_dir),
            cls._append_file_name(Path.home()),
            ".credmgr.ini",
        ]
        config.read(locations)
        cls._config = config

    def __init__(self, config_name, **kwargs):
        """Initialize a Config instance."""
        with Config._lock:
            if Config._config is None:
                self._load_config()
        self._settings = kwargs
        self.custom_settings = dict(
            Config._config.items(config_name),
            **{k.lower(): v for k, v in kwargs.items() if v},
        )
        self.server = self.api_token = self.username = self.password = None
        self._initialize_config()

    def _fetch(self, key, default=None):
        config_file_value = self.custom_settings.pop(key.lower(), default)
        env_override = os.getenv(f"credmgr_{key}")
        return env_override or config_file_value

    def _initialize_config(self):
        self.server = self._fetch("server")
        self.endpoint = self._fetch("endpoint")
        old_token = self._fetch("apitoken")
        new_token = self._fetch("api_token")
        if old_token and not new_token:  # pragma: no cover
            warnings.warn(
                "apitoken is deprecated, use api_token instead.",
                DeprecationWarning,
                stacklevel=3,
            )
        self.api_token = new_token or old_token
        self.username = self._fetch("username")
        self.password = self._fetch("password")
