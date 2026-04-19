from collections import defaultdict

#Carga de Datos: Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta

ventas = [
    {"fecha": "2024-01-01", "producto": "Computador", "cantidad": 2, "precio": 259000.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 10000.0},
    {"fecha": "2024-01-02", "producto": "Computador", "cantidad": 1, "precio": 360000.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 25000.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 4, "precio": 10000.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 1, "precio": 120000.0},
]

#Cálculo de Ingresos Totales: Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]


#Análisis del Producto Más Vendido:
#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = defaultdict(int)
for venta in ventas:
    ventas_por_producto[venta["producto"]] += venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

#Promedio de Precio por Producto:
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
precios_por_producto = defaultdict(lambda: (0.0, 0))
for venta in ventas:
    prod = venta["producto"]
    ingresos_venta = venta["cantidad"] * venta["precio"]
    suma_actual, cant_actual = precios_por_producto[prod]
    precios_por_producto[prod] = (suma_actual + ingresos_venta, cant_actual + venta["cantidad"])

precio_promedio_por_producto = {}
for prod, (suma_ingresos, cant_total) in precios_por_producto.items():
    promedio = suma_ingresos / cant_total if cant_total > 0 else 0
    precio_promedio_por_producto[prod] = promedio

#Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
ingresos_por_dia = defaultdict(float)
for venta in ventas:
    ingresos_por_dia[venta["fecha"]] += venta["cantidad"] * venta["precio"]

#Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.
resumen_ventas = {}
for prod in ventas_por_producto.keys():
    cantidad_total = ventas_por_producto[prod]
    ingresos_totales_prod = precios_por_producto[prod][0]  # suma de ingresos
    precio_promedio = precio_promedio_por_producto[prod]
    resumen_ventas[prod] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_prod,
        "precio_promedio": round(precio_promedio, 2)
    }

output_lines = []

output_lines.append("=== ANÁLISIS DE VENTAS ===")
output_lines.append("\n1. LISTA ORIGINAL DE VENTAS:")
for i, venta in enumerate(ventas, 1):
    output_lines.append(f"   Venta {i}: {venta}")

output_lines.append(f"\n2. INGRESOS TOTALES GENERADOS: ${ingresos_totales:,.2f}")

output_lines.append(f"\n3. PRODUCTO MÁS VENDIDO:")
output_lines.append(f"   Producto: {producto_mas_vendido}, Cantidad total vendida: {cantidad_mas_vendida}")

output_lines.append("\n4. PRECIO PROMEDIO DE VENTA POR PRODUCTO:")
for prod, prom in precio_promedio_por_producto.items():
    output_lines.append(f"   {prod}: ${prom:.2f}")

output_lines.append("\n5. INGRESOS TOTALES POR DÍA:")
for fecha in sorted(ingresos_por_dia.keys()):
    output_lines.append(f"   {fecha}: ${ingresos_por_dia[fecha]:,.2f}")

output_lines.append("\n6. RESUMEN DE VENTAS POR PRODUCTO (diccionario anidado):")
for prod, datos in resumen_ventas.items():
    output_lines.append(f"   {prod}: {datos}")

print("\n".join(output_lines))