from maxim_pkg import Sentence


First_noun = input("Please enter a noun------ ")
cap1 = First_noun.upper()
print("---", cap1, '---\n')

Second_noun = input("Please enter another noun------ ")
cap2 = Second_noun.upper()
print("---", cap2, '---\n')

Third_noun = input("please enter another noun------ ")
cap3 = Third_noun.upper()
print("---", cap3, '---\n')

First_pronoun = input("please enter a pronoun------ ")
cap4 = First_pronoun.upper()
print("---", cap4, '---\n')

Fourth_noun = input("Please enter another noun----- ")
cap5 = Fourth_noun.upper()
print("---", cap5, '---\n')

Fifth_noun = input("Please enter another noun----- ")
cap6 = Fifth_noun.upper()
print("---", cap6, '---\n')

Sixth_noun = input("Please enter another noun----- ")
cap7 = Sixth_noun.upper()
print("---", cap7, '---\n')

First_verb = input("Please enter another verb----- ")
cap8 = First_verb.upper()
print("---", cap8, '---\n')

Seventh_noun = input("Please enter another noun----- ")
cap9 = Seventh_noun.upper()
print("---", cap9, '---\n')

Eight_noun = input("Please enter another noun----- ")
cap10 = Eight_noun.upper()
print("---", cap10, '---\n')

Ninth_noun = input("Please enter another noun----- ")
cap11 = Ninth_noun.upper()
print("---", cap11, '---\n')


print(Sentence.fullStory(cap1, cap2, cap3, cap4, cap5, cap6, cap7,
                         cap8, cap9, cap10, cap11))
