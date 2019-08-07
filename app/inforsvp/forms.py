from django import forms


class RSVPForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=500)
    email = forms.EmailField(label="Email")
    number_attending = forms.IntegerField(label="Number Attending", max_value=50)
    extra_info = forms.CharField(label="Anything we should know?", max_length=5000, required=False)
