from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact

# Create your views here.
def contact(request):
    #print('tipo de peticion: {}'.format(request.method))
    form= ContactForm()
    #if request.method == 'POST':
    #    print(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            contacto= Contact()
            contacto.nombre=form.cleaned_data['nombre']
            contacto.apellido=form.cleaned_data['apellido']
            contacto.email=form.cleaned_data['email']
            contacto.celular=form.cleaned_data['celular']
            contacto.comentario=form.cleaned_data['comentario']
            contacto.save()

            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('Invalido')

    return render(request,'contact/contact.html',{'form':form})

