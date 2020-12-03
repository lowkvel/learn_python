from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method != 'POST':    # Display blank registration form if we are not responding to a POST request, 
                                    # that means it is a initial GET request used for retrive the initial blank registgration form
        form = UserCreationForm()
    else:                           # Process completed form if POST, the data is located in request.POST
        form = UserCreationForm(data=request.POST)

        if form.is_valid():             # if valid
            new_user = form.save()      # create the user, save the username and the hash of the password into the database
            login(request, new_user)    # log the user in after sucessful registration
            return redirect('learning_logs:index')  # redirect to the home page
    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
