from .jsonplaceholder import *
import logging
import inspect
import time
import requests


__all__ = [
    'jsonplaceholder',
]

__title__ = 'pypodadmin'

__url__ = 'https://github.com/EricDalrymple91/pyplaceholder'

__version__ = '0.2'

__author__ = 'Eric Dalrymple'

__co_authors__ = [
]

__copyright__ = 'Copyright 2021 MIT'

# Logging setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.getLogger("requests").setLevel(logging.WARNING)

TIMEOUT = 30

RAISE_STATUS = True

RESPONSE_AS_JSON = True


def set_logfile(file_path):
    log = logging.getLogger()

    # remove all old handlers
    for hdlr in log.handlers[:]:
        log.removeHandler(hdlr)

    fileh = logging.FileHandler(file_path, 'a')
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fileh.setFormatter(formatter)

    log.addHandler(fileh)


# Send a request that is thoroughly logged
def request(method, url, **kwargs):

    # Log
    stack = inspect.stack()

    request_name = f'{stack[1][0].f_locals["self"].__class__.__name__}.{stack[1][0].f_code.co_name}'

    logger.info(f'[{request_name}] Request method: {method}')

    logger.debug(f'[{request_name}] Input URL: {url}')

    # Log kwargs
    for k in kwargs:
        logger.debug(f'[{request_name}] {k}: {kwargs[k]}')

    # Send request and log time taken
    start_time = time.time()

    response = requests.request(method, url, **kwargs)

    logger.info(f'[{request_name}] Took: {time.time() - start_time} s')

    # Log response attributes
    logger.info(f'[{request_name}] Response URL: {response.url}')

    logger.info(f'[{request_name}] Response status code: {response.status_code}')

    logger.debug(f'[{request_name}] {response.content}')

    if RAISE_STATUS:
        raise_status(response)

    return response.json() if RESPONSE_AS_JSON else response
