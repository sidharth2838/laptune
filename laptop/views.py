from django.shortcuts import redirect,get_object_or_404, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Laptop, Customization, Review, Purchase
from .forms import PurchaseForm, ReviewForm  # Ensure these forms exist
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect

# Home view
def home(request):
    # laptops = Laptop.objects.all()
    return render(request, 'laptop/home.html')

# Customize view
def customize(request, laptop_id):
    laptop = get_object_or_404(Laptop, pk=laptop_id)
    customizations = Customization.objects.filter(laptop=laptop)
    return render(request, 'laptop/customize.html', {'laptop': laptop,})

# Purchase view
def purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            payment_method = form.cleaned_data['payment_method']
            
            # Handle purchase logic here
            Purchase.objects.create(
                name=name,
                email=email,
                payment_method=payment_method
            )
            
            # Create the URL with query parameters
            query_string = urlencode({'name': name, 'email': email})
            url = f"{reverse('purchase_confirmation')}?{query_string}"
            
            # Redirect to the confirmation page with the query string
            return HttpResponseRedirect(url)
        else:
            # Handle form errors
            return render(request, 'laptop/purchase.html', {'form': form, 'error': 'Please correct the errors below'})
    else:
        form = PurchaseForm()

    return render(request, 'laptop/purchase.html', {'form': form})

# Review view with pagination
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'laptop/review.html', {'reviews': reviews, 'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirect to the customize page for a specific laptop after login
            laptop_id = request.POST.get('laptop_id', 1)  # You can change this to a dynamic value or pass it as a parameter
            return redirect('customize', laptop_id=laptop_id)
        else:
            return render(request, 'laptop/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'laptop/login.html', {'form': form})

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'laptop/register.html', {'form': form})

# Purchase confirmation view
def purchase_confirmation(request):
    name = request.GET.get('name', 'Guest')
    email = request.GET.get('email', 'No email provided')
    return render(request, 'laptop/purchase_confirmation.html', {'name': name, 'email': email})


def reviews_page(request):
    reviews = Review.objects.all()
    return render(request, 'review_page.html', {'reviews': reviews})

def example_view(request):
    if request.method == 'POST':
        # Handle POST data
        pass
    return render(request, 'example_template.html')