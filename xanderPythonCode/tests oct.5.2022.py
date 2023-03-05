grades = [30,50,70,90]
names = ["James","Karim","Lora",'Jojo']

average = sum(grades)/len(grades)

for i in grades:
    if i <= average:
        name = names[grades.index(i)]
        print(name + ' is below the average with a grade of: '+str(i))
