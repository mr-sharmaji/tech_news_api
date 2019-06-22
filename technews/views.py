from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("https://newsapi.org/v2/everything?sources=techradar&apiKey=96cc98dbabea497b921dcd946f249e78")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api})

def search(request):

    if request.method == 'POST':
        import requests
        import json
        lookups = request.POST.get('lookup')
        lookup_request = requests.get("https://newsapi.org/v2/everything?sources=techradar&apiKey=96cc98dbabea497b921dcd946f249e78")
        update = json.loads(lookup_request.content)
        return render(request,'search.html',{'lookup':lookups,'update':update})
    else:
        messages.error(request, 'Not Found')
        return render(request,'search.html')
