from django.core.paginator import Paginator
from django.shortcuts import render

from main_app.models import Product, Category


def home(request):
    return render(request, 'home.html')


def contact_us_page(request):
    return render(request, 'contact_us_page.html')


def categories_list(request):
    p = Paginator(Category.objects.all().order_by('id'), 6)
    page = request.GET.get('page')
    categories = p.get_page(page)

    context = {
        'categories': categories,
    }
    return render(request, 'categories_list.html', context)


def products_list(request, category_id):
    p = Paginator(Product.objects.filter(category_id=category_id).order_by('id'), 1)
    page = request.GET.get('page')
    products = p.get_page(page)

    context = {
        'products': products,
        'range': range(9),
        'category': Category.objects.get(id=category_id),
    }
    return render(request, 'product_list.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        p = Paginator(Product.objects.filter(name__contains=searched).order_by('id'), 1)
        page = request.GET.get('page')
        products = p.get_page(page)

        context = {'searched': searched,
                   'products': products}
        return render(request, 'searched.html', context)

    else:
        context = {
            'products': []
        }
        return render(request, 'searched.html', context)