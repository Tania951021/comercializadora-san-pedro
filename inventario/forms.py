from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:

        model = Producto

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),

            'fecha_ingreso': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),

        }

    # Validación de precio
    def clean_precio(self):

        precio = self.cleaned_data.get('precio')

        if precio < 0:

            raise forms.ValidationError(
                'El precio no puede ser negativo'
            )

        return precio