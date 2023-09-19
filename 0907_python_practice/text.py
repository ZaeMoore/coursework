# :)

a1 = [1, 2, 3, 4]
a = 5
a + a
a - a
a / a
a * a
a ** (0.5)

if a > 5:
    a = 10

elif a == 5:
    a = 5

#for x in a1:
    #print(x)

#for x in range(10): #this will start at 0 and go to 9
    #print(x)

b = 0
while b < 10: #this will print from 1 to 10
    b += 1
    #print(b)

def fibonacci(n):
    n1 = 0
    n2 = 1

    for i in range(n - 2):
        ans = n1 + n2
        n1 = n2
        n2 = ans
    return ans

n = int(input("n = "))
print(fibonacci(n))

