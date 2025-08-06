from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from collections import Counter
from datetime import datetime

def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    product_counter = Counter()
    date_counter = Counter()

    filas = []

    for post in posts.values():
        product_id = post.get("productID")
        date_str = post.get("date")

        dia = ""
        hora = ""

        if product_id:
            product_counter[product_id] += 1

        if date_str:
            try:
                dt = datetime.fromisoformat(date_str.replace("Z", ""))
                dia = dt.strftime("%Y-%m-%d")   # Formato: 2025-06-12
                hora = dt.strftime("%H:%M")     # Formato: 01:40
                date_counter[dia] += 1
            except Exception as e:
                print(f"Fecha inválida: {date_str}")

        filas.append({
            "dia": dia,
            "hora": hora,
            "productID": product_id,
        })

    most_common_product = product_counter.most_common(1)[0] if product_counter else ("N/A", 0)
    least_common_product = product_counter.most_common()[-1] if product_counter else ("N/A", 0)
    most_common_day = date_counter.most_common(1)[0] if date_counter else ("N/A", 0)

    producto_labels = list(product_counter.keys())
    producto_valores = list(product_counter.values())

    data = {
        'title': "Landing Page Dashboard",
        'total_responses': total_responses,
        'most_common_product': most_common_product[0],
        'most_common_product_count': most_common_product[1],
        'least_common_product': least_common_product[0],
        'least_common_product_count': least_common_product[1],
        'most_common_day': most_common_day[0],
        'most_common_day_count': most_common_day[1],
        'filas': filas,
        'producto_labels': producto_labels,
        'producto_valores': producto_valores,
    }

    return render(request, 'dashboard/index.html', data)