from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.
    
def all_products(request):
    """ 
    A view to show all products
    """

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    select_category = None

    if request.GET:
        if 'category' in request.GET:
            category_filter = request.GET['category']
            if category_filter:
                select_category = category_filter.split(',')
                products = products.filter(category__name__in=select_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria provided. Please try a keyword")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'categories': categories,
        'select_category': select_category
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show product detail
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """
    Add product to a store
    """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)