#Tyler Shepherd, A02259244
#HW3 - If statements, Loops, Logic

# PROBLEM 3.4
for y in range(2):
    for x in range (7):
        print('@', end="")
    print()

# PROBLEM 3.9
digit = int(input("Please enter a 7-10 digit number: " ))
digit_length =len(str(digit))
remove_digit = int(digit_length -1)

if digit_length in (7, 8, 9, 10):
    new_digit = 10 ** remove_digit
    while(digit):
        print(digit // new_digit)
        digit = digit % new_digit
        new_digit = new_digit // 10
else: 
    print("You silly goose, enter a correct input next time")
    
# PROBLEM 3.11
control_check = 0
total_gallons = []
total_miles = []

while control_check == 0:
    gallons = eval(input("Please enter the gallons used (enter -1 to end):"))
    if gallons == -1:
        control_check = 1
    else:
        miles = eval(input("Please enter the miles driven:"))
        total_gallons.append(gallons)
        total_miles.append(miles)
        miles_per_gallon = miles / gallons
        print("The miles/gallon for this tank was", miles_per_gallon)
else:
    overall_miles_gallons = sum(total_miles) / sum(total_gallons)
    print("The overall average miles/gallons was", overall_miles_gallons)

# PROBLEM 3.12
palindrome = int(input("Please enter a 5 digit number:"))
palindrome_stored = palindrome
palindrome_reversed = 0

while palindrome != 0:
    digits = palindrome % 10
    palindrome_reversed = palindrome_reversed * 10 + digits
    palindrome = palindrome // 10

if palindrome_stored == palindrome_reversed:
    print("This is a palindrome!")
else:
    print("Sorry, this isn't a palindrome.")

# PROBLEM 3.14
pi = 0
numerator = 4
denomindator = 1
previous_value = 0

#LOOP TO FIND PI TO THE HUNDRETHS PLACE (COMMENT OUT THIS WHEN USING THOUSANDTHS LOOP)
for iteration in range (1,1000):
    calculate = 2 * (iteration % 2) -1
    pi += calculate * (numerator / denomindator)
    denomindator += 2
    
    if str(pi)[0:4] == str(3.14) and str(previous_value)[0:4] == str(3.14):
        print("iteration:",iteration, "pi:", str(pi)[0:4], "previous pi was also:", str(previous_value)[0:4], "IT's HERE TWICE IN A ROW!")
        break
        
    else:
        print("iteration:",iteration, "pi:", str(pi)[0:4])

    if iteration  > 1:
        previous_value =  pi
        
#LOOP TO FIND PI TO THE THOUSANDTHS PLACE (COMMENT OUT THIS WHEN USING HUNDRETHS LOOP)
#3.141 appears twice in a row at iteration 2455
# for iteration in range (1,3000):
#     calculate = 2 * (iteration % 2) -1
#     pi += calculate * (numerator / denomindator)
#     denomindator += 2
    
#     if str(pi)[0:5] == str(3.141) and str(previous_value)[0:5] == str(3.141):
#         print("iteration:",iteration, "pi:", str(pi)[0:5], "IT'S HERE!!!!!!!! previous pi was also:", str(previous_value)[0:5])
#         break
        
#     else:
#         print("iteration:",iteration, "pi:", str(pi)[0:5])

#     if iteration  > 1:
#         previous_value =  pi
