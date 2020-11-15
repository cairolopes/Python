"""
Applying Multiple Decorators to a Single Function
"""
# def uppercase_decorator(function):

#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase

#     return wrapper

# def split_string(function):

#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper

# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello there'

# print(say_hi())
"""
Accepting Arguments in Decorator Functions
"""
# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print(f"My arguments are {arg1}, {arg2}")
#         function(arg1, arg2)
    
#     return wrapper_accepting_arguments

# @decorator_with_arguments
# def cities( city_one, city_two):
#     print(f"Cities I love are {city_one} and {city_two}")

# cities("Nairobi", "Accra")
    
"""
Defining General Purpose Decorators
"""
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are', args)
#         print('The keyword arguments are', kwargs)
#         function_to_decorate(*args)

#     return a_wrapper_accepting_arbitrary_arguments


# @a_decorator_passing_arbitrary_arguments

# def function_with_no_arguments():
#     print("No arguments here.")

# function_with_no_arguments()

# @a_decorator_passing_arbitrary_arguments

# def function_with_arguments(a,b,c):
#     print(a,b,c)

# function_with_arguments(1,2,3)

# @a_decorator_passing_arbitrary_arguments
# def function_with_keyword_arguments():
#     print("This has show keyword arguments")

# function_with_keyword_arguments(first_name="Cairo", last_name="Lopes")

    
"""
Defining General Purpose Decorators
"""
# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
#     def decorator(func):
#         def wrapper(*args): #function_arg1, function_arg2, function_arg3
#             "This is the wrapper function"
#             function_arg1, function_arg2, function_arg3 = args[0],args[1],args[2]
#             print(" The wrapper can access all the cariables\n"
#                 f"\t - from the decorator maker: {decorator_arg1} {decorator_arg2} {decorator_arg3} \n"
#                 f"\t - from the function call: {function_arg1} {function_arg2} {function_arg3}\n"
#                 "and pass them to the decorated function")
            
#             return func(function_arg1, function_arg2, function_arg3)
#         return wrapper
#     return decorator

# pandas = "Pandas"

# @decorator_maker_with_arguments(pandas, "Numpy", "Scitkit-learn")
# def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
#     print("This is the decorated function and it only knows about its arguments: {0}"
#            " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

# decorated_function_with_arguments(pandas, "Science", "Tools")
    
"""
Debugging Decorators
"""
import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    
    return wrapper

@uppercase_decorator
def say_hi():
    "This will say hi"
    return "hello there"

print(say_hi())
print(say_hi.__name__)
print(say_hi.__doc__)