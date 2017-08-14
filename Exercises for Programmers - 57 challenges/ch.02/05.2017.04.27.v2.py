while True:
    try:
        no1 = float(raw_input("What is the first number? "))
        if no1 < 0:
            print("Oops! The negative number is not allowed.")
            continue
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.")

while True:
    try:
        no2 = float(raw_input("What is the second number? "))
        if no2 < 0:
            print("Oops! The negative number is not allowed.")
            continue
        break
    except ValueError:
        print("Oops! That was no valid number. Try again.")

add = no1 + no2
sub = no1 - no2
multi = no1 * no2
div = no1 / no2

print ("%d + %d= %.2f") % (no1, no2, add)
print ("%d - %d = %.2f") % (no1, no2, sub)
print ("%d * %d = %.2f") % (no1, no2, multi)
print ("%d / %d = %.2f") % (no1, no2, div)
