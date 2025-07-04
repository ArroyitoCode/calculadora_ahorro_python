def pedir_numero_positivo (mensaje):
    while True:
        dato = input(mensaje)
        if dato.replace('.', '', 1).isdigit() and float(dato) >= 0:
            return float(dato)
        print("⚠️ Ingresa un número válido y positivo.")

def calculadora_ahorro():
    ingreso = pedir_numero_positivo("💰 Ingreso mensual: ")
    gasto_vivienda = pedir_numero_positivo("🏠 Gasto en vivienda: ")
    gasto_transporte = pedir_numero_positivo("🚗 Gasto en transporte: ")
    gasto_alimentos = pedir_numero_positivo("🍽️ Gasto en alimentos: ")
    otros = pedir_numero_positivo ("📦 Otros gastos: ")
    
    total_gastos = gasto_vivienda + gasto_transporte + gasto_alimentos + otros
    ahorro = ingreso - total_gastos
    
    print(f"\n🔎 Total de gastos: ${total_gastos:.2f}")
    print(f"💸 Ahorro estimado: ${ahorro:.2f}")
    
    if ahorro < 0:
        print("🚨 Estás gastando más de lo que ganas. Revisa tus gastos.")
    elif ahorro < ingreso * 0.2:
        print("📉 Ahorro bajo. Intenta reducir algunos gastos.")
    else:
        print("✅ ¡Buen trabajo! Tienes un ahorro saludable.")

calculadora_ahorro()
