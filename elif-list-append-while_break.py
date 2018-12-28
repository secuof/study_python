a = [1,2,3,4,5,6,7]
resutl = []

for num in a:
        resutl.append(num*4)
print(resutl)

a = "Life is too short, you need python"
if "wife" in a:
        print("wife")
elif "Life is asdf" in a:
        print("asdfasdfasdf")
elif "python" in a and "you" not in a:
        print("python")
elif "shirt" not in a:
        print("shirt")
elif "need" in a:
        print("need")
else:
        print("none")

i = 0
while True:
        i += 1
        if i > 10: 
                break
        print('*' * i)

b = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
person = len(b)
for x in b:
        print(x)
        total += x
average = total / person
print (average)