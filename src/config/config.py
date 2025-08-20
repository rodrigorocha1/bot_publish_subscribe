import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    URL_API = os.environ['URL_CITYBIKE']
    USR_RABBITMQ = os.environ['USR_RABBITMQ']
    PWD_RABBITMQ = os.environ['PWD_RABBITMQ']
    HOST_RABBITMQ = os.environ['HOST_RABBITMQ']
    PORTA_RABBITMQ = os.environ['PORTA_RABBITMQ']
    URL_DISCORD = os.environ['URL_DISCORD']
    TOKEN_TELEGRAM = os.environ['TOKEN_TELEGRAM']
    CHAT_ID = os.environ['CHAT_ID']
