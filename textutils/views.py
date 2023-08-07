from django.http import HttpResponse
from django.shortcuts import render

'''render() function takes three arguments:

request: It is the argument that is required to serve the input request.
Name of the template file: The name of the template which we want to use. Here, we have passed "index.html."
Name of the dictionary: We can also pass a dictionary containing variables to the template if we want. and use it using {{}} in html'''

'''
Key points about GET requests:

Used to retrieve data from the server.
Data is sent in the URL as query parameters.
Limited amount of data can be sent in a GET request.


Key points about post requests: 

Used to send data to the server for processing or creation.
Data is sent in the request body.
There is no limitation on the amount of data that can be sent with a POST request.
POST requests are not cached by default, making them suitable for operations that should not be repeated automatically.


'''
# def index(request):
#     return HttpResponse("<h1>hello harry bhai<h1> <a href=https://www.youtube.com/>Go to youtube </a>")  # html prop
# def about(request):
#     return HttpResponse("<h3>About our hero<h3>")
def rasen(request):
    return render(request,'rasen.html')

def analyze(request):
    # TO ACCESS THE TEXT IN TEMPLATE AND DISPLAY IT IN COMMAND LINE
    # i.e. POST THE TEXT
    # djtext=(request.GET.get('text','default'))
    djtext=(request.POST.get('text','default'))
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    removeextraspace=request.POST.get('removeextraspace','off')
    # ANALYSE THE TEXT
    analyzed=""
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed=djtext.upper()
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed=djtext.replace("\n"," ").replace("\r"," ")
        djtext=analyzed

    if(removeextraspace=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index-1]== " ":
                pass
            else:
                analyzed+=char
        djtext=analyzed
        
    params = {'purpose': 'SUITABILITY', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
def navbar(request):
    return render(request,'nav.html')

# def direct(request):
#     return HttpResponse("<a href='/'>back</a>")  # rat le