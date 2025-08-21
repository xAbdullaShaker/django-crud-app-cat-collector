from django.shortcuts import render
from django.http import HttpResponse


#Temp cat 

class Cat:

    def __init__(self, name, age, breed, description):
        self.name = name
        self.breed = breed
        self.age = age
        self.description = description

cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]        


# Create your views here.
def home(request):
    return render(request, 'home.html')

# main_app/views.py

def about(request):
    return render(request, 'about.html')

# views.py

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})