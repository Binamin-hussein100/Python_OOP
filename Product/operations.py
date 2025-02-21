def add(*args, **kwargs):
    total = 0
    print(args)
    for num in args:
        total += num
        
    print(total)

add(2,6,1,29,23)

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="john doe", age=90, city="Nairobi")

def subtract(a,b):
    return a - b

subtract(3,2)