from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200, default='')
    pub_date=models.DateTimeField('date published', default='')
    body=models.TextField(default='')
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:10000]
    
    def summaryone(self):
        return self.body[:100]
