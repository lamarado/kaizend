name = input("What is your name? ")
birthdate = input("What is your birthdate? ")
age = int(input("How old are you? "))

print(f"{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}")

def say_hello(name):
    print(f"Hello {name}!")

say_hello(name)
