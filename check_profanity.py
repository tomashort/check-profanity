from urllib import request, parse

def read_text():
    quotes = open(
        r"C:\Users\Tom\Documents\Code\Udacity\Python\check_profanity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = f"http://www.wdylike.appspot.com/?q={parse.quote(text_to_check)}"
    response = request.urlopen(url)
    output = response.read().decode()
    response.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
