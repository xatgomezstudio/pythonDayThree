# python learning DAY 3

# ------------------------------------- IF STATEMENTS -------------------------------------
# Ex1
# variables
is_techBro = True

if is_techBro:
    # anything written inside this block will run when the if statement above has a true boolean
    print("Because I am Male,")

# Ex2
# variables have EQUAL SIGNS
is_cosmoNaut = True
is_whitePrivilege = False

# if statement has COLONS
if is_cosmoNaut and is_whitePrivilege:
    print("and life is a movie")
# elif stand for 'else if'
elif is_whitePrivilege and not(is_cosmoNaut):
    print("how do I have privilege if I'm not rich?")
elif is_cosmoNaut and not(is_whitePrivilege):
    print("you're not real, just a projection of my mind.")
else:
    print(" and I manifested it!")

print("--------------------------------------------------------------")

# Ex3

is_Queer = True
is_Poc = True
is_Male = False

if is_Male and is_Poc:
    print("Brown boy magic!")
elif is_Male and not(is_Queer):
    print("Cute cup of milk!")
elif is_Poc and not(is_Male):
    print("Oat milk baddie!")
elif is_Poc and is_Queer:
    print("Lavender oat milk latte stat!!")
else:
    print("Either way you're cute!")

print("--------------------------------------------------------------")
# ------------------------------------- COMPARISONS -----------------------------------

# applying a function
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        #    ^ comparison operator
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

print("--------------------------------------------------------------")

# ------------------------------------- BUILDING A BETTER CALCULATOR -----------------------------------

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))


# if op == "+":
    # print(num1 +num2)

# elif op == "-":
   # print(num1 - num2)

# elif op == "*":
  #  print(num1 * num2)

# elif op == "/":
  #  print(num1 / num2)

# elif op == "//":
   # print(num1 // num2)

# elif op == "%":
  #  print(num1 % num2)

# elif op == "**":
  #  print(num1 ** num2)

# else:
  #  print("Well shit idk")

# ------------------------------------- DICTIONARIES ----------------------------------

monthConversions = {
    "Jan": "January",
    # ^key     ^value
    "Feb": "February",
    # EACH KEY HAS TO BE UNIQUE, or else you'll get an error
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
# keys ^ can also be numbers
}

print(monthConversions["Mar"])
# or you could also use this method below
print(monthConversions.get("Nov"))
# what's nice about this option is that it will return NONE instead of an error when wrong
print(monthConversions.get("Luv"))

print("---------------------------------------------")

# ------------------------------------- WHILE LOOP ----------------------------------

# variables
i = 1

# the 'condition' can also be called a 'loop guard'
# the while loop will repeat for as long as the CONDITION is TRUE
while i <= 10:
    # this is the code inside the while loop
    print(i)
    # i = i + 1
    # or we can shortcut that by writing i += 1
    i += 1

print("Done with loop")

print("---------------------------------------------")

# ------------------------------------- BASIC GUESSING GAME IN PYTHON ----------------------------------

secretWord = "Thailand"
guess = ""
# strings that need to match

guessCount = 0
guessLimit = 3
# numbers that need to match

out_of_guesses = False
# boolean that needs to match

while guess != secretWord and not(out_of_guesses):
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        out_of_guesses = True
    # this ELSE changes the ^ booleans value to TRUE once the guess count number matches the limit variable

# when they break out of the loop they are either A or B, and code will check each
# AAAA
if out_of_guesses:
    print("Wrong! Believe it or not, straight to jail!")
# once that out_of_guesses boolean is changed to TRUE in the previous loop it triggers this reaction

# BBBB
else:
    print("You win!")

