from dotenv import load_dotenv, find_dotenv
import os

#locate the .env file
load_dotenv(find_dotenv())


class Config:
    """Use the Environment Variables from .env"""
    
    #Set the variables for the website
    TESTING = os.getenv('TESTING')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG')
    SERVER_NAME = os.getenv('SERVER_NAME')

    #Set the database variable for SQLAlchemy
    DATABASE_STRING = os.getenv('DATABASE_STRING')
    
    
    
    