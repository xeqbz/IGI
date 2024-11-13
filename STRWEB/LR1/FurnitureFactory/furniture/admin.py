from django.contrib import admin
from .models import Employee, ProductType, Product, ProductModel, Client, Sale, CompanyInfo, Vacancy, PromoCode, News, Faq, Review, PartnerCompany
from django.contrib.auth.models import Group


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'position', 'contact_info', 'email', 'photo')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_code', 'price', 'product_type', 'product_model', 'status')


admin.site.register(ProductModel)
admin.site.register(ProductType)
admin.site.register(Sale)
admin.site.register(News)
admin.site.register(Faq)
admin.site.register(Review)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'address')


admin.site.register(CompanyInfo)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
