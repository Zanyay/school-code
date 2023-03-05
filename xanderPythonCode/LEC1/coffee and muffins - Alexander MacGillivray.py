#write a program that asks you how many coffees you want
#and how many

print("prices: coffee is 2$, muffins are 4$")
print("How many coffees would you like? : ")
coffee = input()
print("How many muffins would you like? : ")
muffin = input()
muffin = int(muffin) * 4
coffee = int(coffee) * 2
total = coffee + muffin
print("your total will be: " + str(total) + "$")
