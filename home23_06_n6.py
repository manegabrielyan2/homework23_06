#outer, inner function
def outer_function(x):
    def inner_function():
        factor = 20
        return x*factor
    return inner_function
x = outer_function(5)
print(x())


