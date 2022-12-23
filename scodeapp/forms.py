from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 1000)
	last_name = forms.CharField(max_length = 1000)
	email_address = forms.EmailField(max_length = 1000)
	message = forms.CharField(widget = forms.Textarea(attrs={'rows':3}))