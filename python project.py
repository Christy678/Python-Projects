# Example 1
# Calculate the multiplication and sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = num1 * num2

if product <= 1000:
    print("Product is greater than or equal to 1000:", product)
else:
    print("Sum of the two numbers:", num1 + num2)
    
# Example 2
# Remove first 'n' characters from a string 
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
word = input("Enter your word: ")
print(remove_chars(word, 4))
print(remove_chars(word, 2))

# Example 3
# Friend activity timers
friends = ["Rolf", "Jane", "Anne", "Sarah", "Carolene"]
Last_seen = ["3:00", "12:00", "7:00", "5:00", "6:00"]

# Combine the two lists into a dictionary using zip
timers = dict(zip(friends, Last_seen))

print(timers)

def multiply():
    num1, num2 = map(int, input("Enter 2 numbers: ").split(','))
    results = num1 * num2
    return results

print(multiply())

# Example 4
# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for numbers in range(1, 101):
    if numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    else:
        print(numbers)
        
