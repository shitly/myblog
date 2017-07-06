from django import forms
from blog.models import Column


class SearchForm(forms.Form):
    serach_start = forms.DateField(
        widget = forms.DateInput(
            attrs={'class': ['form-control', 'vDateField'],
                   'id': 'id_serach_start',
                   }),
    )
    serach_end = forms.DateField(
        widget = forms.DateInput(
            attrs={'class': ['form-control', 'vDateField'],
                   'id': 'id_serach_end',
                   }),
    )
    tag = forms.ModelChoiceField(label=u"栏目", queryset=Column.objects.all())
    title_word = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'title_word',
                   'placeholder': '模糊标题(支持正则搜索)',
                   }),
    )
    # a = forms.CheckboxInput()