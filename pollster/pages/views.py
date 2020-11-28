from django.shortcuts import render

# Create index views

def index(request) :
    return render(request, 'pages/index.html')
