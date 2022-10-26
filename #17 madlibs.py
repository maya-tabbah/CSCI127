#Maya Tabbah
#maya.tabbah40@myhunter.cuny.edu
#February 3, 2022

template = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

noun = input("Enter a noun: ")
template = template.replace("NOUN", noun)

verb1 = input("Enter a verb: ")
template = template.replace("VERB1", verb1)

verb2 = input("Enter another verb: ")
template = template.replace("VERB2", verb2)

print(template)
