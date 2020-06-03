# Find a no is palindrome or not
num = int(input("Enter a number:"))
temp = num
rev = 0
while num > 0:
    dig = num % 10  # modulus
    rev = rev * 10 + dig  # reverse
    num = num // 10  # we do this so that we make our value in integers
if temp == rev:
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

# find a string is palindrome or not
string = input("Enter a string:")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("Not a palindrome")