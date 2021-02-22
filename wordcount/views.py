from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionary={}       # here i am today right here
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedtext=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'countingwords':len(wordlist),'worddictionary':sortedtext})
def about(request):
    return render(request,'about.html')