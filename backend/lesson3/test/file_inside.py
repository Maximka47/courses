def print_name(name="Adam", *args, **kwargs):
    print("Hello, "+ name)
    for one_name in args:
        print("Goodbye, "+one_name)
    
    print("-------------------------")
    for name, surname in kwargs.items():
        print(f"Good day, {name} {surname}")
# arguments, keyword arguments(dictionary)