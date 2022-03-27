from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Listing

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Username',
                'class': 'form_fields',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Password',
                'class': 'form_fields',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
                'class': 'form_fields',
            }
        )

class ListingsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Title',
                'class': 'form_fields',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Description',
                'class': 'form_text',
            }
        )
        self.fields['item'].widget.attrs.update(
            {
                'placeholder': 'Item',
                'class': 'form_fields',
            }
        )
        self.fields['item_amount'].widget.attrs.update(
            {
                'placeholder': 'Amount',
                'class': 'form_fields',
            }
        )
        self.fields['item_amount_unit'].widget.attrs.update(
            {
                'placeholder': 'Amount Unit',
                'class': 'form_fields',
            }
        )
        self.fields['item_expiration_date'].widget.attrs.update(
            {
                'placeholder': 'Expiration Date',
                'class': 'form_fields',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
                'class': 'form_fields'
            }
        )
    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ["lister", "claim"]