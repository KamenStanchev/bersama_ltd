from django.core.paginator import Paginator
from django.shortcuts import render

from main_app.models import Product, Category, Manufacture, Campaign


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


def manufactures_list(request):
    p = Paginator(Manufacture.objects.all().order_by('id'), 6)
    page = request.GET.get('page')
    manufactures = p.get_page(page)

    context = {
        'manufactures': manufactures,
    }
    return render(request, 'manufactures_list.html', context)


def products_list(request, filter_by_name):

    try:
        manufacture = Manufacture.objects.get(name=filter_by_name)
        p = Paginator(Product.objects.filter(manufacture__name=filter_by_name).order_by('id'), 1)
        page = request.GET.get('page')
        products = p.get_page(page)
        category = None
    except:
        category = Category.objects.get(name=filter_by_name)
        p = Paginator(Product.objects.filter(category__name=filter_by_name).order_by('id'), 1)
        page = request.GET.get('page')
        products = p.get_page(page)
        manufacture = None

    context = {
        'products': products,
        'range': range(9),
        'category': category,
        'manufacture': manufacture,

    }
    return render(request, 'product_list.html', context)


def product_view(request, category_name, product_name):
    product = Product.objects.get(name=product_name)
    category = Category.objects.get(name=category_name)
    # manufacture = Manufacture.objects.get(name=category_name)

    return render(request, 'product_view.html',
                  context={
                      'category': category,
                      'product': product,
                  })


def campaign_list(request):
    p = Paginator(Campaign.objects.all().order_by('id'), 2)
    page = request.GET.get('page')
    objects = p.get_page(page)

    url_tree = {'home': 'Начало', 'campaign_list': 'Промоции'}

    context = {
        'objects': objects,
        'url_tree': url_tree,
        'object_url': 'campaign_view',
    }
    return render(request, 'objects_list.html', context)


def campaign_view(request, pk):
    object = Campaign.objects.get(id=pk)
    url_tree = {'home': 'Начало',
                'campaign_list': 'Промоции',
                }
    context = {
        'object': object,
        'url_tree': url_tree,
        'object_url': 'campaign_view',
    }
    return render(request, 'object_view.html', context)


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
