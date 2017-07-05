from django import forms
from .models import Candidate

class NewCandidateForm(forms.ModelForm):

   class Meta:
       model = Candidate
       fields = ('first_name', 'last_name', 'description', 'email', 'phone', 'image', 'cv')
