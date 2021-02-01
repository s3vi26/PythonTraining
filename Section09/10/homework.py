# Problem 1
try:
  for i in ['a','b','c']:
      print(i**2)
except TypeError:
  print('The values are strings and need to be int')

# Problem 2
try:
  x = 5
  y = 0

  z = x/y
except ZeroDivisionError:
  print(f'y is {y}. You cannot divide by {y}.')
finally:
  print("All Done")

# Problem 3
def ask():
  while True:
    try:
      result = int(input('Please provide an Int: '))
    except ValueError:
      print('That is not an integar')
      continue
    else:
      print(f"Thank you, your number is: {result}")
      break
    finally:
      print("All Done")
