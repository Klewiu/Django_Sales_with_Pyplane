from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(label='Select date FROM', widget=forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(label='Select date TO', widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(label='Select char type', choices=CHART_CHOICES)