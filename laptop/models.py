from django.db import models
from django.shortcuts import render

class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='laptops/')
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.brand} {self.model}"

class Customization(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    customization_name = models.CharField(max_length=100)
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.customization_name} for {self.laptop}"


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(6)] 
    customer_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES) 

    def __str__(self):
        return self.customer_name

class Purchase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    payment_method = models.CharField(max_length=50)

    def _str_(self):
        return f"Purchase by {self.name} with {self.payment_method}"

def reviews_page(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_page.html', {'reviews': reviews})