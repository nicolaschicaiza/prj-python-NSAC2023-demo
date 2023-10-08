import os
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Notebook
from papermill import execute_notebook

# Create your views here.


class NotebookView(viewsets.ModelViewSet):
    pass

    @action(detail=False, methods=["POST"])
    def execute_notebook_endpoint(request):
        # Obtén los datos de entrada desde la solicitud POST
        data = request.POST.get('data', '')

        # Define la ubicación de la plantilla del notebook
        notebook_template = 'ruta/a/la/plantilla_del_notebook.ipynb'

        # Define la ubicación donde se guardará el notebook ejecutado
        output_notebook = 'ruta/donde/guardar/el/notebook_ejecutado.ipynb'

        # Utiliza Papermill para ejecutar el notebook con los datos
        try:
            execute_notebook(notebook_template, output_notebook,
                             parameters={'data': data})

            # Elimina el notebook ejecutado después de la ejecución
            os.remove(output_notebook)

            return Response({"message": "El notebook se ejecutó con éxito y se eliminó."})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
