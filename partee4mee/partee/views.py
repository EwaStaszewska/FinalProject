from django.shortcuts import render,redirect
from .models import Party
from .forms import PartyForm,SearchingForm
from datetime import datetime
from django.contrib.auth.decorators import login_required



def main(request):
    form = SearchingForm(request.GET)
    total_advertisement = Party.objects.all()
    all_party = Party.objects.all().order_by('date')
    # searching by form
    city = request.GET.get('city',False)
    date = request.GET.get('date',False)
    bfield = request.GET.get('bolean_field',False)
    # city_contains_query,date_query are a var in form in main.html.

    if city and not date:
        all_party = all_party.filter(city__icontains=city).order_by('date')
    if city and date:
        all_party = all_party.filter(city__icontains=city).filter(date__gte=date).order_by('date')
    if city and date and bfield:
        all_party = all_party.filter(city__icontains=city).filter(date__icontains=date).order_by('date')
    if date and bfield:
        all_party = all_party.filter(date__icontains=date).order_by('date')
    if date and not bfield:
        all_party = all_party.filter(date__gt=date).order_by('date')
    

    context = {
        'all':all_party,
        'total':total_advertisement,
        'form':form

    }

    return render(request, "main.html",context)



# requirements to add form: only for logged in users.
@login_required
def add(request):
    form = PartyForm(request.POST or None)
    
    if form.is_valid():
        temporary_form = form.save(commit=False)
        temporary_form.author = request.user
        temporary_form.save()
        return redirect(main)

    return render(request, 'add_party.html', {"form":form}) 


@login_required
def your_account(request):
    user_party_advert = Party.objects.filter(author= request.user)
    user = request.user
    context={
        'user':user,
        'user_party_advert' : user_party_advert,


    }
    return render(request,'accounts.html',context)