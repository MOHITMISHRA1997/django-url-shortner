from django.db import models

# Create your models here.

class URLmodel(models.Model):
    sno = models.AutoField(primary_key=True)
    orignal_url = models.URLField("URL", unique=False)
    new_url = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.orignal_url
    
