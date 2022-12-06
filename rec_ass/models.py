from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_users = models.IntegerField()
    bio = models.TextField(blank = True)
    profileImagge = models.ImageField(upload_to='profil_images',default='Certificate(2).jpg')
    location = models.CharField(max_length=100, blank=True)
    
    def _str_(self) : 
        return self.user.username
        
# Create your models here.
