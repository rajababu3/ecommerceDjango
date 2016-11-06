import time
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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
        # return HttpResponseRedirect("/cart/")
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
        # work on some error message
        return HttpResponseRedirect(reverse("cart"))
    final_amount = 0
    if new_order is not None:
        new_order.sub_total = cart.total
        new_order.save()
        final_amount = new_order.get_final_amount()

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
@login_required()
def success(request):
    context = {}
    template = "orders/success.html"
    return render(request, template, context)

@login_required()
def user_order(request, user):
    orders = Order.objects.filter(user = user)
    context = {"orders": orders}
    template = "orders/userOrder.html"
    return render(request, template, context)