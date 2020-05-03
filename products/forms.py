from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='',
                    widget= forms.TextInput( attrs = {'placeholder':"Your Title"}))
            
    description = forms.CharField(
                    required=False, 
                    label = '',
                    widget=forms.Textarea(
                        attrs={
                            'class': "new-class-name two",
                            'id': "my_id_for_text",
                            'rows': 10,
                            'cols':100,
                            'placeholder':"Your Description",
                        }
                    )
                )

    price       = forms.DecimalField(label = '', initial=1.00 )
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    #def clean_<my_field_name>
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     # if not "FTV" in title:
    #     #     raise forms.ValidationError('this is not a valid title')
    #     return title

    

class RawProductForm(forms.Form):
    title       = forms.CharField(label='',
                                widget= forms.TextInput( attrs = {'placeholder':"Your Title"}))
    description = forms.CharField(
                        required=False, 
                        label = '',
                        widget=forms.Textarea(
                            attrs={
                                'class': "new-class-name two",
                                'id': "my_id_for_text",
                                'rows': 10,
                                'cols':100,
                                'placeholder':"Your Description",
                            }
                        )
                    )

    price       = forms.DecimalField(label = '', initial=1.00 )
                                

