import os
import sqlite3


class Config:
    """Base configuration class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Used for security


class DevelopmentConfig(Config):
    """Development environment configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///games.db'  # SQLite (for local development)


class ProductionConfig(Config):
    """Production environment configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/game_db')  # PostgreSQL


# Choose the config based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
