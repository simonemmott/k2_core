import os
import yaml
import json
import logging
import logging.config
from k2_core import configuration

default_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {name} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {name} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'root': {
        'propagate': True,
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'propagate': True,
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}

def get_logging_config(path=None, default_level=logging.INFO, env_key='LOG_CFG'):
    config_path = None
    if path:
        config_path = path
    if not config_path:
        config_path = os.getenv(env_key, None)
    if not config_path:
        config_path = configuration.config.get('DEFAULT', 'logging_config')
    if not config_path:
        config_path = 'logging.yaml'
        
    config_path = configuration.find(config_path)
    
    config_format = configuration.config.get('DEFAULT', 'logging_config_format')
    if not config_format:
        config_format = 'YAML'
        
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            try:
                if config_format.upper() == 'YAML':
                    return yaml.safe_load(f.read())
                elif config_format.upper() == 'JSON':
                    return json.loads(f.read())  
            except Exception as e:
                print(e)
                print('Error in logging configuration file: {file} Using default configs'.format(file=config_path))
                return default_config
    else:
        logging.basicConfig(level=default_level)
        return default_config
