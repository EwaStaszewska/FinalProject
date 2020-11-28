from django.shortcuts import render,redirect
from .models import Party
from .forms import PartyForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


def main(request):
    all_party = Party.objects.all()


    # searching by form
    city_contains_query = request.GET.get('filter_by_city')
    date_query = request.GET.get('filter_by_date')
    # city_contains_query,date_query are a var in form in main.html.
    all_city_query = Party.objects.all().order_by('-date')
    all_date_query = Party.objects.all().order_by('-date')
    city_text = ''
    date_text = ''


    if request.GET.get('filter_by_city') or request.GET.get('filter_by_date'):
        if city_contains_query != "" and date_query=="":
            if city_contains_query != '' and city_contains_query is not None:
                all_city_query = all_city_query.filter(city__icontains= city_contains_query).order_by('-date')
                # all_city_query = [i for i in all_city_query if i.date >= datetime.now()].order_by('-date')
                all_date_query = []
                if len(all_city_query) == 0:
                    city_text = "Unfortunately in your city we don't have party..."

        elif date_query != '' and date_query is not None:
            if date_query != '' and date_query is not None:
                all_date_query = all_date_query.filter(date__gte = date_query)
                # all_date_query = [i for i in all_date_query if i.date >= datetime.now()].order_by('-date')
                all_city_query = []
                if len(all_date_query) == 0:
                    date_text = "Unfortunately in this date we don't have party..."

    else:
        city_text = ""
        date_text = ""
        all_date_query =[]

    
    #end searching

    context = {
        'all':all_party,
        'city_filter': all_city_query,
        'city_text':city_text,
        'date_filter': all_date_query,
        'date_text': date_text
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
