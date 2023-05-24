from django import forms
from app1.models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"  #('name','phone#') #