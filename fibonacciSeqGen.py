def fib(n):
    a=1
    b=1
    fib_seq = []
    fib_seq.append(a)
    fib_seq.append(b)
    for i in range(n):
        a,b = b,a+b
        fib_seq.append(b)

    return fib_seq[:n]

while True:
    try:
        num = int(input("Please enter a number: "))
    except:
        print("Invalid Input. Please try again.")
        continue
    else:
        print(fib(num))
    break
