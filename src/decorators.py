import logging
from functools import wraps

def log(filename=None):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                log_message = f'{function.__name__} ok'

                if filename:
                    with open(filename, 'a', encoding = 'utf-8') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)

                return result
            except Exception as e:
                error_type = type(e).__name__

                log_message = f'{function.__name__} error: {error_type}. Inputs: {args}, {kwargs}'

                if filename:
                    f.write(log_message + '\n')
                else:
                    print(log_message)

                raise e
        return wrapper
    return decorator








