### doc string - use """ """

def say_hello():
    """ A simple function that returns the string hello"""
    return "Hello!"
print(say_hello().__doc__)

'''
Recap 

- functions are procedures for executing code. the accpet inputs and return outputs when the return keyword is used
- to create inputs, we make parameters which can have default values, we call those default parameters
- variables defined inside of functions are scoped to that function - watch out for that!
- when invoking a function we can pass i n keyword arguments in any order.
- be careful to not return too earlt in your conditional logic and refactor when you  can to remove unnecessary 
conditional logic. Make sure you dont return in a loop too early as well

'''

