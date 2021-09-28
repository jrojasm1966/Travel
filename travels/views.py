from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime, localtime
from datetime import datetime
from login.models import User
from travels.models import Travel
# Create your views here.

def travels(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    MisTravels = Travel.objects.filter(usuario = reg_user)
    # Query directa con JOIN Buscar Viajes de otros usuarios.
    OtrosTravels = Travel.objects.raw(
        "SELECT a.id, a.destino, a.descripcion, a.fechaDesde, a.fechaHasta, b.nombre FROM travels_travel a JOIN login_user b ON a.usuario_id = b.id and b.id not in (" + str(request.session['user_id']) + ") order BY b.id"
        )

    context = {
        "active_user": reg_user,
        "MisTravels": MisTravels,
        "OtrosTravels": OtrosTravels,
    }    
    return render(request,'index.html', context)

def ingresatravel(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    context = {
        "active_user": reg_user,
    }    
    return render(request, 'CrearTravel.html', context)

def despliegatravels(request):
    travels = Travel.objects.all()

    context = {
        'lista_travels': travels,
    }
    return render(request, 'index.html', context)

def createtravel(request):
    #validacion de parametros
    errors = Travel.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return render(request, 'CrearTravel.html')
    else:
        reg_user = User.objects.get(id=request.session['user_id'])
        
        travels = Travel(
                    destino= request.POST['destino'],
                    descripcion = request.POST['descripcion'], 
                    fechaDesde = request.POST['fechades'], 
                    fechaHasta = request.POST['fechahas'], 
                    estado = 0,
                    usuario = reg_user, 
                    created_at = localtime,
                    updated_at = localtime
                    )
        travels.save()
        return redirect('/travels')

def capturatravel(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    leertravel = Travel.objects.get(id=request.POST['travelid'])

    # Query directa con JOIN Buscar Viajes de otros usuarios.
    OtrosUserTravel = User.objects.raw("SELECT a.id, a.nombre FROM login_user a JOIN travels_travel b ON a.id <> b.usuario_id and a.id not in (" + str(request.session['user_id']) + ") GROUP BY a.id")

    context = {
        "active_user": reg_user,
        'leertravel': leertravel,
        'OtrosUserTravel': OtrosUserTravel,
    }
    return render(request,'EditarTravel.html', context)

def updatetravel(request):
    reg_user = User.objects.get(id=request.session['user_id'])
    leertravel = Travel.objects.get(id=request.POST['travelid'])

    validaTravels = Travel.objects.filter(
        usuario = reg_user,
        destino= request.POST['destino'],
        descripcion = request.POST['descripcion'] 
        )

    if validaTravels.count() > 0:
            messages.error(request, "Usuario ya está en éste viaje !!")
            return redirect('/travels')
        
    
    travels = Travel(destino = leertravel.destino, descripcion = leertravel.descripcion, 
                fechaDesde = leertravel.fechaDesde, fechaHasta = leertravel.fechaHasta, 
                estado = 0,usuario = reg_user, created_at = localtime, updated_at = localtime
                )
    travels.save()

    return redirect('/travels')
