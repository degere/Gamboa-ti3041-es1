from django.shortcuts import render, get_object_or_404
from django.http import Http404

# json hecho x ia  
productos = [
    {"id": 1, "nombre": "Martillo", "categoria": "Herramientas", "precio": 12.50, "stock": 15},
    {"id": 2, "nombre": "Destornillador", "categoria": "Herramientas", "precio": 8.90, "stock": 0},
    {"id": 3, "nombre": "Taladro", "categoria": "Electricidad", "precio": 45.00, "stock": 7},
    {"id": 4, "nombre": "Sierra circular", "categoria": "Electricidad", "precio": 60.20, "stock": 3},
    {"id": 5, "nombre": "Llave ajustable", "categoria": "Herramientas", "precio": 15.30, "stock": 10},
    {"id": 6, "nombre": "Pinza", "categoria": "Herramientas", "precio": 7.40, "stock": 20},
    {"id": 7, "nombre": "Cinta métrica", "categoria": "Medición", "precio": 5.60, "stock": 25},
    {"id": 8, "nombre": "Nivel", "categoria": "Medición", "precio": 18.90, "stock": 0},
    {"id": 9, "nombre": "Lijadora", "categoria": "Electricidad", "precio": 32.10, "stock": 5},
    {"id": 10, "nombre": "Pintura blanca 1L", "categoria": "Pintura", "precio": 9.99, "stock": 30},
    {"id": 11, "nombre": "Pintura azul 1L", "categoria": "Pintura", "precio": 10.50, "stock": 12},
    {"id": 12, "nombre": "Rodillo", "categoria": "Pintura", "precio": 4.20, "stock": 40},
    {"id": 13, "nombre": "Brocas para metal", "categoria": "Accesorios", "precio": 6.80, "stock": 18},
    {"id": 14, "nombre": "Brocas para madera", "categoria": "Accesorios", "precio": 7.30, "stock": 0},
    {"id": 15, "nombre": "Cerradura", "categoria": "Seguridad", "precio": 22.00, "stock": 8},
    {"id": 16, "nombre": "Perno M8", "categoria": "Ferretería", "precio": 0.50, "stock": 200},
    {"id": 17, "nombre": "Tuerca M8", "categoria": "Ferretería", "precio": 0.30, "stock": 150},
    {"id": 18, "nombre": "Arandela", "categoria": "Ferretería", "precio": 0.10, "stock": 500},
    {"id": 19, "nombre": "Lámpara LED", "categoria": "Electricidad", "precio": 15.00, "stock": 0},
    {"id": 20, "nombre": "Cable eléctrico 10m", "categoria": "Electricidad", "precio": 12.30, "stock": 20},
    {"id": 21, "nombre": "Enchufe", "categoria": "Electricidad", "precio": 3.20, "stock": 45},
    {"id": 22, "nombre": "Interruptor", "categoria": "Electricidad", "precio": 4.50, "stock": 33},
    {"id": 23, "nombre": "Cinta aislante", "categoria": "Electricidad", "precio": 1.80, "stock": 60},
    {"id": 24, "nombre": "Serrucho", "categoria": "Herramientas", "precio": 14.20, "stock": 6},
    {"id": 25, "nombre": "Formón", "categoria": "Herramientas", "precio": 9.90, "stock": 0},
    {"id": 26, "nombre": "Cepillo", "categoria": "Herramientas", "precio": 11.00, "stock": 9},
    {"id": 27, "nombre": "Soplete", "categoria": "Herramientas", "precio": 27.50, "stock": 4},
    {"id": 28, "nombre": "Manguera 15m", "categoria": "Jardín", "precio": 19.80, "stock": 11},
    {"id": 29, "nombre": "Regadera", "categoria": "Jardín", "precio": 8.40, "stock": 0},
    {"id": 30, "nombre": "Tijeras de podar", "categoria": "Jardín", "precio": 13.60, "stock": 7},
    {"id": 31, "nombre": "Guantes de trabajo", "categoria": "Seguridad", "precio": 5.90, "stock": 22},
    {"id": 32, "nombre": "Gafas de seguridad", "categoria": "Seguridad", "precio": 6.70, "stock": 14},
    {"id": 33, "nombre": "Mascarilla", "categoria": "Seguridad", "precio": 2.30, "stock": 30},
    {"id": 34, "nombre": "Extensión eléctrica 5m", "categoria": "Electricidad", "precio": 10.20, "stock": 0},
    {"id": 35, "nombre": "Foco", "categoria": "Electricidad", "precio": 4.10, "stock": 18},
    {"id": 36, "nombre": "Cinta de teflón", "categoria": "Ferretería", "precio": 0.90, "stock": 50},
    {"id": 37, "nombre": "Pegamento instantáneo", "categoria": "Ferretería", "precio": 3.70, "stock": 15},
    {"id": 38, "nombre": "Lija", "categoria": "Ferretería", "precio": 1.20, "stock": 40},
    {"id": 39, "nombre": "Candado", "categoria": "Seguridad", "precio": 8.80, "stock": 12},
    {"id": 40, "nombre": "Cadena", "categoria": "Ferretería", "precio": 6.30, "stock": 0},
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
    # Buscar producto por id
    producto = next((p for p in productos if p['id'] == id), None)
    if producto is None:
        raise Http404("Producto no encontrado")
    return render(request, 'catalogo/detalle.html', {'producto': producto})