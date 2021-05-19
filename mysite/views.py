#I have created this file-Amrit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def bootuses(request):
    return render(request,'bootuses.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    puncremover=request.POST.get('puncremover','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if puncremover=='on':
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
            else:
                pass

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext=analyzed
        
        
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                 analyzed=analyzed+char
            
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        djtext=analyzed
        
    if(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
            
        params={'purpose':'Remove extra space','analyzed_text':analyzed}
        djtext=analyzed
        

    if(charcount=='on'):
        analyzed=len(djtext)
        params={'purpose':'Count character','analyzed_text':analyzed}
        

    if(puncremover != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)



