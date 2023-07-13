#pow
def power_of(n):
    def power(num):
        return num ** n
    return power
result = power_of(2)
print(result(4))
print(result(9))
print(result(10))
res2 = (power_of(3))(4)
print(res2)