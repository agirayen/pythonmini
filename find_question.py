from nltk.tokenize import word_tokenize

question_words = ["what","where","when","whom","are","why","could","can","may","have","has","which","is","do","don't"]

question = input("Enter your Question : ")
question = question.lower()

question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print("It's Question")
else:
    print("Not a Question")
