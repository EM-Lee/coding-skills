from datetime import datetime

age = int(raw_input("What is your current age? "))
while True:
    try:
        reAge = int(raw_input("At what age would you like to retire? "))
        if reAge < age:
            print("Oops! You could already retire.")
            continue
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.")
       
toRe = reAge - age
thisYear = datetime.now().year #datetime.now().month/day/hour/minute/second
reYear = thisYear + toRe

print ("You have %d years left until you can retire.") % (toRe)
print ("It's %d, so you can retire in %d.") % (thisYear, reYear)
