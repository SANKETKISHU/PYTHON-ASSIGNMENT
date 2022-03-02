num = int(input("ENTER THE NUMBER :- "))
v=num
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if(v==reversed_num):
    print("This value is a palindrome number!")  
else:
    print("This value is not a palindrome number!")  