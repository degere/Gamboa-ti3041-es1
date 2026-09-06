from django.shortcuts import render
from django.http import Http404

productos = [
    {"id": 1, "nombre": "Martillo", "categoria": "Herramientas", "precio": 12.50, "stock": 15, "imagen": "1.jpg"},
    {"id": 2, "nombre": "Destornillador", "categoria": "Herramientas", "precio": 8.90, "stock": 0, "imagen": "2.jpg"},
    {"id": 3, "nombre": "Taladro", "categoria": "Electricidad", "precio": 45.00, "stock": 7, "imagen": "3.jpg"},
    {"id": 4, "nombre": "Sierra circular", "categoria": "Electricidad", "precio": 60.20, "stock": 3, "imagen": "4.jpg"},
    {"id": 5, "nombre": "Llave ajustable", "categoria": "Herramientas", "precio": 15.30, "stock": 10, "imagen": "5.jpg"},
    {"id": 6, "nombre": "Pinza", "categoria": "Herramientas", "precio": 7.40, "stock": 20, "imagen": "6.jpg"},
    {"id": 7, "nombre": "Cinta métrica", "categoria": "Medición", "precio": 5.60, "stock": 25, "imagen": "7.jpg"},
    {"id": 8, "nombre": "Nivel", "categoria": "Medición", "precio": 18.90, "stock": 0, "imagen": "8.jpg"},
    {"id": 9, "nombre": "Lijadora", "categoria": "Electricidad", "precio": 32.10, "stock": 5, "imagen": "9.jpg"},
    {"id": 10, "nombre": "Pintura blanca 1L", "categoria": "Pintura", "precio": 9.99, "stock": 30, "imagen": "10.jpg"},
    {"id": 11, "nombre": "Pintura azul 1L", "categoria": "Pintura", "precio": 10.50, "stock": 12, "imagen": "11.jpg"},
    {"id": 12, "nombre": "Rodillo", "categoria": "Pintura", "precio": 4.20, "stock": 40, "imagen": "12.jpg"},
    {"id": 13, "nombre": "Brocas para metal", "categoria": "Accesorios", "precio": 6.80, "stock": 18, "imagen": "13.jpg"},
    {"id": 14, "nombre": "Brocas para madera", "categoria": "Accesorios", "precio": 7.30, "stock": 0, "imagen": "14.jpg"},
    {"id": 15, "nombre": "Cerradura", "categoria": "Seguridad", "precio": 22.00, "stock": 8, "imagen": "15.jpg"},
    {"id": 16, "nombre": "Perno M8", "categoria": "Ferretería", "precio": 0.50, "stock": 200, "imagen": "16.jpg"},
    {"id": 17, "nombre": "Tuerca M8", "categoria": "Ferretería", "precio": 0.30, "stock": 150, "imagen": "17.jpg"},
    {"id": 18, "nombre": "Arandela", "categoria": "Ferretería", "precio": 0.10, "stock": 500, "imagen": "18.jpg"},
    {"id": 19, "nombre": "Lámpara LED", "categoria": "Electricidad", "precio": 15.00, "stock": 0, "imagen": "19.jpg"},
    {"id": 20, "nombre": "Cable eléctrico 10m", "categoria": "Electricidad", "precio": 12.30, "stock": 20, "imagen": "20.jpg"},
    {"id": 21, "nombre": "Enchufe", "categoria": "Electricidad", "precio": 3.20, "stock": 45, "imagen": "21.jpg"},
    {"id": 22, "nombre": "Interruptor", "categoria": "Electricidad", "precio": 4.50, "stock": 33, "imagen": "22.jpg"},
    {"id": 23, "nombre": "Cinta aislante", "categoria": "Electricidad", "precio": 1.80, "stock": 60, "imagen": "23.jpg"},
    {"id": 24, "nombre": "Serrucho", "categoria": "Herramientas", "precio": 14.20, "stock": 6, "imagen": "24.jpg"},
    {"id": 25, "nombre": "Formón", "categoria": "Herramientas", "precio": 9.90, "stock": 0, "imagen": "25.jpg"},
    {"id": 26, "nombre": "Cepillo", "categoria": "Herramientas", "precio": 11.00, "stock": 9, "imagen": "26.jpg"},
    {"id": 27, "nombre": "Soplete", "categoria": "Herramientas", "precio": 27.50, "stock": 4, "imagen": "27.jpg"},
    {"id": 28, "nombre": "Manguera 15m", "categoria": "Jardín", "precio": 19.80, "stock": 11, "imagen": "28.jpg"},
    {"id": 29, "nombre": "Regadera", "categoria": "Jardín", "precio": 8.40, "stock": 0, "imagen": "29.jpg"},
    {"id": 30, "nombre": "Tijeras de podar", "categoria": "Jardín", "precio": 13.60, "stock": 7, "imagen": "30.jpg"},
    {"id": 31, "nombre": "Guantes de trabajo", "categoria": "Seguridad", "precio": 5.90, "stock": 22, "imagen": "31.jpg"},
    {"id": 32, "nombre": "Gafas de seguridad", "categoria": "Seguridad", "precio": 6.70, "stock": 14, "imagen": "32.jpg"},
    {"id": 33, "nombre": "Mascarilla", "categoria": "Seguridad", "precio": 2.30, "stock": 30, "imagen": "33.jpg"},
    {"id": 34, "nombre": "Extensión eléctrica 5m", "categoria": "Electricidad", "precio": 10.20, "stock": 0, "imagen": "34.jpg"},
    {"id": 35, "nombre": "Foco", "categoria": "Electricidad", "precio": 4.10, "stock": 18, "imagen": "35.jpg"},
    {"id": 36, "nombre": "Cinta de teflón", "categoria": "Ferretería", "precio": 0.90, "stock": 50, "imagen": "36.jpg"},
    {"id": 37, "nombre": "Pegamento instantáneo", "categoria": "Ferretería", "precio": 3.70, "stock": 15, "imagen": "37.jpg"},
    {"id": 38, "nombre": "Lija", "categoria": "Ferretería", "precio": 1.20, "stock": 40, "imagen": "38.jpg"},
    {"id": 39, "nombre": "Candado", "categoria": "Seguridad", "precio": 8.80, "stock": 12, "imagen": "39.jpg"},
    {"id": 40, "nombre": "Cadena", "categoria": "Ferretería", "precio": 6.30, "stock": 0, "imagen": "40.jpg"},
]

def lista(request):
    total = len(productos)
    disponibles = sum(1 for p in productos if p['stock'] > 0)
    context = {
        'productos': productos,
        'total': total,
        'disponibles': disponibles,
    }
    return render(request, 'catalogo/lista.html', context)

def detalle(request, id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto is None:
        raise Http404("Producto no encontrado")
    return render(request, 'catalogo/detalle.html', {'producto': producto})