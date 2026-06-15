
def combine_funcs(*funcs):
    def combined_func(*x, **y):
        for f in funcs:
            f(*x, **y)
    return combined_func   
