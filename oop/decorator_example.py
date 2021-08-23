def add_parenthesis(lambda text: f(text)):
    def function_to_return(text):
        print('(', end='')
        f()
        print(')')
    return function_to_return

@add_parenthesis()
def f(text):
    print(f"hello{text}", end='')

f("hi")
