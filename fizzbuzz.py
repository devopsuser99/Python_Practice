
for fizzbuzz in range (101):
    if fizzbuzz % 3 ==0 and fizzbuzz  % 5==0:
        print("FizzBuzz")
    elif fizzbuzz % 5 ==0:
        print("Fizz")
    elif fizzbuzz % 3 ==0:
        print("Buzz")
        continue
    print(fizzbuzz)