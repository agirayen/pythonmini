from difflib import SequenceMatcher

text1 = "My name is Teddy bear,I like to eat kisses"
text2 = "My name is goldfish,I love to eat cheese"

findmatch = SequenceMatcher(None,text1,text2).ratio()

print(f"Both texts are {findmatch * 100} % match")

t1 = "hello"
t2 = "hello"
findma = SequenceMatcher(None,t1,t2).ratio()

print(f"Both {findma *100} % matches")
