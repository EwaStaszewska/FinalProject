from django.shortcuts import render
from .models import Party
from .forms import PartyForm

def main(request):
    all_paty = Party.objects.all()


    # searching by form
    city_contains_query = request.GET.get('filter_by_city')
    # city_contains_query is a var in form in main.html.
    all_city_query = Party.objects.all() 

    if city_contains_query != '' and city_contains_query is not None:
        all_city_query = all_city_query.filter(city__icontains= city_contains_query)
    
    #end searching


    # for our knowledge: 
    # party_filter = Party.objects.filter(date__startswith ='2020-11-22') 
    # startswith, because we've in db datetimefield. I suppose it'll be useful in our next_steps
    context = {
        'all':all_paty,
        'city_filter': all_city_query
        # 'filter_party': party_filter,
    }

    return render(request, "main.html",context)


def add(requset):
    form = PartyForm(requset.POST or None)

    if form.is_valid():
        form.save()

    return render(requset, 'add_party.html', {"form":form}) 
