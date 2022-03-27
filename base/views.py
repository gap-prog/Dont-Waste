# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Listing
from .forms import RegisterForm, ListingsForm


def home(request):
	listings = Listing.objects.filter(claim="False")
	listings_count = listings.count()
	context = {
		'listings_count': listings_count,
		"listings": listings
	}
	return render(request, 'base/home.html', context)


def loginPage(request):
	page = "login"
	if request.user.is_authenticated:
		return redirect("home")
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exist')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return redirect('login')
	context = {'page': page}
	return render(request, 'base/login_register.html', context)
	
def logoutUser(request):
	logout(request)
	return redirect('home')


def registerPage(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			login(request, user)
			messages.error("There was an error in the registration process.")
			return redirect('home')
		else:
			return redirect('register')
	return render(request, 'base/login_register.html', {'form': form})


def listing(request, pk):
	listings = Listing.objects.get(id=pk)
	page = "listing"
	context = {
		'page': page,
        'listing': listings,
    }
	return render(request, 'base/listing.html', context)


@login_required(login_url='login')
def createListing(request):
	form = ListingsForm()
	if request.method == "POST":
		form = ListingsForm(request.POST)
		if form.is_valid():
			listing = form.save(commit=False)
			listing.lister = request.user
			listing.save()
			return redirect("home")
	context = {"form": form}
	return render(request, "base/listing_form.html", context)


def updateListing(request, pk):
	listings = Listing.objects.get(id=pk)
	form = ListingsForm(instance=listings)
	if request.user != listings.lister:
		return HttpResponse("You did not create this listing.")
	if request.method == "POST":
		form = ListingsForm(request.POST, instance=listings)
		if form.is_valid():
			form.save()
			return redirect("home")
	context = {
		"form": form,
		'page': 'update'
	}
	return render(request, "base/listing_form.html", context)


def deleteListing(request, pk):
	listing = Listing.objects.get(id=pk)
	if request.user != listing.lister:
		return HttpResponse("You did not create this listing.")
	if request.method == "POST":
		listing.delete()
		return redirect("home")
	return render(request, 'base/delete.html', {'listing': listing})

def claim(request, pk):
	listing = Listing.objects.get(id=pk)
	if request.user == listing.lister:
		return redirect('home')
	else:
		if request.method == "POST":
			listing.claim = "True"
			listing.save()
			return redirect("home")
	return render(request, 'base/claim.html', {'listing': listing})
