import random
import requests

'''
Generates random quote
Params: void
Returns: String in form of {quote} : {quoteAuthor}
'''
def getQuote():
    baseURL = "http://api.forismatic.com/api/1.0/"
    numKey = random.randrange(0, 999999)
    fullURL = baseURL + "?method=getQuote&key=" + str(numKey) + "&format=text&lang=en"
    response = (requests.get(fullURL)).text
    #result = response["quoteText"] + "- " + response["quoteAuthor"]
    return response