from django.db import models
# Create your models here.

#Customer model
class customer(models.Model):
    name = models.CharField(verbose_name='Customer_name',max_length=255, null=True, blank=True ,default='Zaid')
    address = models.CharField(verbose_name='customer_address', max_length= 200, null=True, blank=True)
    phone = models.IntegerField("customer_phone", null=True, blank=True)
    email = models.EmailField("customer_email", max_length=254, null=True, blank=True)
    
    def __str__(self):
        return f"name{self.name}-address{self.address}-phone{self.phone}-email{self.email}"
    

class Section(models.TextChoices):
    BookStore = 'Book_Store', 'Book_Store'
    DrawSore = 'Draw_Store', 'Draw_Store'


class product(models.Model):
    name = models.CharField(verbose_name='product_name', max_length=255)
    section = models.CharField('section', max_length=100, choices=Section.choices)
    price = models.FloatField(verbose_name='product_price', default=0.0)
    image = models.URLField('product_image', blank=True, null=True)

    language = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'Franch'),
    ]),
    category = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Scientific', 'Scientific'),
        ('Art', 'Art'),
        ('Historic', 'Historic'),
        ('Novels', 'Novels'),
        ('Fictional', 'Fictional'),
    ])

    # Here is Boolean Field 
    # A true/false field.
    is_active = models.BooleanField('is_active', default=True)
    is_rare = models.BooleanField('is_rare', default=False)
    is_DrawTool = models.BooleanField('is_book', default=False)
    #auth = models.ForeignKey('BookAuth', null=True, blank=True, on_delete=models.SET_NULL, related_name='products')

    def __str__ (self):
        return f'{self.name}-{self.category}-{self.is_DrawTool}'
    
#Order model
class order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    details = models.CharField('Details',null=True,blank= True, max_length=255)
    date = models.DateField("order date")
    
    def __str__(self):
        return f'{self.id} - {customer.name} - {product.name} - {self.quantity} - {self.date}'
    
#Cart model
class cart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{product.name}-{self.quantity}'

#class BookAuth(models.Model):
#    name = models.CharField('auth_name', max_length=100)
#    email = models.EmailField('auth_email', max_length=254, null=True, blank=True)
#    phone = models.CharField('auth_phone', max_length=100)
#    number_of_book = models.IntegerField('number_of_book', default=0)
#    def __str__(self):
#        return f'{self.name}-{self.email}'

