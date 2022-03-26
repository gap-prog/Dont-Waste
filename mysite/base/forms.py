from django.forms import ModelForm
from .models import Listing

class ListingsForm(ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ["lister"]