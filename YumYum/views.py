from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import book, Dessert, Gelato, Mocktail, Shake, Starter, Indian, Chinese, American, Cart
from django.contrib import messages
from .forms import ReviewForm
import json

def index(request):
    return render(request, "index.html")

def starters(request):
    starters = Starter.objects.all()
    return render(request, "categories/starters.html", {'starters': starters})

def maincourse(request):
    return render(request, "categories/maincourse.html")

def desserts(request):
    desserts = Dessert.objects.all()
    return render(request, 'categories/desserts.html', {'desserts': desserts})

def gelatos(request):
    gelatos = Gelato.objects.all()
    return render(request, 'categories/gelatos.html', {'gelatos': gelatos})

def mocktails(request):
    mocktails = Mocktail.objects.all()
    return render(request, 'categories/mocktails.html', {'mocktails': mocktails})

def shakes(request):
    shakes = Shake.objects.all()
    return render(request, 'categories/shakes.html', {'shakes': shakes})

def indian(request):
    indian = Indian.objects.all()
    return render(request, 'categories/indian_cuisine.html', {'indian': indian})

def chinese(request):
    chinese = Chinese.objects.all()
    return render(request, 'categories/chinese.html', {'chinese': chinese})

def american(request):
    american = American.objects.all()
    return render(request, 'categories/american.html', {'american': american})

def booking(request):
    mydata = book.objects.all()
    if mydata:
        return render(request, "booking.html", {"book": mydata})
    else:
        return render(request, "booking.html")

def bookingdata(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        date = request.POST["date"]
        time = request.POST["time"]
        address1 = request.POST["address1"]
        count = request.POST["count"]
        request1 = request.POST["SplRequest"]

        if book.objects.filter(Date=date, Time=time).exists():
            messages.error(request, "Sorry this table isn't available")
            return redirect("booking")  
        
        obj = book(
            Name=name,
            Age=age,
            Gender=gender,
            Phone=phone,
            Email=email,
            Date=date,
            Time=time,
            Address1=address1,
            Count=count,
            Request=request1,
        )
        obj.save()
        messages.success(request, "Your table has been successfully booked!")
        return redirect("booking")

    return render(request, "booking.html")

def check_availability(request):
    date = request.GET.get('date')
    time = request.GET.get('time')

    is_booked = book.objects.filter(Date=date, Time=time).exists()
    return JsonResponse({'is_booked': is_booked})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            
            return JsonResponse({'success': True, 'message': 'Thank you for your review!'})
        else:
            
            return JsonResponse({'success': False, 'errors': form.errors})
    
def update_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        starter_id = data.get('starter_id')
        quantity = data.get('quantity')

        if starter_id and quantity is not None:
            starter = Starter.objects.get(id=starter_id)
            user = request.user

            cart_item, created = Cart.objects.get_or_create(user=user, starter=starter)

            if quantity > 0:
                cart_item.update_quantity(quantity)
                message = 'Cart updated successfully!'
            else:
                cart_item.delete() 
                message = 'Item removed from cart!'

            return JsonResponse({'success': True, 'message': message})

        return JsonResponse({'success': False, 'message': 'Invalid data'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})