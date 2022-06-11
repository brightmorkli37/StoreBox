from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField()
    ref = models.CharField(max_length = 400)
    email = models.EmailField()
    verified = models.BooleanField(default= False)
    date_created = models.DateTimeField(auto_now_add=True)
    method_of_payment = models.CharField(max_length = 1000,null = True, blank = True, default = "electronically")
    payment_info = models.CharField(max_length = 1000,null = True, blank = True)

    
    def amount_value(self) -> int:
        return self.amount * 100