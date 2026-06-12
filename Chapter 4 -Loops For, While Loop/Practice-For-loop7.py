# sum =0
# sum= sum + 1 
# sum= sum + 4
# sum= sum + 5
# sum= sum + 7
# sum= sum + 10
# sum= sum + 16

n=int(input("tell me number"))
sum= 0
for i in range(1,n+1):
    sum = sum + i
    print(f"your sum is {sum}")