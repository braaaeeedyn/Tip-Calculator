print("Welcome to the tip calculator.")
cost = float(input("What was the cost of the meal?\n $"))
people = float(input("How many people is the bill split with?\n"))
percent = float(input("In a whole number, what percent tip are we giving?\n"))
percentfull = 1.0 + percent / 100.0

costperperson = float((cost / people * percentfull))
costrounded = round(costperperson,3)
costroundedwith0 = "{:.2f}".format(costperperson)
print("$"+ costroundedwith0)
