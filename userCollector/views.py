from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_user = form.save()
            
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'userCollector/index.html', {'form': form})
