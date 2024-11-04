from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully added.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product! Please check the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
    Edit product in the store
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated this product.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update product, Please check the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """
    View to delete a product from store
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been deleted!')
    return redirect(reverse('products'))
