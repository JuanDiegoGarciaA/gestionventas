from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto
    if request.method =='POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email_message=EmailMessage(
                "Mensaje desde App Django",
                "El usuario con nombre {} con la direccion de correo {} escribe lo siguiente: \n \n {}".format(nombre, email, contenido),
                "", 
                ["jdiegogarcia0110@gmail.com"],
                reply_to=[email])
            
            try:
                email_message.send()
                return redirect("/contacto/?valido")
            except:               
                return redirect("/contacto/?novalido")
            
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})