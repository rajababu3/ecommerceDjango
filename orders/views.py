import time

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
from .models import Order
from users.forms import UserAddressForm

@login_required()
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = str(time.time())
        new_order.save()


    except:
        new_order = None
        return HttpResponseRedirect(reverse("cart"))

    address_form = UserAddressForm(request.POST or None)
    if address_form.is_valid():
        new_address = address_form.save(commit=False)
        new_address.user = request.user
        new_address.save()

    if new_order.status == "Started":
        new_order.status = "Finished"
        new_order.save()

    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("success"))

    context = {
        "address_form": address_form
    }
    template = "orders/success.html"
    return render(request, template, context)

def success(request):
    context = {}
    template = "orders/success.html"
    return render(request, template, context)