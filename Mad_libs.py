# Mad Libs
# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file. For example, a text file may look like this:
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events

ADJECTIVE = input('ADJECTIVE ')
NOUN = input('NOUN ')
VERB = input('VERB ')
NOUN_2 = input('NOUN_2 ')

msg = f'''
The {ADJECTIVE} panda walked to the {NOUN} and then {VERB}.
 A nearby {NOUN_2} was unaffected by these events'''

work = open("Myfile.txt", "w")
work.write(msg)
print(work.write(msg))
work.close()
