# coding: utf-8

import functools
import typing
import inspect


def inject_call(fn, *args, **kwargs):
    """
    Call function without known all the arguments

    Args:
        fn: function
        args: arguments
        kwargs: key-values
    
    Returns:
        as the fn returns
    """
    assert callable(fn), "first argument must be callable"

    # signature(callable)函数，可以获取签名
    # 函数签名包含了一个函数的信息，包括：函数名、参数类型、函数所在的类和名称空间及其他信息
    st = inspect.signature(fn)
    # 简便写法值得学习
    fn_kwargs = {
        key: kwargs[key]
        for key in st.parameters.keys() if key in kwargs
    }
    # 把任意个参数绑定到签名中的形参上, 可以使用这个方法在真正调用函数前验证参数是否传递
    ba = st.bind(*args, **fn_kwargs)
    ba.apply_defaults()
    return fn(*ba.args, **ba.kwargs)


def limit_call_depth(n: int):
    """
    n = 0 means not allowed recursive call
    """
    def wrapper(fn: typing.Callable):
        if not hasattr(fn, '_depth'):
            fn._depth = 0

        @functools.wraps(fn)
        def _inner(*args, **kwargs):
            if fn._depth > n:
                raise RuntimeError("call depth exceed %d" % n)

            fn._depth += 1
            try:
                return fn(*args, **kwargs)
            finally:
                fn._depth -= 1
        
        _inner._fn = fn
        return _inner
    
    return wrapper


def main():
    @limit_call_depth(1)
    def foo(a):
        print("Foo:", a)
        if a == 2:
            return
        foo(a+1)

    foo(0)

if __name__ == "__main__":
    main()