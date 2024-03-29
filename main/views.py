from django.shortcuts import render, render_to_response, redirect
from django.conf import settings
from main.models import State, StateCapital, Area
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from forms import Search, CityDetails, ContactForm, AreaEditForm
from django.core.mail import send_mail


# list views
# detail views
# create views
# edit view
# delete view
# make the view --> make the URL

def home(request):
    context = {}

    return render_to_response('home.html', context, context_instance=RequestContext(request))

def api_state_list(request):

    states = State.objects.all()
    state_list = []
    api_dict = {}
    api_dict['states'] = state_list
    for state in states:
        state_list.append({'name': state.name, 'abbrev': state.abbrev, 'pk': state.pk, 'statecapital':state.statecapital.name, 'statecapital_pk':state.statecapital.pk})
    return JsonResponse(api_dict, safe=False)

def api_state_detail(request):
    name = request.GET.get('name')
    state = State.objects.get(name__iexact=name)
    return JsonResponse({'name': state.name, 'abbrev': state.abbrev, 'map':state.state_map.url, 'flag':state.flag.url}, safe=False)

def api_city_list(request):

    areas = Area.objects.all()
    area_list = []
    api_dict = {}
    api_dict['areas'] = area_list
    for area in areas:
        area_list.append({'city': area.city, 'county': area.county})
    return JsonResponse(api_dict, safe=False)

def ajax_state_list(request):
    context = {}

    return render_to_response('ajax_state_list.html', context, context_instance=RequestContext(request))

def ajax_state_detail(request, slug):
    context = {}
    context['name'] = slug
    return render_to_response('ajax_state_detail.html', context, context_instance=RequestContext(request))

def ajax_city_list(request):
    context = {}

    return render_to_response('ajax_city_list.html', context, context_instance=RequestContext(request))

def state_list(request):

    context = {}
    context['request'] = request
    temp = request.user
    context['user'] = temp
    form = Search(request.GET, "by State")
    context['form'] = form
    context['states'] = State.objects.all().order_by('name')
    print context['states']
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print username
        print password 

        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
           
    
        




    # print request.user.is_authenticated()
    # print request.user

    


    return render_to_response('state_list.html',context, context_instance=RequestContext(request))


def state_detail(request, pk):
    context = {}
    context['request'] = request
    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context,context_instance=RequestContext(request))

def state_delete(request, pk):
    context = {}
    state = State.objects.get(pk=pk)
    context['state'] = state
    context['request'] = request

    if request.method=="POST":
        for city in state.area_set.all():
            city.state = None
            city.save()
        state.delete()
        return redirect('state_list')

    return render_to_response('state_delete.html', context, context_instance=RequestContext(request))

# no longer in use. Just here for reference.
def state_search(request):
    context = {}
    context['request'] = request
    search = request.GET.get('search', None)
    # search = request.POST.get('search', None)
    if (search != None):
        states = State.objects.filter(name__icontains=search)
    else:
        states = State.objects.all()
    context['states'] = states


    return render_to_response('state_search.html', context, context_instance=RequestContext(request))


def city_search(request):
    context = {}
    context['request'] = request
    # states = State.objects.all().order_by("name")
    # context['states'] = states
    states = []
    

    if (request.method == 'POST'):
        form = Search(request.POST)
        context['form'] = form
        if (form.is_valid()):
            search = form.cleaned_data['search']
            context['search'] = search
            if (search != None):
                cities = Area.objects.filter(city__icontains=search).order_by("city")
                states = State.objects.filter(id__in=cities.values_list('state_id', flat=True))

                context['states'] = states.order_by("name")

            else:
                # cities = Area.objects.all().order_by("city")[:100]
                cities = None
                context['states'] = State.objects.all().order_by("name")
    else:
        form = Search()
        context['form'] = form
        cities = None
           

    context['cities'] = cities
    return render_to_response('city_search.html',context, context_instance=RequestContext(request))


def city_detail(request, pk):
    context = {}
    city = Area.objects.get(pk=pk)
    context['city'] = city

    return render_to_response('city_detail.html',context,context_instance=RequestContext(request))


def city_create(request, pk=None):
    context = {}
    form = CityDetails()
    
    if pk!=None:
        city = Area.objects.get(pk=pk)
        context['city'] = city
    context['form'] = form
    context['method'] = request.method
    context['states'] = State.objects.all()
    print 1
    if request.method == 'POST':
        form = CityDetails(request.POST)
        print form.errors
        if form.is_valid():       
            print 2
            zip_code = form.cleaned_data['zip_code']
            new_area, created = Area.objects.get_or_create(zip_code=zip_code)
            new_area.county = form.cleaned_data['county']
            new_area.lat = form.cleaned_data['lat']
            new_area.lon = form.cleaned_data['lon']
            new_area.city = form.cleaned_data['city']
            state_id = form.cleaned_data['state']

            print 3

            if state_id != None:
                state = State.objects.get(pk=state_id)
            else:
                state = None
            new_area.state = state
            new_area.state_abbrev = state.abbrev
            new_area.save()
            state.save()
            print 4 
            context['created'] = created
            return redirect('city_detail', pk=new_area.pk)

    elif request.method == "GET":
        pass


    return render_to_response('city_create.html', context, context_instance=RequestContext(request))



def capital_detail(request, pk):
    context = {}

    capital = StateCapital.objects.get(pk=pk)   

    context['capital'] = capital

    return render_to_response('capital_detail.html', context, context_instance=RequestContext(request))


def logout_user(request):
    context = {}
    logout(request)
    
    return render_to_response('logout.html', context, context_instance=RequestContext(request))


def capital_list(request):
    context = {} 
    context['request'] = request
    capitals = StateCapital.objects.all()
    context['capitals'] = capitals

    return render_to_response('capital_list.html', context, context_instance=RequestContext(request))


def city_delete(request, pk):
    context = {}
    
    city = Area.objects.get(pk=pk)
    context['city'] = city
    context['request'] = request

    print 1
    if (request.method =="POST"):
        city.delete()

        print 2
        return redirect('city_search')
        print 3

    return render_to_response('city_delete.html', context, context_instance=RequestContext(request))


def contact_view(request):
    context = {}

    if (request.method == "POST"):
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            send_mail("States Django: %s" % form.cleaned_data['name'], form.cleaned_data['message'], form.cleaned_data['email'], [settings.EMAIL_HOST_USER], fail_silently=False)
    else:
        form = ContactForm()
        context['form'] = form



    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):

    context = {}
    context['request'] = request
    city = Area.objects.get(pk=pk)

    form = AreaEditForm(request.POST or None, instance=city)
    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('city_detail', city.pk)

    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))

def searcher(request):
    search = request.GET.get('search', '')

    obj_qs = State.objects.filter(name__icontains=search)

    obj_list = [{'name': obj.name, 'state_pk': obj.pk, 'capital': obj.statecapital.name, 'cap_pk': obj.statecapital.pk} for obj in obj_qs]

    return JsonResponse(obj_list, safe=False)








