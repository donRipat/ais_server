from django.db import models

# Create your models here.


class Status(models.Model):
    abbreviation = models.CharField(max_length=10)
    meaning = models.CharField(max_length=100)

    def __str__(self):
        return self.abbreviation

    class Meta:
        verbose_name_plural = "Statuses"


class ApparatusName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Apparatus(models.Model):
    name = models.ForeignKey(ApparatusName, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return str({"name": self.name.name,
                    "status": self.status.meaning})

    class Meta:
        verbose_name_plural = "Apparatuses"


class DeviceName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.ForeignKey(DeviceName, on_delete=models.PROTECT)
    apparatus = models.ForeignKey(Apparatus, related_name="devices", on_delete=models.PROTECT)

    def __str__(self):
        return str({"Device": self.name,
                    "Apparatus": self.apparatus})


class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    device = models.ForeignKey(Device, related_name="sensors", on_delete=models.CASCADE)
    parameter = models.CharField(max_length=100, unique=True)
    lower = models.DecimalField(max_digits=10, decimal_places=5)
    upper = models.DecimalField(max_digits=10, decimal_places=5)
    current = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return str({"name": self.name,
                    'device': self.device,
                    "parameter": self.parameter,
                    "lower limit": self.lower,
                    "upper limit": self.upper,
                    'current value': self.current,
                    'date': self.date,
                    'time': self.time})
