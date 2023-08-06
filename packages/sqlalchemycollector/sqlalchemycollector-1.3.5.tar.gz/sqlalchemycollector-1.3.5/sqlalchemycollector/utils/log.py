from __future__ import division, absolute_import, print_function, unicode_literals

import functools
from collections import defaultdict

import sys
import logging

ULTRA_VERBOSE = True
MAX_ARG_LEN = 256
MAX_CALLS = {}
MAX_LOGGING_SIZE = -1  # If -1 ignore log limit

logger = logging.getLogger(__name__)

if ULTRA_VERBOSE:
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
        stream=sys.stdout)

call_counter = defaultdict(int)
logging_size = 0


def log_and_raise(func):
    return log(func, True)


def log(should_throw: bool = False):
    def _log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def _to_string(obj):
                try:
                    return repr(obj)
                except:
                    try:
                        return str(obj)
                    except:
                        return f'{obj.__name__}'

            def to_string(obj):
                res = _to_string(obj)
                return res if len(res) <= MAX_ARG_LEN else f'{res[:MAX_ARG_LEN]}...'

            global logging_size, call_counter

            if -1 < MAX_LOGGING_SIZE < logging_size:
                return

            func_name = f'{func.__module__}.{func.__name__}'
            if func_name in MAX_CALLS and call_counter[func_name] > MAX_CALLS[func_name]:
                return
            call_counter[func_name] += 1
            args_repr = [to_string(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            message = f"function {func_name} (call #{call_counter[func_name]}) called with args {signature}"
            message_len = len(message) + 1
            logger.debug(message)
            logging_size += message_len
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exception_string = f"Exception raised in {func_name}. Exception: {str(e)}"
                logger.exception(exception_string)
                logging_size += len(exception_string) + 1
                if should_throw:
                    raise e
            finally:
                logger.debug(f"{message} DONE!")
                logging_size += message_len + 6

        return wrapper

    return _log
