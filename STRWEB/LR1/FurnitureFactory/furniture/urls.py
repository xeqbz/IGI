from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from .views import promo_codes_list, promo_code_create, promo_code_update, promo_code_delete

urlpatterns = [
    path('furniture/', views.index, name='home'),
    path('about/', views.about),
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('dictionary/', views.dictionary),
    path('contacts/', views.contacts),
    re_path(r'^privacy_policy/$', views.privacy_policy),
    path('vacancies/', views.vacancies),
    #path('promo_codes/', views.promo_codes),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_view, name='login'),
    path('reviews/', views.review_list, name='review_list'),
    path('products_list/', views.products_list, name='products_list'),
    #path('profile/', views.profile, name='profile'),
    path('superuser_profile/', views.superuser_profile, name='superuser_profile'),
    path('employee_profile/', views.employee_profile, name='employee_profile'),
    path('client_form/', views.client_form, name='client_form'),
    path('client_profile/', views.client_profile, name='client_profile'),
    path('promo_codes_list/', promo_codes_list, name='promo_codes_list'),
    path('promo_codes/new/', promo_code_create, name='promo_code_create'),
    path('promo_codes/<int:pk>/edit/', promo_code_update, name='promo_code_update'),
    path('promo_codes/<int:pk>/delete/', promo_code_delete, name='promo_code_delete'),
    path('chair/', views.chair),
    path('table/', views.table),
    path('closet/', views.closet),
    path('cart/', views.cart),
    path('cart/payment.html', views.payment),
    path('task/', views.task)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

