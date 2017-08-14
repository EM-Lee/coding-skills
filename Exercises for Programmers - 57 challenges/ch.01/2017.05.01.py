while True:
    try:
        bill = float(raw_input("What is the bill? "))
        break
    except ValueError:
        print("Oops! Please enter a number. Try again.")

while True:
    try:
        tipRate = int(input("What is the tip percentage(%)? "))
        break
    except NameError:
        print("Oops! Please enter a number.")

total = bill + bill * tipRate / 100

print "The tip is " + "{:d}".format(tipRate) + "%."

# round fractions of a cent up to the next cent
print "The total is $" + "{:.0f}".format(total) + "."
    
