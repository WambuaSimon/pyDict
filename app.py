import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " %get_close_matches(w, data.keys())[0])
        if yn=="Y" or yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N" or yn == "n":
            return "The Word Doesn't exist"
        else:
            return "We didn't understand your query"
        
    else:
        return "The Word doesn't exist!"

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        

print(translate(word))