#Problem 5 : Frequency of each element in List

# Taking list as input and sorting
print("Enter a list of integers: ")
N=list(map(int,input().split()))
N.sort()

d={}            #Empty Dictionary
for x in N :
    if x not in d :
        d[x]=1
    else :
        d[x]+=1
        
print (len(d)) 
for i in d :
    print (i,":",d[i])


    
