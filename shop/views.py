from collections import OrderedDict

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin  # for social_django
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from blog.forms import ProfileEditForm
from .forms import CommentForm
from blog.models import Profile
from django.urls import reverse
from django.views.generic import TemplateView  # for social_django

from .models import product, Orders, Contact, OrderCome, Comment, OrderReceived
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from math import ceil
import json

from django.template.loader import render_to_string
# for email
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    # products = product.objects.all()
    # n=len(products)
    # nSlides=n//4 + ceil((n/4)-(n//4))
    # params={'no of slides':nSlides,'range':range(1,nSlides),'product':products}
    #  allProds =[[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

    allProds = []  # here objects is a model manager
    catProds = product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    print(params)
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    '''return True only if query matches item'''
    if query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}

    for cat in cats:
        prodtemp = product.objects.filter(category=cat)

        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds, "msg": ""}
    print(params)
    if len(allProds) == 0 or len(query) < 4:
        params = {"msg": "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def basic(request):
    return render(request, 'shop/basic.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('inputName', '')
        email = request.POST.get('inputEmail', '')
        phone = request.POST.get('inputPhone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)

        if len(phone) < 10 or len(desc) < 50 or len(email) < 5:
            messages.error(request, 'INVALID CREDENTIALS, PLEASE TRY AGAIN')
        else:
            messages.success(request, 'SUCCESSFULLY PLACED')
            contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderID', '')
        email = request.POST.get('inputEmail', '')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderCome.objects.filter(order_id=orderid)
                updates = []
                for item in order:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})

                response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json},
                                      default=str)
                # If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def productview(request, myid):
    # fetch the product using the id
    products = product.objects.filter(id=myid)

    post = get_object_or_404(product, id=myid)

    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(post.get_absolute_url())if using ajax comment this line
        # At very first time when url calls Post_detail else part just initialize the form object
    else:
        comment_form = CommentForm()
    context = {
        'products': products[0],

        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),

        'comments': comments,
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('shop/comments.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request, 'shop/productview.html', context)


def likePost(request):
    post = get_object_or_404(product, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('shop/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    # return HttpResponseRedirect(post.get_absolute_url())


def checkout(request):
    if request.method == "POST":
        # inputName is  ID in from
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        totalproducts = request.POST.get('total_products', '')
        name = request.POST.get('inputName', '')
        email = request.POST.get('inputEmail', '')
        address = request.POST.get('inputAddress', '')
        phone = request.POST.get('inputPhone', '')
        city = request.POST.get('inputCity', '')
        state = request.POST.get('inputState', '')
        zip_code = request.POST.get('inputZip', '')

        if request.user.is_authenticated:
            parsed = json.loads(items_json)
            dictobj = OrderedDict(parsed)
            final_str = ""
            counter = 0
            for obj in dictobj:
                print(obj, "--", dictobj[obj])
                # liststr = (str(dictobj[obj][1])).join((str(dictobj[obj][2] )))
                counter += 1
                liststr = f"({counter})   {str(dictobj[obj][0])}  {str(dictobj[obj][1])}                 {str(dictobj[obj][2])}"
                final_str += liststr
                final_str += "\n"

            # for sending email to customer
            subject = "Thank you for your order from EBuyZone"
            message = "Wellcome to EBuyZone.\n #   QTY PRODUCT NAME                        PRICE \n" + final_str + f"\nYou order total {totalproducts} products.\n Your total bill is {amount} Rs\n"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]

            order = Orders(items_details=message, items_json=items_json, name=name, email=email, address=address,
                           phone=phone, city=city,
                           state=state, zip_code=zip_code, amount=amount, update_desc="Order Placed")
            order.save()

            received = OrderReceived(order_id=order.order_id, name=order.name, address=order.address,
                                     items_details=message, amount=order.amount)
            received.save()

            id = order.order_id
            message += f"\nYour order id is {id} . Use it to track your order using our order tracker."
            thanks = True
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return render(request, 'shop/thanks.html', {'thanks': thanks, 'id': id, 'items_json': items_json})
        else:
            messages.error(request, 'YOU ARE NOT LOGGED IN')

    return render(request, 'shop/checkout.html')


def thanks(request):
    return render(request, 'shop/thanks.html')


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        user = User.objects.filter(username=username)
        emailExist = User.objects.filter(email=email)
        # Check for errorneous inputs
        # username should be under 18 characters
        if user:
            messages.error(request, 'USER ALREADY EXISTS')
            return redirect('shophome')
        if emailExist:
            messages.error(request, 'EMAIL ALREADY EXISTS')
            return redirect('shophome')

        if len(username) > 18:
            messages.error(request, 'USERNAME MUST BE UNDER 18 CHARACTERS')
            return redirect('shophome')
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, 'USERNAME SHOULD ONLY CONTAIN LETTERS AND NUMBERS')
            return redirect('shophome')
        # passwords should match
        if pass1 != pass2:
            messages.error(request, 'PASSWORDS DO NOT MATCH')
            return redirect('shophome')

        # Create the user
        myUser = User.objects.create_user(username, email, pass2)
        myUser.first_name = fname.title()  # capitalize each word first letter
        myUser.last_name = lname.title()
        myUser.save()
        Profile.objects.create(user=myUser)
        messages.success(request, 'YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED')
        return redirect('shophome')
    else:
        return HttpResponse('404 - NOT FOUND')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginUsername = request.POST['loginUsername']
        loginPass = request.POST['loginPass']
        user = authenticate(username=loginUsername, password=loginPass)
        if user is not None:
            login(request, user)
            messages.success(request, 'SUCCESSFULLY LOGED IN')
            return redirect('shophome')
        else:
            messages.error(request, 'INVALID CREDENTIALS, PLEASE TRY AGAIN')
            return redirect('shophome')

    return HttpResponse('404 - NOT FOUND')


def handleLogout(request):
    logout(request)
    messages.success(request, 'SUCCESSFULLY LOGED OUT')
    return redirect('shophome')
