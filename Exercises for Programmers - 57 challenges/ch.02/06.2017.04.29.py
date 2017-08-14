age = raw_input("What is your current age? ")
reAge = raw_input("At what age would you like to retire? ")

toRe = int(reAge) - int(age)
thisYear = 2017
reYear = 2017 + toRe

print ("You have %d years left until you can retire.") % (toRe)
print ("It's %d, so you can retire in %d.") % (thisYear, reYear)
