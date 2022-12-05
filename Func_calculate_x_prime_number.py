"""This function print a list of x prime numbers followed by the input"""
contador = 0
last_prime = 1
next_number = 2
list = [last_prime]

def is_prime (y):
    for x in range (2, y):
        if y%x == 0:
            return False
        if y == x+1: 
            return True
        
def calculate(x):
    while contador < x-1:
        next_number = next_number + 1
        if is_prime(next_number):
            contador+= 1
            last_prime = next_number
            list.append(last_prime)
    print(list)
    
if __name__ == "__main__":
    x = int(input("por favor escribe un numero entero:"))
    calculate(x)