bill = float(input("What is the bill? "))
tipRate = int(input("What is the tip percentage? "))

total = bill + bill * tipRate / 100

print "The tip is " + "{:d}".format(tipRate) + "%."
print "The total is $" + "{:.2f}".format(total) + "."
