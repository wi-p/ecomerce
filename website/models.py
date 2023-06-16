from django.db import models
from django.utils.text import slugify

# add editor and age attributs \

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length = 30, primary_key = True)
    title = models.CharField(max_length = 100)
    writter = models.CharField(max_length = 100)
    publication_date = models.DateField()
    description = models.CharField(max_length = 500)
    download_number = models.IntegerField(default = 0)
    genre = models.CharField(max_length = 20)
    publisher = models.CharField(max_length = 50)
    age = models.CharField(max_length = 10)
    photo = models.FileField(upload_to = 'website/bookphotos/')
    file = models.FileField(upload_to = 'website/bookfiles/')
    price = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
        
        
class User(models.Model):
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 10)
    address = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 20)
    login_date = models.DateField()
    my_books = models.ManyToManyField(Book, through = 'UserCart')
    
    def __str__(self):
        return self.username
        

class UserComment(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    book_isbn = models.ForeignKey(Book, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 500)
    comment_date = models.DateField()
    
    def __str__(self):
        return self.id
        
        
class UserCart(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    book_isbn = models.ForeignKey(Book, on_delete = models.CASCADE)
    buyed = models.BooleanField(default = False)
    buy_date = models.DateField()
    
    def __str__(self):
        return self.id