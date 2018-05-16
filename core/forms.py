from django import forms

class ComentarioForm(forms.Form):
    comentario = forms.CharField(label='', help_text='', widget=forms.Textarea(attrs={'width':"100%", 'cols' : "40", 'rows': "2"}))

class BuscarForm(forms.Form):
    texto = forms.CharField(max_length=20, help_text='')

class ContactoForm(forms.Form):
    email = forms.EmailField()
    nombre = forms.CharField(max_length=20, help_text='')
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "40", 'rows': "2"}))

class ResponderForm(forms.Form):
    respuesta = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "40", 'rows': "2"}))