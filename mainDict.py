import json
import difflib

def extractDefiniton(dict,key):
    if dict.get(key.lower()) == None:
        if difflib.get_close_matches(key,dict.keys()) == []:
             return "Word doesn't exit. Double check and try again"
        else:
            response = input("Did you mean %s instead? Enter Y for yes or N for no: " % (difflib.get_close_matches(key,dict.keys())[0]))
            if(response == 'Y'):
                return dict[difflib.get_close_matches(key,dict.keys())[0]]
            else:
                return "Word doesn't exit. Double check and try again"
            

    return (dict[key.lower()])

    
dictionary = json.load(open("data.json"))
word = input("Enter word: ")
output = extractDefiniton(dictionary, word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
