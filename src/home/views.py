from platform import system
from django.shortcuts import render

def index(request):
    return render(request, "index.html", {
        "data": [
            "Nazrep project",
            system()
        ]
    })