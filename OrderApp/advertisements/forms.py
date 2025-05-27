from django import forms
from .models import Advertisement


class AdsFormCreations(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'condition', 'image', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
