from itertools import product
from random import randint

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from products.models import Product

from .cart import Cart
from .forms import CartAddProductForm

from pytest import Session
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('cart:detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_detail(request):
    '''
    if request.session.get('teste') is None:
        request.session['teste'] = randint(1,1000)
    
    request.session['cart'] = {
        'produto_1':{
            'nome':'Brinco',
            'preço':29.00,
            'quantidade': 3,
        },
        'produto_2':{
            'nome':'Colar',
            'preço':59.00,
            'quantidade': 1,
        },
    }
    '''
    cart = Cart(request)
    return render(request,'cart/cart_detail.html', {'cart':cart})