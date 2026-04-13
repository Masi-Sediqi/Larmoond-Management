from django.db import models
from customers.models import Customer

class Domain(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    domain_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Domain Name"
    )

    client = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Client"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Status"
    )

    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    registrar = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Registrar (e.g. GoDaddy, Namecheap)"
    )

    dns_provider = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="DNS Provider (e.g. Cloudflare)"
    )

   
    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Notes"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain_name

class Server(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    server_name = models.CharField(
        max_length=255,
        verbose_name="Server Name"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Status"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price"
    )

    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    # 🔧 Server Specifications
    cpu_cores = models.IntegerField(
        default=1,
        verbose_name="CPU Cores"
    )

    ram_gb = models.IntegerField(
        default=1,
        verbose_name="RAM (GB)"
    )

    storage_gb = models.IntegerField(
        default=20,
        verbose_name="Storage (GB)"
    )

    bandwidth_tb = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1,
        verbose_name="Bandwidth (TB)"
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name="IP Address"
    )

    provider = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Hosting Provider (AWS, DigitalOcean, etc.)"
    )

    operating_system = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Operating System (Ubuntu, Windows, etc.)"
    )

    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Notes"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.server_name