from django import forms
from .models import yellowm,Reviews
from django.contrib.auth.models import User

class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
        #the only check we have to do is compare passwords
        #creating a CharField object by passing values into the constructor
        password = forms.CharField(label="Password",widget=forms.PasswordInput)
        password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

        class Meta:
            #in meta , we specify which model the form is for and the fields
            model = User
            fields = ('username','first_name','email','password')
        #naming convection is clean_<fieldname>
        def clean_password2(self):
            #clean the data in the context
            cd=self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords not matching')
            return cd['password2']

class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = yellowm #the post model from model.py and its fields for user to input
        fields = ('business_name', 'business_category', 'business_shortname', 'profile_image',
                  'person_name','phone_number','email','website')


class BusinessEditForm(forms.ModelForm):
    class Meta:
        model = yellowm #the post model from model.py and its fields for user to input
        fields = ('business_name', 'business_category', 'business_shortname', 'profile_image',
                  'person_name','phone_number','email','website')

class ReviewsAddForm(forms.ModelForm):
    class Meta:
        model = Reviews #the post model from model.py and its fields for user to input
        fields = ( 'rating','title', 'description', 'video_url')

class ReviewerRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        # in meta , we specify which model the form is for and the fields
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    # naming convection is clean_<fieldname>
    def clean_password2(self):
        # clean the data in the context
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matching')
        return cd['password2']