from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

 # Film Türü
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    

# Persona ait İletişim bilgileri
class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.address} {self.email}"
   

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
    
    first_name = models.CharField("Ad",max_length=50)
    last_name = models.CharField ("Soyad",max_length=50)
    biography = models.CharField( max_length=3000)
    image_name = models.CharField(max_length=100)
    date_of_birth=  models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField("Cinsiyet",max_length=1,choices=genders)
    duty_type = models.CharField("Görev",max_length=50,choices = duty_types)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE,null=True,blank=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    full_name.fget.short_description = "Ad Soyad"

    class Meta:
        verbose_name = "Kişi"
        verbose_name_plural = "Kişiler"
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.duty_types[int(self.duty_type) -1][1]}"

# Filme ait model
class Movie(models.Model):
    title = models.CharField("Başlık",max_length=100)
    description = models.TextField("Açıklama",validators = [MinLengthValidator(20)])
    image_name = models.CharField("Resim",max_length=50)
    image_cover  = models.CharField("Kapak Fotoğraf",max_length=50)
    date = models.DateField("Tarih",auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True,db_index=True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    isActive = models.BooleanField(default=False)
    is_hone = models.BooleanField(default=False)
    language = models.CharField(max_length=100)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)
    
    # Menü de artık film ve filmler olarak gözükecek
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"
    
    
    def __str__(self):
        return f"{self.title}"

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField( max_length=200)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"

