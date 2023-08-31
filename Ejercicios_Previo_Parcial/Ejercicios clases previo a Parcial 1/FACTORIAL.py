print("Este programa calcula el factorial")
n = int(input("Ingrese el número del cuál quiere saber el factorial:"))
factorial = 1
for i in range(n+1):
    if i == 0:
        factorial = 1
    else:
        factorial *= i
print("Factorial de", n, ":", factorial)
