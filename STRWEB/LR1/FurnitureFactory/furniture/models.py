from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    """
    Model representing an employee
    """
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    first_name = models.CharField(max_length=100, default='Jack')
    last_name = models.CharField(max_length=100, default='Jones')
    position = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s, %s' % (self.last_name, self.first_name)


class ProductType(models.Model):
    """
    Model representing a product type
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class ProductModel(models.Model):
    """
    Model representing a product model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Product(models.Model):
    """
    Model representing a product
    """
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)

    MAKE = (
        ('+', 'Производится'),
        ('-', 'Снято с производства'),
    )

    status = models.CharField(max_length=20, choices=MAKE)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Client(models.Model):
    """
    Model representing a client
    """
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=22, default="+375 (29) ")
    address = models.CharField(max_length=200)

    CITIES = (
        ('Br', 'Brest'),
        ('Gr', 'Grodno'),
        ('Vb', 'Vitebsk'),
        ('Mg', 'Mogilev'),
        ('Mn', 'Minsk'),
        ('Gm', 'Gomel'),
    )

    city = models.CharField(max_length=10, choices=CITIES)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Sale(models.Model):
    """
    Model representing a sale
    """
    id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    #completion_date = models.DateField()
    client = models.CharField(max_length=200)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.client}"


class CompanyInfo(models.Model):
    """
    Model representing a company info
    """
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/')
    video = models.FileField(upload_to='videos/')
    history = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    certificate = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """
    Model representing a vacancy
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class PromoCode(models.Model):
    """
    Model representing a Promo code
    """
    code = models.CharField(max_length=8)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.code

    def is_active(self):
        return self.start_date <= timezone.now().date() <= self.end_date


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username}'

    class Meta:
        ordering = ['-date']


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question


class PartnerCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компании")
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип")
    website = models.URLField(max_length=255, verbose_name="Сайт компании")
