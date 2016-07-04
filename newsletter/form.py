from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField(required=False)

    def clean_email(self):
        mymail = self.cleaned_data.get('email')
        if not "@gmail" in mymail:
            raise forms.ValidationError("use your gmail id")
        return mymail




class SingnUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields=['email','full_name']
    def clean_email(self):
        mymail=self.cleaned_data.get('email')
        if not "@gmail" in mymail:
            raise forms.ValidationError("use your gmail id")
        return mymail