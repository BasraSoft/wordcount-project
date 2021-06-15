from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def count(request):
    fulltext= request.GET['fulltext']
    wordlist = fulltext.split()
    worddic={}
    for word in wordlist:
        if word in worddic:
            worddic[word] +=1
        else:
            worddic[word]=1
    
    sortedword=sorted(worddic.items(), key=operator.itemgetter(1), reverse=False)

    return render(request, 'count.html',{'fulltext':fulltext, 'counts': len(wordlist), 'sortedword':worddic.items(),})

def about(request):
    return render(request, 'about.html')
