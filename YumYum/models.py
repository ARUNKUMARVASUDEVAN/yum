from django.db import models
from django.contrib.auth.models import User

AGE_CHOICES = (
    ('<12', 'Less than 12'),
    ('12<18', '12 to 17'),
    ('>18', 'Over 18'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

class book(models.Model):
    Name = models.CharField(max_length=50, default="")
    Age = models.CharField(max_length=5, choices=AGE_CHOICES, default="")
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="")
    Phone = models.IntegerField(default="")
    Email = models.EmailField(max_length=100, default="")
    Date= models.DateField(default="")
    Time= models.TimeField(default="")
    Address1 = models.CharField(max_length=100, default="")
    Count= models.IntegerField(default="")
    Request = models.CharField(max_length=100, default="")
    Table = models.IntegerField(default=1)

    def __str__(self):
        return self.Name

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.message[:50]}"

class Starter(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='starters/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class Dessert(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='desserts/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Gelato(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gelatos/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class Mocktail(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mocktails/')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Shake(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shakes/')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Indian(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='indian/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class Chinese(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chinese/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class American(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='american/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starter = models.ForeignKey(Starter, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'starter')  

    def __str__(self):
        return f"{self.user.username}'s Cart - {self.starter.name}: {self.quantity}"

    def update_quantity(self, quantity):
        if quantity > 0:
            self.quantity = quantity
            self.save()
        else:
            self.delete()