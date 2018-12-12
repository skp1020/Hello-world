#Problem 1 :Fibonacci Numbers

a=[0,1]  #Predefined list
n=int(input("Enter length of fibnacci series : "))

for i in range(2,n) :
    ans=a[i-2]+a[i-1]
    a.append(ans)

print ("Fibonacci Series : ")
for i in range(0,n) :
    print (a[i])




