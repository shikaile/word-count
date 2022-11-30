from django.http import HttpResponse
from django.shortcuts import render

# home funcion for requesting home page
def home(req):
    return render(req, 'index.html')

def count(req):
    fulltext = req.GET ['fulltext']
    wordlist = fulltext.split()

    return render(req, 'count.html', {'fulltext':fulltext, 'count':len(wordlist)})

