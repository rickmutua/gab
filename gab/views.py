from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response
from gab.models import Category, Box, Product
from .forms import OrderForm

from cart.cart import Cart

# Create your views here.


def index(request):

    return render(request, 'index.html')


def categories(request):

    categories = Category.objects.all()

    return render(request, 'category/categories.html', {'categories': categories})


def single_category(request, category_id, category_slug):

    category = Category.single_category(category_id, category_slug)

    boxes = Box.objects.filter(category=category_id).all()

    return render(request, 'category/single-category.html', {'category': category, 'boxes': boxes})


def box(request, box_id, box_slug):

    box = Box.single_box(box_id, box_slug).order_by('-id')

    products = Product.objects.filter(box=box_id).order_by('-id')

    return render(request, 'category/box.html', {'box': box, 'products': products})


def add_to_cart(request, box_id, box_slug):

    try:

        cart = Cart(request)

        box = Box.objects.get(id=box_id, slug=box_slug)

        cart.add(box, box.price)

        return redirect('box', box_id, box_slug)

    except Exception as exception:

        raise exception


def remove_from_cart(request, box_id, box_slug):

    try:

        cart = Cart(request)

        box = Box.objects.get(id=box_id, slug=box_slug)

        cart.remove(box)

        return redirect('box', box_id, box_slug)

    except Exception as exception:

        raise exception


def display_cart(request):

    return render_to_response('cart.html', dict(cart=Cart(request)))


def checkout(request):

    try:

        cart = Cart(request)

        if request.method == 'POST':

            form = OrderForm(request.POST)

            if form.is_valid():

                order = form.save(commit=False)

                order.user = request.user

                order.save()

                return redirect(index)

            else:

                form = OrderForm()

                return render_to_response('checkout.html', dict(cart=Cart(request)), {'cart': cart, 'form': form})

        else:

            form = OrderForm()

            return render_to_response('checkout.html', dict(cart=Cart(request)), {'cart': cart, 'form': form})

    except Exception as exception:

        raise exception

