from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.conf import settings

BACKEND_URL = settings.BACKEND_API_URL
API_CON_OK = "PROPOJENÍ API = OK"
API_DATA_OK = "PŘÍJEM DAT API = OK"

def index(request):
    print(f'spuštění backendu API at {BACKEND_URL}')
    
    try:
        api_response = requests.get(BACKEND_URL)
        print(API_CON_OK)
        
        if api_response.status_code == 200:
            print(API_DATA_OK)

            return render(request, 'app_dm_frontend/index.html')
            
        else:
            return HttpResponse(f"Backend vrátil chybu: {api_response.status_code}")

    except requests.exceptions.ConnectionError:
        return HttpResponse("Nepodařilo se připojit k backendu. Běží atarax_backend?")

def maps(request):

    try:
        api_response = requests.get(BACKEND_URL + "/maps")
        print(f"MAPY: {API_CON_OK}")
        
        if api_response.status_code == 200:
            print(f"MAPY: {API_DATA_OK}")

            data = api_response.json()
            
            context = {
                'continents': data.get('continents', []),
                'kingdoms': data.get('kingdoms', []),
                'regions': data.get('regions', []),
                'cities': data.get('cities', []),
                'dungeons': data.get('dungeons', []),
                'unique_locations': data.get('unique_locations', [])
            }
            
            return render(request, 'app_dm_frontend/maps.html', context)
            
        else:
            return HttpResponse(f"Backend vrátil chybu: {api_response.status_code}")

    except requests.exceptions.ConnectionError:
        return HttpResponse("Nepodařilo se připojit k backendu. Běží atarax_backend?")

def maps_detail(request, name):
    print(f'spuštění map_detail s parametrem {name}')

# PTÁM SE TORCHU NEEFEKTIVNĚ NA VŠECHNY MAPY V DATABÁZI ALE SERVER JE DOST RYCHLÝ ABY TO ZVLÁDL

    try:
        api_response = requests.get(BACKEND_URL + "/maps")
        print(f"MAPY: {API_CON_OK}")
        
        if api_response.status_code == 200:
            print(f"MAPY: {API_DATA_OK}")

            data = api_response.json()
            
            for item in data.get('kingdoms', []) + data.get('continents', []) + data.get('regions', []) + data.get('cities', []) + data.get('dungeons', []) + data.get('unique_locations', []):
                if item.get('name') == name:
                    return render(request, 'app_dm_frontend/maps_detail.html', {'item': item})

            return HttpResponse(f"Mapa '{name}' nebyla nalezena ve všech kategoriích.")
            
        else:
            return HttpResponse(f"Backend vrátil chybu: {api_response.status_code}")

    except requests.exceptions.ConnectionError:
        return HttpResponse("Nepodařilo se připojit k backendu. Běží atarax_backend?")


def npc(request):
    print('spuštění metody npc')
    return render(request, 'app_dm_frontend/npc.html')

def diary(request):
    print('spuštění metody diary')
    return render(request, 'app_dm_frontend/diary.html')

def glem(request):
    print('spuštění metody glem')
    return render(request, 'app_dm_frontend/glem.html')

def notes(request):
    print('spuštění metody notes')
    return render(request, 'app_dm_frontend/notes.html')

def chronicle(request):
    print('spuštění metody chronicle')
    return render(request, 'app_dm_frontend/chronicle.html')