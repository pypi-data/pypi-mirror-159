import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent

TEMPLATE_DIR = BASE_DIR / 'templates'

VAR_DIR = BASE_DIR.parent / 'var'

LOGGING = {
    'version': 1,
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG'
    },
    'handlers': {
        'console': {
            'formatter': 'std_out',
            'class': 'logging.StreamHandler',
            'level': 'DEBUG'
        },
        'file': {
            'formatter': 'std_out',
            'class': 'logging.TimedRotatingFileHandler',
            'level': 'INFO',
            'filename': 'all_messages.log',
            'backupCount': 7
        }
    },
    'formatters': {
        'std_out': {
            'format': '%(levelname)s : %(module)s : %(funcName)s : %(message)s',
        }
    },
}

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
