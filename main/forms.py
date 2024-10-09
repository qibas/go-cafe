from django import forms
from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        # Use strip_tags to remove any HTML tags from the name field
        cleaned_name = strip_tags(name)
        return cleaned_name

    def clean_description(self):
        description = self.cleaned_data["description"]
        # Use strip_tags to remove any HTML tags from the description field
        cleaned_description = strip_tags(description)
        return cleaned_description
