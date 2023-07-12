from django import forms

class ContactForm(forms.Form):
    nombre= forms.CharField(label='Nombre', required=True, min_length=5,max_length=25, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre'}))
    apellido= forms.CharField(label='Apellido', required=True, min_length=5,max_length=25, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'apellido'}))
    email=forms.EmailField(label='Correo Electronico', required=True, max_length=33, widget= forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ej: email@email.com'}))
    celular=forms.IntegerField(label='celular' ,required=True, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'celular'}))
    comentario=forms.CharField(label='comentario', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'comentario', 'row':5}))