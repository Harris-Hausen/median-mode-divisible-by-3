
def median(*args):
  if len(args) == 0:
      return None

  sorted_args = sorted(args)
  length = len(sorted_args)
  mid = length // 2

  if length % 2 == 0:
      return (sorted_args[mid - 1] + sorted_args[mid]) / 2
  else:
      return sorted_args[mid]



while True:
  user_input = input("Enter the numbers you want to find for the median")
  if not user_input:
    print("That is not a valid response please try again")
  else:
    numbers= (float(num) for num in user_input.split())
    print("Median:", median(*numbers))
    break

def check_divisible():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))

  if num1 % 3 == 0 and num2 % 3 == 0:
      print("Both numbers are divisible by 3.")
  elif num1 % 3 == 0:
      print("Only the first number is divisible by 3.")
  elif num2 % 3 == 0:
      print("Only the second number is divisible by 3.")
  else:
      print("Neither number is divisible by 3.")


check_divisible()
  
from collections import Counter
def average(*args):
  if len(args) == 0:
      return None

  total = 0
  count = 0
  for num in args:
      total += num
      count += 1

  return total / count

while True:
  user_input = input("Enter the numbers you want to find the average of and separate them with a comma: ")
  if not user_input:
   break
  avg = average(*numbers)
  print("Average:", avg)


def mode(*args):
  if not args: 
    return None
  num_counts = Counter(args)
  max_count = max(num_counts.values())
  mode = [num for num , count in num_counts.items() if count == max_count]
#num_counts [(1,3), (27, 4), (4,3)]
#num_counts.items() creates a list from a dictionary
#the list is an array of pairs
  return mode
user_input = input("What numbers do you want to use for the mode? ")
numbers = [
  int(num) for num in user_input.split()
]

result = mode(*numbers)

if result:
    if len(result) == 1:
        print(f"The mode is: {result[0]}")

    else:
      print(*result)
      
mode(*numbers)
  