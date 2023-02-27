logging_list = open("C:/Users/Sirichaggy/Desktop/sss/debug_log.py", 'w', encoding = 'utf-8')
def trace(func):
    def inner_func(*args, **kwargs):
        func(*args, **kwargs)
        logging_list.write("Information: {}".format(logging.Formatter))
        r = func(*args, **kwargs)
        return r
    return inner_func





logging_list = open("C:/Users/Sirichaggy/Desktop/sss/debug_log.py", 'w', encoding = 'utf-8')

class Log:
    def __init__(self, *args, **kwargs):
        pass
    def __call__(func):
        def inner_func(*args, **kwargs):
            func(*args, **kwargs)
            logging_list.write("Information: {}".format(logging.Formatter))
            r = func(*args, **kwargs)
            return r
        return inner_func