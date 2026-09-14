from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.conf import settings

BACKEND_URL = settings.BACKEND_API_URL

def index(request):
    print(f'spuštění backendu API at {BACKEND_URL}')
    
    try:
        api_response = requests.get(BACKEND_URL)
        print('spuštěnbí TRY metody')
        
        if api_response.status_code == 200:
            print('spuštění if metody')

            context = {
                'nazev': 'Nákupní seznam',
            }
            return render(request, 'index.html', context)




            
        else:
            return HttpResponse(f"Backend vrátil chybu: {api_response.status_code}")

    except requests.exceptions.ConnectionError:
        return HttpResponse("Nepodařilo se připojit k backendu. Běží atarax_backend?")