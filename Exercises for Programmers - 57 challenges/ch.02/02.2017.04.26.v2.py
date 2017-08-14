inStr = raw_input("What is the input string? ")
#numChar = len(inStr)

def countLetters(str):
    count = 0
    for c in str:
        count += 1
    return count

numChar = countLetters(inStr)

print inStr + " has " + str(numChar) + " characters."
