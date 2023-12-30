from django.db import models
from django.contrib.auth.models import AbstractUser


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    warranty_service = models.BooleanField(
        default=False, verbose_name='Centro tecnico autorizado?')
    company = models.CharField(
        max_length=50, verbose_name='Compañía', null=True, blank=True)
    image = models.ImageField(
        upload_to='logos', verbose_name='Logo o imagen', null=True)

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
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='get_refencies', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='get_refencies', verbose_name='Categoria')
    manpower = models.DecimalField(
        max_digits=8, decimal_places=0, null=True, verbose_name='Mano de obra')
    exploded_view = models.FileField(
        upload_to='exploded_views', null=True, verbose_name='Despiece')

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'Referencies'
        ordering = ['reference']

    def __str__(self):
        return self.reference


class Client(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='Nombre completo')
    genred = models.CharField(max_length=20, verbose_name="Genero", null=True)
    is_company = models.BooleanField(default=False)
    document = models.CharField(
        max_length=20, verbose_name='Documento', unique=True)
    phone_number = models.CharField(max_length=20, verbose_name='Celular')
    second_phone_number = models.CharField(
        max_length=20, verbose_name='Telefono', null=True)
    email = models.CharField(max_length=50, verbose_name='email', null=True)
    municipality = models.CharField(max_length=30, verbose_name='Municipio')
    address = models.CharField(
        max_length=200, verbose_name='Direccion', null=True)

    def __str__(self):
        return self.fullname


class User(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    fullname = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    email = models.EmailField('email address', max_length=50, unique=True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['fullname']

    def __str__(self):
        return self.fullname


class Order(models.Model):
    is_guarantee = models.BooleanField(default=False)
    service_number = models.CharField(max_length=30, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT)
    serial = models.CharField(max_length=30, null=True)
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name='Order')
    reason_for_entry = models.CharField(max_length=200, null=True)
    observations = models.TextField(max_length=500)
    diagnostic = models.TextField(max_length=1000, null=True)
    is_necesary_spare_parts = models.BooleanField(default=False)
    spare_parts_list = models.TextField(max_length=2000, null=True)
    estimate_for_repair = models.DecimalField(
        max_digits=8, decimal_places=0, null=True)
    payment = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    payment_for_revision = models.DecimalField(
        max_digits=8, decimal_places=0, null=True)
    paid = models.BooleanField(default=False)
    entry_date = models.DateTimeField("Fecha recibido")
    admitted_date = models.DateField("Fecha ingresado", null=True)
    revised_date = models.DateField("Fecha revisado", null=True)
    warranty_denial_date = models.DateField(
        "Fecha negacion garantia", null=True)
    quoted_date = models.DateField("Fecha cotizado", null=True)
    reapired_date = models.DateField("Fecha reparado", null=True)
    delivered_date = models.DateField("Fecha entregado", null=True)
    received_by = models.ForeignKey(
        User, related_name='recibido_por', on_delete=models.PROTECT)
    checked_by = models.ForeignKey(
        User, related_name='revisado_por', on_delete=models.PROTECT, null=True)
    repared_by = models.ForeignKey(
        User, related_name='reparado_por', on_delete=models.PROTECT, null=True)
    dispatched_by = models.ForeignKey(
        User, related_name='entregado_por', on_delete=models.PROTECT, null=True)

    STATE_CHOICES = (
        ('received', 'Recibido'),
        ('admitted', 'Ingresado'),
        ('in_revision', 'En revision'),
        ('revised', 'Revisado'),
        ('waiting_response_brand', 'En espera de respuesta de la marca'),
        ('warranty_denial', 'Negacion de garantia'),
        ('quoted', 'Cotizado'),
        ('waiting_for_spare_parts', 'En espera de repuestos'),
        ('spare_parts_ready', 'Repuestos en taller'),
        ('in_repair', 'En reparacion'),
        ('repaired', 'Listo para entregar'),
        ('delivered', 'Entregado'),
    )
    state = models.CharField(
        max_length=25,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[0]
    )

    TYPE_CHOICES = (
        ('collect', 'Cobro'),
        ('warranty', 'Garantia'),
        ('workshop_warranty', 'Garantia de taller'),
        ('warranty_denial', 'Negacion de garantia'),
        ('workshop_warranty_denial', 'Negacion de garantia de taller'),
    )

    type_service = models.CharField(
        max_length=25,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0]
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        # ordering = ['entry_date']

    def __str__(self):
        return self.service_number


class Evidence(models.Model):
    image = models.ImageField(upload_to='evidences', verbose_name='Imagen')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='evidences', verbose_name='Orden')

    def __str__(self):
        return self.image.url
