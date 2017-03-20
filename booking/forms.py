from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from booking.models import Booking, Country, State, City


class BookForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['firstname', 'surname', 'email', 'date_in', 'date_out', 'country_out', 'country_in', 'state_out',
                  'state_in', 'city_out', 'city_in']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['date_in'] = forms.DateField(widget=AdminDateWidget)
        self.fields['date_out'] = forms.DateField(widget=AdminDateWidget)
        self.fields['country_out'] = forms.ModelChoiceField(queryset=Country.objects.all())
        self.fields['country_in'] = forms.ModelChoiceField(queryset=Country.objects.all())
        self.fields['state_out'] = forms.ModelChoiceField(queryset=State.objects.filter(id=0))
        self.fields['state_in'] = forms.ModelChoiceField(queryset=State.objects.filter(id=0))
        self.fields['city_out'] = forms.ModelChoiceField(queryset=City.objects.filter(id=0))
        self.fields['city_in'] = forms.ModelChoiceField(queryset=City.objects.filter(id=0))
