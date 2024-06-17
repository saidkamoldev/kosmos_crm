from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ishchi '
        verbose_name_plural = 'Ishchilar '

class Client(models.Model):
    ishchi = models.ForeignKey(Worker, on_delete=models.SET_NULL,
                               null=True, blank=True)
    f_i_o = models.CharField(max_length=60)
    telefon_raqam = PhoneNumberField()  
    zayafka_vaqti = models.DateTimeField(auto_now_add=True)
    tekshirilgan_vaqti = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('KELADI', 'KELADI'),
        ('ULANILMADI', 'ULANILMADI'),
        ('QOLDIRILDI', 'QOLDIRILDI'),
        ('KEMIDI', 'KEMIDI')
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,
                              blank=True, null=True,)
    comment = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.f_i_o}"

    class Meta:
        verbose_name = 'Mijoz '
        verbose_name_plural = 'Mijozlar '
