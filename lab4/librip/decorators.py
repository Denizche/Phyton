def print_result(func_to_decorate):
    def decorated_func(*args):
        res = func_to_decorate(*args)
        print(func_to_decorate.__name__)
        if type(res) in (str,int):
            print(res)
        if type(res) is list:
            [print(i) for i in res]
        if type(res) is dict:
            for y, z in res.items():
                print('{} = {}'.format(y, z))
        return res

    return decorated_func
