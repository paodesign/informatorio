from .base import *
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'BDTPFINAL',
        'Trusted_Connection':'yes',
        'HOST': 'I7-HP',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}