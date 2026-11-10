def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def describe(a, b):
    print("Adding two numbers:")
    print(f"Added: {a} + {b} = {add(a, b)}")
    return add(a, b)


def broken_total():
    return missing_total
