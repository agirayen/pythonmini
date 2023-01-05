from spellchecker import SpellChecker

dictionary =SpellChecker()

word = input("ENter your word :")
if word in dictionary:
    print("Correct spelling")

else:
    correct_word= dictionary.correction(word)
    print("Correct spelling is : ",correct_word)

