# Decorators


def message_decorator(function):

    def wrapper():
        print("Starting function...")
        function()
        print("Function finished.")

    return wrapper


@message_decorator
def greet():
    print("Hello, Subathra!")


greet()