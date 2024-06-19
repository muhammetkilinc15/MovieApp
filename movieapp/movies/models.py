from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

 # Film Türü
class Genre(models.Model):
    name = models.CharField(max_length=100)


# Persona ait İletişim bilgileri
class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
   
   

# Person   
class Person(models.Model):
    
    genders = (
        ("M" , "Male"),
        ("F","Female"),
    )
    duty_types=(
        ("1","Crew"), # Görevli 
        ("2","Cast"), # Oyuncu
        ("3","Director"), # Yönetmen
        ("4","Writer") # Senarist
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    biography = models.CharField( max_length=3000)
    image_name = models.CharField(max_length=100)
    date_of_birth=  models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1,choices=genders)
    duty_type = models.CharField(max_length=50,choices = duty_types)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE,null=True,blank=True)

# Filme ait model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators = [MinLengthValidator(20)])
    image_name = models.CharField(max_length=50)
    image_cover  = models.CharField( max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField(max_length=100)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)
    

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField( max_length=200)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)


