from django.shortcuts import render

# Create your views here.
import os
import subprocess
from django.http import JsonResponse

def listar_archivos(request):
    ruta = "/home"  # Ruta del sistema donde listar archivos
    archivos = os.listdir(ruta)
    return JsonResponse({"archivos": archivos})

def ejecutar_comando(request):
    comando = "ls -l"  # Comando de Linux
    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        return JsonResponse({"resultado": resultado})
    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": str(e)}, status=400)
