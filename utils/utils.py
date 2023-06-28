def check_type(*args : tuple) -> None:
    for arg in args:
        if not isinstance(arg[0], arg[1]):
            raise TypeError(f"Expected {arg[1]} got {type(arg[0])}")