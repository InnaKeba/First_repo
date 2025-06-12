
first = int(input("Enter the first intenger"))
second = int(input("Enter the first intenger"))

gsd = min(first,second)

while not(first % gsd == 0 and second % gsd == 0):
     gsd -= 1
print(gsd)