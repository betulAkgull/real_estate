from django.shortcuts import redirect, render
from .models import Listing
from .forms import ListingForm
from django.contrib import messages

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listings_retrieve(request, pk):
    listing = Listing.objects.get(id = pk)
    context = {
        "listing": listing
    }
    return render(request,"listing.html", context)

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing saved successfully!")
            return redirect("/")
        else:
            messages.error(request, "Something got wrong, try again.")
            print(form.errors)
    else:
        form = ListingForm()
    
    context = {
        "form":form
    }
    return render(request, "listing_create.html",context)


def listing_update(request,pk):
    listing = Listing.objects.get(id = pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance= listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing saved successfully!")
            return redirect('/', pk=listing.pk)
        else:
            messages.error(request, "Something got wrong, try again.")
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, "listing_update.html",context)


def listing_delete(request,pk):
    listing = Listing.objects.get(id = pk)
    if request.method == 'POST':
        listing.delete()
        messages.success(request, "Listing deleted successfully!")
        return redirect('/')
    else:
        return redirect('listing.html', pk=pk) 
    