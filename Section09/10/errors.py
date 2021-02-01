def add(n1,n2):
    print(n1+n2)

number1 = 10 
number2 = input("please provide a number")

# type error will happen because the input will come back as a string

try:
    # want to attempt this code
    # it may have an error

    result = 10 + '10'
except:
    # If there is an error
    # can add type check for error
    # ex. expect TypeError: 
    print('Hey it looks like you arent adding correctly')

else:
    # If there isnt an error
    print('add went well')
    print(result)

finally:
    # always runs even after catching errors
    print("I always run")