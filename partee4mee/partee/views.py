from django.shortcuts import render,redirect, get_object_or_404
from .models import Party
from .forms import PartyForm,SearchingForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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


def error_site_signed(request):
    context = {
        'message': 'Brak miejsc na imprezie, nie możesz się zapisać'
    }

    return render(request,'error_signed.html',context)

# zmienic nazwe
def party_signed_up_by_user(request, pk):
    user = request.user
    event = Party.objects.get(pk = pk)

    if user not in event.signed_users.all():
        if event.free_space > 0: 
            event.signed_users.add(user)
            event.free_space -= 1
            event.save()
        else:
            print("Full space")
            return redirect(error_site_signed)

            # stworzyc nowy widok na blad jak nie ma miejsc + kolor buttona uzaleznic od ilosci miejsc
    else: 
        print("You were signed up to event")
        return redirect(user_signed_up_events)




    # context={
    #     'signed_up_events' : user.signed_event.all(),
    # }

    return redirect(user_signed_up_events)
    # return redirect()


def user_signed_up_events(request):
    user = request.user
    context={
        'signed_up_events' : user.signed_event.all(),
    }

    return render(request, 'signed_up_events.html', context)


# events edit logic
def edit_event(request, id):
    event = get_object_or_404(Party, pk=id, author=request.user)
    form = PartyForm(request.POST or None, instance=event)


    if form.is_valid():
        form.save()
        return redirect(user_signed_up_events)

    return render(request, 'edit_event.html', {"form": form})
