from django import forms

class CarForm(forms.Form):
    YEAR_CHOICES = [(i, i) for i in range(1950, 2031)]

    year = forms.ChoiceField(choices=YEAR_CHOICES)
    present_price = forms.FloatField()
    kms_driven = forms.IntegerField()
    owner = forms.IntegerField()
    fuel_type_petrol = forms.BooleanField(required=False)
    seller_type_individual = forms.BooleanField(required=False)
    transmission_manual = forms.BooleanField(required=False)


