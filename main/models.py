from email.mime import image
from unicodedata import category
from django.db import models

        
class Slider(models.Model):
    image = models.ImageField(upload_to="Slider/")

class Logo(models.Model):
    image = models.ImageField(upload_to="Logo/")

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="News/")
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Malumotlar(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="Malumotlar/")
    title = models.CharField(max_length=100)
    text= models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

class Video(models.Model):
    video = models.FileField(upload_to="Video/")

class VideoNews(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=350)

class Xabarlar(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="Xabarlar/")
    title = models.CharField(max_length=100)
    text= models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
class Reklama(models.Model):
    image = models.ImageField(upload_to="Reklama/")
    link = models.CharField(max_length=400)

class FoydaliSaytlar(models.Model):
    image = models.ImageField(upload_to="FoydaliSaytlar/")
    link = models.CharField(max_length=400)

class AndOrganing(models.Model):
    image = models.ImageField(upload_to="AndOrganing/")
    link = models.CharField(max_length=400)

class Malumotlar2(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="Malumotlar2/")
    title = models.CharField(max_length=100)
    text= models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
class TavsiyaVideo(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to="TavsiyaVideo/")
    date = models.DateField(auto_now_add=True)

class Kerak(models.Model):
    image = models.ImageField(upload_to="Kerak/")
    title1 = models.CharField(max_length=150)
    title2 = models.CharField(max_length=100)

class Loyiha1(models.Model):
    image = models.ImageField(upload_to="Loyiha1/")
    link = models.CharField(max_length=400)

class Xizmatlar(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Xizmatlar/")

class Andijon(models.Model):
    image = models.ImageField(upload_to="Andijon/")
    andijon = models.TextField()
    dengiz = models.CharField(max_length=100)
    aholi = models.CharField(max_length=100)
    maydoni = models.CharField(max_length=100)
    harorat = models.CharField(max_length=100)
    text = models.TextField()
    info = models.CharField(max_length=100)
    #map qoshish kerak

class Loyiha2(models.Model):
    image = models.ImageField(upload_to="Loyiha2/")
    link = models.CharField(max_length=400)

class InvsTarmoqlar(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="InvsTarmoqlar/")
    text = models.CharField(max_length=300)

class Hujjat(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="Hujjat/")
    link = models.CharField(max_length=400)

class QoshimchaXizmat(models.Model):
    image = models.ImageField(upload_to="QoshimchaXizmat/")
    title = models.CharField(max_length=400)

class Savol(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name

class Javob(models.Model):
    savol = models.ForeignKey(Savol, on_delete=models.CASCADE)
    javob = models.CharField(max_length=200)
    def __str__(self):
        return self.javob

class Savol_Javob(models.Model):
    jovoblar = models.ManyToManyField(Javob, blank=True)

class Loyiha3(models.Model):
    image = models.ImageField(upload_to="Loyiha3/")
    link = models.CharField(max_length=400)

class Info(models.Model):
    link1 = models.CharField(max_length=202)
    link2 = models.CharField(max_length=202)
    link3 = models.CharField(max_length=202)
    phone = models.CharField(max_length=100)

    
