time=int(input("Enter a time:"))
w=int(input("Enter waiting time:"))
time=time+w
a=time%12
b=time//12
if(b%2==0):
	c="AM"
else:
	c="PM"
print("The Time after adding waiting time is :", a, c)