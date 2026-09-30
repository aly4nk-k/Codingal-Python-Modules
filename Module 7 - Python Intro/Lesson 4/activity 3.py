# task = print the sum of first n positive num

n = int(input("Enter a number : "))
sum = 0

for i in range(1,n + 1):
    sum = sum + i

print(sum)

#----------------------------

# while loop

i = 1
sum = 0
while i <= n:
    sum = sum + i 
    i = i + 1
    print(sum)