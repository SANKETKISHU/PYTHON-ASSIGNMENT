time=int(input("Enter a time:"))
time=time+51
a=time%12
b=time//12
if(b%2==0):
	c="AM"
else:
	c="PM"
print("The Time after adding 51hrs is :", a, c)