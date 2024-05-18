from django.shortcuts import render, redirect
from store_app.models import Order, Product, Categories, Filter_Price, Color, Brand, Contact_us, OrderItem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db import IntegrityError

def BASE(request):
    return render(request, 'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status="Publish")

    context = {
        'product': product,
    }

    return render(request, 'Main/index.html',context)

def PRODUCT(request):
    
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()


    CATID = request.GET.get('categories')
    PRICE_FILTER_ID= request.GET.get('filter_price')
    BRANDID = request.GET.get('brand')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICELOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICEHIGHTOLOWID = request.GET.get('PRICE_HIGHTOLOW')
    NEWPRODUCTSID = request.GET.get('NEW_PRODUCTS')
    OLDPRODUCTSID = request.GET.get('OLD_PRODUCTS')

    if CATID:
        product = Product.objects.filter(Categories=CATID, status = "Publish" )  
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(Filter_Price=PRICE_FILTER_ID, status = "Publish")
    elif BRANDID:
        product = Product.objects.filter(Brand = BRANDID, status = "Publish" )
    elif ATOZID:
        product = Product.objects.filter(status = "Publish" ).order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status = "Publish" ).order_by('-name')
    elif PRICELOWTOHIGHID:
        product = Product.objects.filter(status = "Publish" ).order_by('price')
    elif PRICEHIGHTOLOWID:
        product = Product.objects.filter(status = "Publish" ).order_by('-price')
    elif NEWPRODUCTSID:
        product = Product.objects.filter(status = "Publish",condition='New' ).order_by('-id')
    elif OLDPRODUCTSID:
        product = Product.objects.filter(status = "Publish", condition='Old'  ).order_by('id')
    else:
        product = Product.objects.filter(status="Publish")

    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand
    }


    return render(request, 'Main/product.html',context)


def SEARCH(request):

    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains = query)
    
    context = {
        'product': product
    }



    return render(request, 'Main/search.html', context) 

def SINGLE_PRODUCT_PAGE(request, id):
    prod = Product.objects.filter(id=id).first()
    context = {
        'prod': prod,
    }
    return render(request, 'Main/single_product.html', context)

def CONTACT(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        subject = subject 
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['ahmadmugal760@gmail.com'])
            return redirect('home')
        except:
           return redirect('contact')




    return render(request, 'Main/contact_us.html')

def HandleRegister(request):
     if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('register')

     return render(request, 'Registration/auth.html')

def HandleLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'Registration/auth.html')

def HandleLogOut(request):
    logout(request)

    return redirect('home')



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')

def Check_out(request):
    return render(request, 'Cart/checkout.html')

def PLACE_ORDER(request):
    if request.method == "POST":
        try:
            uid = request.session.get('_auth_user_id')
            user = User.objects.get(id = uid)
            cart = request.session.get('cart')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            country = request.POST.get('country')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = int(request.POST.get('postcode'))
            phone = int(request.POST.get('phone'))
            email = request.POST.get('email')
            amount = request.POST.get('amount')
            # payment_id = request.POST.get('payment_id', '')  # Optional field

            order = Order(
                user=user,
                firstname=firstname,
                lastname=lastname,
                country=country,
                address=address,
                city=city,
                state=state,
                postcode=postcode,
                phone=phone,
                email=email,
                # payment_id=payment_id,
                amount=amount
            )

            order.save()
            for i in cart:
                a = (int(cart[i]['price']))
                b = cart[i]['quantity']

                total = a + b
                
                item = OrderItem(
                    order = order,
                    product = cart[i]['name'],
                    image = cart[i]['image'],
                    quantity = cart[i]['quantity'],
                    price = cart[i]['price'],
                    total = total
                )

                item.save()

        except IntegrityError as e:
           print(e)

        


    return render(request, 'Cart/placeorder.html')


def SUCCESS(request):
    return render(request, 'Cart/thankyou.html')