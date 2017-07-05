from django.db import models
from django.utils import timezone

# Create your models here.

class Candidate(models.Model):
    
#manager is linked to a registered user 
# in the 'auth_user' table

    manager = models.ForeignKey('auth.user')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField(max_length=150)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    cv = models.FileField(upload_to='cvDocs', blank=True, null=True )
    created_date = models.DateTimeField(auto_now_add=True)
    deactivated_date = models.DateTimeField(blank=True, null=True)
    interview_stage = models.IntegerField( null=False, blank=False)

    def deactivate(self):
        self.deactivated_date = timezone.now()
        self.save()
    
    #Candidate is active if deactivated date is null
    def activate(self):
        self.deactivated_date = null
        self.save()

    def __str__(self):
        name = "{0} {1}".format(self.first_name, self.last_name)
        return name