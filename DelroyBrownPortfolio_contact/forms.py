# DelroyBrownPortfolio_contact/forms.py
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.ChoiceField(
        choices=[
            ("1", "Account"),
            ("2", "Service"),
            ("3", "Pricing"),
            ("4", "Support"),
        ]
    )
    message = forms.CharField(widget=forms.Textarea)
