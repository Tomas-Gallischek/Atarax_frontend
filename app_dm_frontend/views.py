from django.shortcuts import render
import requests
from django.http import HttpResponse

def index(request):
    backend_url = 'http://127.0.0.1:8000/api/ziskej-data/' 

    try:
        odpoved = requests.get(backend_url)
        
        if odpoved.status_code == 200:
            data = odpoved.json() 
            data_list = data.get("data", [])

            return HttpResponse(f"Úspěšně přijato z backendu: {data_list}")
        else:
            return HttpResponse(f"Backend vrátil chybu: {odpoved.status_code}")

    except requests.exceptions.ConnectionError:
        return HttpResponse("Nepodařilo se připojit k backendu. Běží atarax_backend?")