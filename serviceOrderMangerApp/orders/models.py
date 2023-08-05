from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    warranty_service = models.BooleanField(default=False, verbose_name='Centro tecnico autorizado?')
    company = models.CharField(max_length=50, verbose_name='Compañía', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    TYPE_CHOICES = (
        ('electric_tools', 'Herramientas electricas'),
        ('cordless_tools', 'Herramientas inalámbricas'),
        ('combustion_machines', 'Maquinas de combustión'),
        ('welding', 'Soldadura'),
        ('home_appliances', 'Electrodomésticos'),
        ('white_line', 'Linea blanca'),
        ('agricultural_tools', 'Herramienta agrícola'),
        ('others', 'Otros'),
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0],
        verbose_name='Tipo')
    
    def __str__(self):
        return self.name
    

class Reference(models.Model):
    reference = models.CharField(max_length=20, verbose_name='Referencia')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='get_refencies', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='get_refencies', verbose_name='Categoria')
    manpower = models.DecimalField(max_digits=8, decimal_places=0, null=True, verbose_name='Mano de obra')
    exploded_view = models.FileField(upload_to='exploded_views', null=True, verbose_name='Despiece')
    
    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'Referencies'
        ordering = ['reference']
        
    def __str__(self):
        return self.reference


class User(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='Nombre completo')
    document = models.CharField(max_length=20, verbose_name='Documento')
    phone_number = models.CharField(max_length=20, verbose_name='Celular')
    second_phone_number = models.CharField(max_length=20, verbose_name='Telefono')
    municipality = models.CharField(max_length=30, verbose_name='Municipio')
    address = models.CharField(max_length=200, verbose_name='Direccion')
    

class Collaborator(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    occupation = models.CharField(max_length=50, verbose_name='Cargo')
    email = models.EmailField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=20, verbose_name='Contraseña')
    
    class Meta:
        verbose_name = "Collaborator"
        verbose_name_plural = "Collaborators"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
     
class Order(models.Model):
    entry_date = models.DateTimeField("Fecha de ingreso")
    is_guarantee = models.BooleanField(default=False)
    service_number = models.CharField(max_length=30, null=True)
    brand_of_the_product = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT)
    serial = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    observations = models.TextField(max_length=500)
    diagnostic = models.TextField(max_length=1000, null=True)
    received_by = models.ForeignKey(Collaborator, related_name='recibido_por', on_delete=models.PROTECT)
    estimate_for_repair = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    payment = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    payment_for_revision = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    paid = models.BooleanField(default=False)
    checked_and_or_repaired_by = models.ForeignKey(Collaborator, related_name='revisado_o_reparado_por', on_delete=models.PROTECT)

    STATE_CHOICES = [
        ('received', 'Recibido'),
        ('admitted', 'Ingresado'),
        ('in_revision', 'En revision'),
        ('revised', 'Revisado'),
        ('waiting_for_spare_parts', 'En espera de respuestos'),
        ('in_repair', 'En reparacion'),
        ('repaired', 'Listo para entregar'),
        ('delivered', 'Entregado'),
    ]
    state = models.CharField(
        max_length=25,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[0]
    )
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['entry_date']
        
    def __str__(self):
        return self.service_number
    

class Evidence(models.Model):
    image = models.ImageField(upload_to='evidences', verbose_name='Imagen')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='evidences', verbose_name='Orden')