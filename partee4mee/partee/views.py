from django.shortcuts import render
from .models import Party
from .forms import PartyForm

def main(request):
    all_paty = Party.objects.all()
    return render(request, "main.html", {'all':all_paty})


def add(requset):
    form = PartyForm(requset.POST or None)

    if form.is_valid():
        form.save()

    return render(requset, 'add_party.html', {"form":form}) 
