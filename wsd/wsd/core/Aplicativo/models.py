from django.db import models
from datetime import datetime
class Monitor(models.Model):
    names=models.CharField(max_length=150,verbose_name='Nombres')
    id=models.CharField(max_length=15,unique=True,verbose_name='Identificacion',primary_key=True)
    date_joined=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_create=models.DateField (default=datetime.now)
    date_update=models.DateTimeField(default=datetime.now)
    age= models.PositiveIntegerField(default=0)
    salary= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    CVitae=models.FileField(upload_to='cvitae/%Y/%m/%d ', null=True, blank=True)
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name='empleado'
        verbose_name_plural='empleados'
        db_table='empleado'
        ordering=['id']
    

