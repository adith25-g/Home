from  django import forms
from django.contrib.auth.models import User
from .models import Customer,Payment
# from forms.helper import FormHelper
# from forms.layout import Layout
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['id','user','locality','city','mobile','pincode']
       
class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['user','amount']
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.layout = Layout(
    #         'name',
    #         'amount',
    #         Button('Buy',css_class="button white btn-block btn-primary")
    #     )


