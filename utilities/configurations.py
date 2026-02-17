import configparser
import os
from typing import Any, Dict, Optional

import mysql.connector
from mysql.connector import Error


DEFAULTS: Dict[str, Dict[str, str]] = {
    "API": {"endpoint": os.getenv("API_ENDPOINT", "http://216.10.245.166")},
    "SQL": {
        "user": os.getenv("DB_USER", ""),
        "password": os.getenv("DB_PASSWORD", ""),
        "host": os.getenv("DB_HOST", ""),
        "database": os.getenv("DB_NAME", ""),
    },
}


def getConfig() -> configparser.ConfigParser:
    """Load config with safe defaults.

    Backwards compatible with `utilities/properties.ini`, while allowing
    environment-variable based configuration in CI and local runs.
    """
    config = configparser.ConfigParser()
    config.read_dict(DEFAULTS)
    config.read("utilities/properties.ini")
    return config


def get_db_connect_config() -> Dict[str, str]:
    cfg = getConfig()
    return {
        "user": cfg["SQL"].get("user", ""),
        "password": cfg["SQL"].get("password", ""),
        "host": cfg["SQL"].get("host", ""),
        "database": cfg["SQL"].get("database", ""),
    }


def getConnection() -> Optional[mysql.connector.MySQLConnection]:
    """Open DB connection when DB settings are provided, else return None."""
    connect_config = get_db_connect_config()
    if not all(connect_config.values()):
        return None

    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            return conn
    except Error as exc:
        print(exc)
    return None


def getQuery(query: str) -> Any:
    conn = getConnection()
    if conn is None:
        raise RuntimeError(
            "Database connection is not configured. Set DB_* env vars or utilities/properties.ini"
        )

    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
