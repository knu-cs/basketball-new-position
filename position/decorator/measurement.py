import time


def measure_time(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        a = original_function(*args, **kwargs)
        end_time = time.time()
        print("실행시간[{}]: {} sec".format(original_function.__name__, end_time - start_time))
        return a

    return wrapper_function
