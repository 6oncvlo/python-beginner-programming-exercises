def fizz_buzz():
    # your code here
    for k in range(1,101):
        if k%3==0 and k%5==0:
            print("FizzBuzz")
        elif k%3==0 and k%5!=0:
            print("Fizz")
        elif k%3!=0 and k%5==0:
            print("Buzz")
        else:
            print(k)


fizz_buzz()