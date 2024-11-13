import os
from datetime import datetime, timedelta, date
import django.db.models
import numpy as np
from django.conf import settings
from django.db.models import Count, Sum, Max, Min
from matplotlib import pyplot as plt
from .models import Employee, CompanyInfo, Vacancy, PromoCode, Review, ProductModel, ProductType, Product, Sale, Client, News, Faq, PartnerCompany
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse, reverse_lazy, path
from .forms import ReviewForm, ClientForm, PromoCodeForm
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin


def index(request):
    latest_news = News.objects.order_by('-pub_date').first()
    companies = PartnerCompany.objects.all()
    return render(request, "index.html", {'latest_news': latest_news, 'companies': companies})


def about(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company_info': company_info})


def news(request):
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

def dictionary(request):
    faq_list = Faq.objects.all()
    return render(request, 'dictionary.html', {'faq_list': faq_list})


def contacts(request):
    employees = Employee.objects.all()
    return render(request, 'contacts.html', {'employees': employees})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def vacancies(request):
    vacancies_list = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancies_list})


#def promo_codes(request):
 #   current_date = timezone.now().date()
  #  active_promo_codes = PromoCode.objects.filter(start_date__lte=current_date, end_date__gte=current_date)
   # expired_promo_codes = PromoCode.objects.filter(end_date__lt=current_date)

    #return render(request, 'promo_codes_list.html', {
     #   'active_promo_codes': active_promo_codes,
      #  'expired_promo_codes': expired_promo_codes,
    #})

def promo_codes_list(request):
    current_date = timezone.now().date()
    active_promo_codes = PromoCode.objects.filter(start_date__lte=current_date, end_date__gte=current_date)
    expired_promo_codes = PromoCode.objects.filter(end_date__lt=current_date)

    return render(request, 'promo_codes_list.html', {
        'active_promo_codes': active_promo_codes,
        'expired_promo_codes': expired_promo_codes,
    })


@user_passes_test(lambda u: u.is_superuser)
@login_required
def promo_code_create(request):
    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promo_codes_list')
    else:
        form = PromoCodeForm()
    return render(request, 'promo_code_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def promo_code_update(request, pk):
    promo_code = get_object_or_404(PromoCode, pk=pk)
    if request.method == 'POST':
        form = PromoCodeForm(request.POST, instance=promo_code)
        if form.is_valid():
            form.save()
            return redirect('promo_codes_list')
    else:
        form = PromoCodeForm(instance=promo_code)
    return render(request, 'promo_code_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def promo_code_delete(request, pk):
    promo_code = get_object_or_404(PromoCode, pk=pk)
    if request.method == 'POST':
        promo_code.delete()
        return redirect('promo_codes_list')
    return render(request, 'promo_code_delete.html', {'promo_code': promo_code})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('home'))  # Redirect to the furniture page after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def review_list(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'review_list.html', {'reviews': reviews, 'form': form})


def get_random_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    return data["fact"] if "fact" in data else "No cat facts available"


def get_random_activity():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return data['setup'] + ' ' + data['punchline'] if data['setup'] and data['punchline'] else "No jokes available"


def products_list(request):
    if request.method == 'POST':
        product_code = request.POST.get('product_code')
        product = Product.objects.get(product_code=product_code)
        request.session['product_code'] = product_code
        return redirect('client_form')

    products = Product.objects.all()
    product_types = ProductType.objects.all()
    product_models = ProductModel.objects.all()
    product_type_id = request.GET.get('product_type')
    if product_type_id:
        products = products.filter(product_type_id=product_type_id)

    product_model_id = request.GET.get('product_model')
    if product_model_id:
        products = products.filter(product_model_id=product_model_id)

    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)


    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')

    return render(request, 'products_list.html',
                  {'products': products, 'product_types': product_types, 'product_models': product_models})


@login_required
def client_form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            product_code = request.session.get('product_code')
            if product_code:
                product = Product.objects.get(product_code=product_code)
                Sale.objects.create(client=client, products=product)
                return redirect('products_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})


@login_required
def client_profile(request):
    username = request.user.username
    return render(request, 'client_profile.html', {'username': username})


@login_required
def employee_profile(request):
    sales = Sale.objects.all()
    clients = Client.objects.all()

    return render(request, 'employee_profile.html', {
        'sales': sales,
        'clients': clients,
    })


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
def superuser_profile(request):
    product_types = ProductType.objects.all()
    clients_by_city = Client.objects.values('city').annotate(total=Count('id'))
    max_total_sales = Product.objects.annotate(total_sales=Count('sale')).aggregate(max_total_sales=Max('total_sales'))[
        'max_total_sales']
    most_popular_products = Product.objects.annotate(total_sales=Count('sale')).filter(total_sales=max_total_sales)

    min_total_sales = Product.objects.annotate(total_sales=Count('sale')).aggregate(min_total_sales=Min('total_sales'))[
        'min_total_sales']
    least_popular_products = Product.objects.annotate(total_sales=Count('sale')).filter(total_sales=min_total_sales)
    today = date.today()
    current_month = today.month
    current_year = today.year

    # Вычисляем начало и конец текущего месяца
    start_date = date(current_year, current_month, 1)
    end_date = start_date + timedelta(days=31)  # Добавляем один день, чтобы включить весь текущий месяц

    # Получаем все типы продуктов
    product_types = ProductType.objects.all()

    # Вычисляем ежемесячный объем продаж для каждого типа продуктов
    monthly_sales = []
    for product_type in product_types:
        sales = Sale.objects.filter(products__product_type=product_type, order_date__gte=start_date,
                                    order_date__lte=end_date)
        total_sales = sales.aggregate(total_sales=Sum('products__price'))['total_sales'] or 0
        monthly_sales.append({'product_type': product_type, 'total_sales': total_sales})
    start_date = date(current_year, 1, 1)
    end_date = date(current_year, 12, 31)

    # Вычисляем годовой подсчет поступлений от продаж
    annual_sales = Sale.objects.filter(order_date__gte=start_date, order_date__lte=end_date)
    total_revenue = annual_sales.aggregate(total_revenue=Sum('products__price'))['total_revenue'] or 0

    sales_by_product = Product.objects.annotate(total_sales=Count('sale')).order_by('-total_sales')

    # Получаем названия продуктов и их количество продаж
    product_names = [product.name for product in sales_by_product]
    sales_counts = [product.total_sales for product in sales_by_product]

    # Создаем график
    plt.figure(figsize=(10, 6))
    plt.bar(product_names, sales_counts)
    plt.xlabel('Product')
    plt.ylabel('Number of Sales')
    plt.title('Sales by Product')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Сохраняем график в формате PNG
    graph_path = os.path.join(settings.BASE_DIR, 'static', 'graphs', 'sales_by_product.png')

    # Проверяем, существует ли папка static/graphs
    os.makedirs(os.path.dirname(graph_path), exist_ok=True)

    # Сохраняем график в файл
    plt.savefig(graph_path, format='png')

    context = {
        'product_types': product_types,
        'clients_by_city': clients_by_city,
        'most_popular_products': most_popular_products,
        'least_popular_products': least_popular_products,
        'monthly_sales': monthly_sales,
        'total_revenue': total_revenue,
        'current_year':current_year,
        'graph_path': graph_path,
    }
    return render(request, 'superuser_profile.html', context)


def chair(request):
    return render(request, 'chair.html')


def table(request):
    return render(request, 'table.html')


def closet(request):
    return render(request, 'closet.html')


def cart(request):
    return render(request, 'cart.html')


def payment(request):
    return render(request,'payment.html')


def task(request):
    return render(request,'task.html')
