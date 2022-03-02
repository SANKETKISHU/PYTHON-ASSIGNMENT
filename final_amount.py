P=10000
N=12
R=8/100
T=int(input("Enter time: "))
A=P*(1+R/N)**(N*T)
print(int(A))