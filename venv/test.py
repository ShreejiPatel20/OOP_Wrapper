number=input("Enter your number: ")
sum=0
i=0

while i<len(number):
    sum+=int(number[i])
    i += 1

print(sum)