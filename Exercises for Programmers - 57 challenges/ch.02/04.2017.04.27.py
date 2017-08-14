noun = raw_input("Enter a noun: ")
verb = raw_input("Enter a verb: ")
adj = raw_input("Enter an adjective: ")
adv = raw_input("Enter an adverb: ")


#print "Do you " + verb + " your " + adj + " " \
#      + noun + " " + adv + "? That's hilarious!"
print "Do you %s your %s %s %s? That's hilarious!" % (verb, adj, noun, adv)
#print("Do you {} your {} {} {}? That's hilarious!".format \
#     (verb, adj, noun, adv))
