from django.shortcuts import render, redirect
from users.models import Claim, Main, Inpatient_limit, Outpatient_limit, Preauthorisation, Caps_benefits
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.paginator import Paginator


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect after succesful login
                return redirect('dashboard/')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# main info view
def dashboard_view(request):
    maindata = None
    if request.GET:
        memberID = request.GET.get('memberID')  # Using get() method to avoid KeyError
        # print(memberID)
        try:
            maindata = Main.objects.get(membernumber=memberID)
        except Main.DoesNotExist:
            messages.error(request, "Membership number does not exist.")
    return render(request, 'dashboard.html', {'maindata': maindata})



# claims view 
from django.core.paginator import Paginator

def claims_view(request):
    memberID = None
    claimdata = None
    name = None
    page_obj = None

    if request.GET:
        memberID = request.GET.get('memberID')
        page = request.GET.get('page')
        claimdata = Claim.objects.filter(membernumber=memberID)
        paginator = Paginator(claimdata, 6)
        page_obj = paginator.get_page(page)
        if claimdata.exists():  # Check if claimdata exists before attempting pagination
            maindata = Main.objects.get(membernumber=memberID)
            name = f"{(maindata.firstname).title()} {(maindata.lastname).title()}"
        else:
            messages.error(request, "No data found for your entry.")
    return render(request, 'claims.html', {'page_obj': page_obj, 'name': name, 'memberID':memberID})




# inpatient data view
def inpatient_view(request):
    memberID = None
    inpatientdata = None
    name = None

    if request.GET:
        memberID = request.GET.get('memberID')
        inpatientdata = Inpatient_limit.objects.filter(membernumber=memberID)
        if inpatientdata:
            maindata = Main.objects.get(membernumber=memberID) # Fetching the member object from main data in order to get access to name of the ID holder
            name = f"{(maindata.firstname).title()} {(maindata.lastname).title()}"  # Extract name
        else:
            messages.error(request, "No data found for your entry.")
    return render(request, 'inpatient.html', {'inpatientdata': inpatientdata,'name': name, 'memberID':memberID})


def outpatient_view(request):
    memberID = None
    outpatientdata = None
    name = None

    if request.GET:
        memberID = request.GET.get('memberID')
        outpatientdata = Outpatient_limit.objects.filter(membernumber=memberID)
        if outpatientdata:
            maindata = Main.objects.get(membernumber=memberID) 
            name = f"{(maindata.firstname).title()} {(maindata.lastname).title()}"
        else:
            messages.error(request, "No data found for your entry.")
    return render(request, 'outpatient.html', {'outpatientdata': outpatientdata,'name': name, 'memberID':memberID})


def preauthorisation_view(request):
    memberID = None
    preauthorisationdata = None
    name = None

    if request.GET:
        memberID = request.GET.get('memberID')
        preauthorisationdata = Preauthorisation.objects.filter(membernumber=memberID)
        if preauthorisationdata:
            maindata = Main.objects.get(membernumber=memberID) 
            name = f"{(maindata.firstname).title()} {(maindata.lastname).title()}"
        else:
            messages.error(request, "No data found for your entry.")
    return render(request, 'preauthorisation.html', {'preauthorisationdata': preauthorisationdata,'name': name, 'memberID':memberID})


def capsbenefits_view(request):
    capsbenefitsdata = Caps_benefits.objects.all()
    return render(request, 'capsbenefits.html', {'capsbenefitsdata': capsbenefitsdata})



# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


def logout_view(request):
    logout(request)
    return redirect('login')





