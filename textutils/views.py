# i have created this file - ranjeet rai
from django.http import HttpResponse
from django.shortcuts import render

"""def index(request):
    return  HttpResponse('''<h1>hello ranjeet bhai</h1> <ul>
    <li><a href = "https://www.youtube.com/watch?v=bku7S72SceE"> Django CodeWithHarry</a></li>
    <li><a href = "https://www.facebook.com/">Facebook</a></li>
    <li><a href = "https://github.com/">github</a></li></ul>''')"""
def index(request):
    return  render(request, 'index.html')  

def analyze(request):
    #Get the text
    djtext = (request.POST.get('text','default'))
  
    # check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberofcharacter = request.POST.get('numberofcharacter', 'off')
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    #Check which checkbox is on
    if(removepunc == "on" ):
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuation','analyze_text':analyzed}
        #Analyze the text
        #return render(request, 'analyze.html', params)
        # return  HttpResponse("hi this is removepunc <a href = '/' > Back</a>") 
        djtext = analyzed 
      
    #Check which checkbox is on
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyze_text': analyzed}
        #Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed 

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyze_text': analyzed}
        #Analyze the text
        #return render(request, 'analyze.html', params)  
        djtext = analyzed 

    if(extraspaceremover == "on"):
        analyzed = ""    
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyze_text': analyzed}
        #Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed 

    if(numberofcharacter == "on"):
        analyze = 0
        count = 0
        for char in djtext:
            if char.isspace() != True:
                count += 1
        analyze = analyze + count
        params = {'purpose': 'Number of characters', 'analyze_text': analyze}
        #Analyze the text
        #return render(request, 'analyze.html', params)
        #djtext = analyzed 
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and numberofcharacter != "on" ):
        return HttpResponse("Please select an opration") 
    
    
    return render(request, 'analyze.html', params)

'''    else:
        return HttpResponse("Error") 

def capfirst(request):
    return  HttpResponse("hi this is capfirst <a href = '/' > Back</a>")  

def newlineremove(request):
    return  HttpResponse("Hi this is newlineremove <a href = '/' > Back</a>")  

def spaceremove(request):
    return  HttpResponse("Hi this is spaceremove <a href = '/' > Back</a>")  

def charcount(request):
    return  HttpResponse("Hi this is charcount <a href = '/' > Back</a>")  
'''
