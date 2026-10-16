#VERSION 2
# ================================================================
# SISTEMA DE MANTENIMIENTO PREDICTIVO PARA MOTORES ELÉCTRICOS
# MVP - PRIMERA VERSIÓN
# ================================================================

"""
PAROMPT UTILIZADO PARA EL DESARROLLO:

Analiza el documento adjunto y, respetando estrictamente su alcance,
restricciones, entradas, procesamiento, salidas y criterios de prueba,
desarrolla el código principal completo y funcional del MVP en Python
para el sistema de mantenimiento predictivo de motores eléctricos.

En esta primera versión analiza únicamente corriente y temperatura.
Los valores válidos de entrada serán: corriente de 0 A a 5 A y
temperatura de 0 °C a 110 °C. Si alguna medición es exactamente 0,
el sistema la tratará como posible error de sensor y recomendará revisarlo.

Límites de clasificación:

CORRIENTE:
0–1.5 A       -> Normal baja
1.5–2.0 A     -> Normal
2.0–2.5 A     -> Advertencia
>2.5 A        -> Posible sobrecarga/falla

TEMPERATURA:
<40 °C        -> Normal
40–60 °C      -> Normal elevada
60–70 °C      -> Advertencia
>70 °C        -> Posible sobrecalentamiento

El código debe ser sencillo, modular y basado en funciones propias,
sin librerías externas ni frameworks. Debe seguir el flujo:

Entrada → Validación → Análisis → Clasificación → Alertas
→ Recomendación → Resultados

Debe permitir posteriormente incorporar vibración y sonido sin
modificar toda la estructura.

Implementa validación robusta en cada entrada y opción del menú.
Si el usuario ingresa texto, vacío, formato incorrecto, un valor
fuera del rango permitido o una opción inexistente, el programa
debe mostrar claramente el error, indicar las opciones o rangos
válidos y solicitar nuevamente el dato hasta recibir una entrada
correcta.

Incluye un menú principal, ingreso de datos simulados y escenarios
de prueba para condiciones normales, límites, advertencias,
posibles fallas, combinación de riesgos y datos inválidos.

Muestra los valores analizados, estado del motor, nivel de riesgo,
alertas y recomendación básica de mantenimiento.

No agregues funcionalidades fuera del alcance del documento, como
sensores físicos, PLC, IA avanzada, predicción exacta de fallas
o integración industrial.
"""


# ================================================================
# 1. CONSTANTES
# ================================================================

# Rangos válidos para ingresar datos al software
CORRIENTE_MIN = 0.0
CORRIENTE_MAX = 5.0

TEMPERATURA_MIN = 0.0
TEMPERATURA_MAX = 110.0


# ================================================================
# 2. VALIDACIÓN DE DATOS
# ================================================================

def solicitar_corriente():
    """
    Solicita una corriente entre 0 y 5 A; una lectura cero se marca como posible error de medición.
    Repite la solicitud si el usuario comete un error.
    """

    while True:
        entrada = input(
            f"Ingrese la corriente del motor ({CORRIENTE_MIN} a "
            f"{CORRIENTE_MAX} A): "
        ).strip()

        if entrada == "":
            print("ERROR: No puede dejar el campo vacío.")
            continue

        try:
            corriente = float(entrada)

            if corriente < CORRIENTE_MIN or corriente > CORRIENTE_MAX:
                print(
                    f"ERROR: La corriente debe estar entre "
                    f"{CORRIENTE_MIN} A y {CORRIENTE_MAX} A."
                )
                continue

            return corriente

        except ValueError:
            print("ERROR: Debe ingresar un valor numérico válido.")


def solicitar_temperatura():
    """
    Solicita una temperatura entre 0 y 110 °C; una lectura cero se marca como posible error de medición.
    Repite la solicitud si el usuario comete un error.
    """

    while True:
        entrada = input(
            f"Ingrese la temperatura del motor ({TEMPERATURA_MIN} a "
            f"{TEMPERATURA_MAX} °C): "
        ).strip()

        if entrada == "":
            print("ERROR: No puede dejar el campo vacío.")
            continue

        try:
            temperatura = float(entrada)

            if temperatura < TEMPERATURA_MIN or temperatura > TEMPERATURA_MAX:
                print(
                    f"ERROR: La temperatura debe estar entre "
                    f"{TEMPERATURA_MIN} °C y {TEMPERATURA_MAX} °C."
                )
                continue

            return temperatura

        except ValueError:
            print("ERROR: Debe ingresar un valor numérico válido.")


# ================================================================
# 3. ANÁLISIS DE CORRIENTE
# ================================================================

def analizar_corriente(corriente):

    if corriente < 1.5:
        return "Normal baja"

    elif corriente <= 2.0:
        return "Normal"

    elif corriente <= 2.5:
        return "Advertencia"

    else:
        return "Posible sobrecarga/falla"


# ================================================================
# 4. ANÁLISIS DE TEMPERATURA
# ================================================================

def analizar_temperatura(temperatura):

    if temperatura < 40:
        return "Normal"

    elif temperatura <= 60:
        return "Normal elevada"

    elif temperatura <= 70:
        return "Advertencia"

    else:
        return "Posible sobrecalentamiento"


# ================================================================
# 5. CLASIFICACIÓN GENERAL DEL MOTOR
# ================================================================

def clasificar_motor(estado_corriente, estado_temperatura):

    estados_advertencia = [
        "Advertencia",
        "Posible sobrecarga/falla",
        "Posible sobrecalentamiento"
    ]

    falla_corriente = estado_corriente == "Posible sobrecarga/falla"
    falla_temperatura = estado_temperatura == "Posible sobrecalentamiento"

    advertencia_corriente = estado_corriente == "Advertencia"
    advertencia_temperatura = estado_temperatura == "Advertencia"

    # Si alguna variable indica posible falla
    if falla_corriente or falla_temperatura:
        return "POSIBLE FALLA", "ALTO"

    # Si ambas variables están en advertencia
    if advertencia_corriente and advertencia_temperatura:
        return "POSIBLE FALLA", "ALTO"

    # Si una variable está en advertencia
    if estado_corriente in estados_advertencia or \
       estado_temperatura in estados_advertencia:

        return "ADVERTENCIA", "MEDIO"

    # Condición normal
    return "NORMAL", "BAJO"


# ================================================================
# 6. GENERACIÓN DE ALERTAS
# ================================================================

def generar_alertas(estado_corriente, estado_temperatura):

    alertas = []

    if estado_corriente == "Advertencia":
        alertas.append(
            "La corriente se encuentra en un nivel de advertencia."
        )

    elif estado_corriente == "Posible sobrecarga/falla":
        alertas.append(
            "Posible sobrecarga o falla asociada a la corriente."
        )

    if estado_temperatura == "Advertencia":
        alertas.append(
            "La temperatura se encuentra en un nivel de advertencia."
        )

    elif estado_temperatura == "Posible sobrecalentamiento":
        alertas.append(
            "Posible sobrecalentamiento del motor."
        )

    if (
        estado_corriente in ["Advertencia", "Posible sobrecarga/falla"]
        and
        estado_temperatura in ["Advertencia", "Posible sobrecalentamiento"]
    ):
        alertas.append(
            "Se detecta una combinación de variables anormales."
        )

    if len(alertas) == 0:
        alertas.append("No se detectaron condiciones de alarma.")

    return alertas


# ================================================================
# 7. RECOMENDACIONES DE MANTENIMIENTO
# ================================================================

def generar_recomendacion(estado_corriente, estado_temperatura):

    falla_corriente = estado_corriente == "Posible sobrecarga/falla"
    falla_temperatura = estado_temperatura == "Posible sobrecalentamiento"

    advertencia_corriente = estado_corriente == "Advertencia"
    advertencia_temperatura = estado_temperatura == "Advertencia"

    if falla_corriente or falla_temperatura:

        return (
            "Realizar una revisión del motor antes de continuar "
            "con su operación normal. Verificar posibles causas "
            "de sobrecarga o sobrecalentamiento."
        )

    if advertencia_corriente or advertencia_temperatura:

        return (
            "Realizar seguimiento de las variables y programar "
            "una inspección preventiva si la condición persiste."
        )

    if estado_temperatura == "Normal elevada":

        return (
            "Mantener monitoreo de la temperatura y verificar "
            "las condiciones de ventilación del motor."
        )

    return (
        "Continuar con el monitoreo normal del motor y conservar "
        "el registro de las mediciones."
    )


# ================================================================
# 8. ANÁLISIS COMPLETO
# ================================================================

def analizar_motor(corriente, temperatura):
    """Analiza las mediciones y detecta posibles lecturas de sensor en cero."""

    # En este MVP, una lectura exactamente igual a cero se considera
    # una posible falla de medición y no se clasifica como estado del motor.
    if corriente == 0 or temperatura == 0:
        variables_error = []

        if corriente == 0:
            variables_error.append("corriente (0 A)")
        if temperatura == 0:
            variables_error.append("temperatura (0 °C)")

        return {
            "corriente": corriente,
            "temperatura": temperatura,
            "estado_corriente": (
                "Error de medición" if corriente == 0
                else analizar_corriente(corriente)
            ),
            "estado_temperatura": (
                "Error de medición" if temperatura == 0
                else analizar_temperatura(temperatura)
            ),
            "estado_motor": "ERROR DE MEDICIÓN",
            "nivel_riesgo": "NO DETERMINADO",
            "alertas": [
                "Se detectó una medición igual a cero en: "
                + ", ".join(variables_error) + ".",
                "La lectura podría deberse a un sensor desconectado, "
                "una falla de comunicación o un componente que no responde."
            ],
            "recomendacion": (
                "Revisar el sensor correspondiente, sus conexiones, la "
                "alimentación y la comunicación antes de confiar en la medición. "
                "Realizar una nueva lectura después de la revisión."
            )
        }

    estado_corriente = analizar_corriente(corriente)
    estado_temperatura = analizar_temperatura(temperatura)

    estado_motor, nivel_riesgo = clasificar_motor(
        estado_corriente,
        estado_temperatura
    )

    alertas = generar_alertas(
        estado_corriente,
        estado_temperatura
    )

    recomendacion = generar_recomendacion(
        estado_corriente,
        estado_temperatura
    )

    resultado = {
        "corriente": corriente,
        "temperatura": temperatura,
        "estado_corriente": estado_corriente,
        "estado_temperatura": estado_temperatura,
        "estado_motor": estado_motor,
        "nivel_riesgo": nivel_riesgo,
        "alertas": alertas,
        "recomendacion": recomendacion
    }

    return resultado


# ================================================================
# 9. MOSTRAR RESULTADOS
# ================================================================

def mostrar_resultados(resultado):

    print("\n" + "=" * 60)
    print("              RESULTADOS DEL ANÁLISIS")
    print("=" * 60)

    print(f"Corriente:       {resultado['corriente']:.2f} A")
    print(f"Estado corriente: {resultado['estado_corriente']}")

    print(f"Temperatura:     {resultado['temperatura']:.2f} °C")
    print(f"Estado temperatura: {resultado['estado_temperatura']}")

    print("-" * 60)

    print(f"ESTADO DEL MOTOR: {resultado['estado_motor']}")
    print(f"NIVEL DE RIESGO:  {resultado['nivel_riesgo']}")

    print("\nALERTAS:")

    for alerta in resultado["alertas"]:
        print(f"- {alerta}")

    print("\nRECOMENDACIÓN:")
    print(resultado["recomendacion"])

    print("=" * 60)


# ================================================================
# 10. INGRESO MANUAL DE DATOS
# ================================================================

def ingresar_datos():

    print("\n--- INGRESO DE DATOS ---")

    corriente = solicitar_corriente()
    temperatura = solicitar_temperatura()

    return corriente, temperatura


# ================================================================
# 11. DATOS SIMULADOS
# ================================================================

def datos_simulados():

    print("\n--- DATOS SIMULADOS ---")

    escenarios = [
        ("Motor en condición normal", 1.2, 35),
        ("Motor con temperatura elevada", 1.7, 55),
        ("Advertencia de corriente", 2.3, 45),
        ("Advertencia de temperatura", 1.8, 65),
        ("Posible sobrecarga", 2.8, 45),
        ("Posible sobrecalentamiento", 1.5, 80),
        ("Combinación de riesgos", 2.7, 85)
    ]

    for numero, escenario in enumerate(escenarios, start=1):
        print(f"{numero}. {escenario[0]}")

    while True:

        opcion = input(
            f"\nSeleccione un escenario (1-{len(escenarios)}): "
        ).strip()

        try:
            opcion = int(opcion)

            if 1 <= opcion <= len(escenarios):
                _, corriente, temperatura = escenarios[opcion - 1]

                print(f"\nEscenario seleccionado:")
                print(f"Corriente: {corriente} A")
                print(f"Temperatura: {temperatura} °C")

                return corriente, temperatura

            else:
                print(
                    f"ERROR: Seleccione una opción entre 1 y "
                    f"{len(escenarios)}."
                )

        except ValueError:
            print("ERROR: Debe ingresar un número de opción válido.")


# ================================================================
# 12. PRUEBAS DEL SISTEMA
# ================================================================

def ejecutar_pruebas():

    pruebas = [
        ("Caso normal", 1.0, 30),
        ("Límite de corriente normal", 1.5, 35),
        ("Límite de corriente", 2.0, 40),
        ("Advertencia de corriente", 2.3, 45),
        ("Posible falla por corriente", 2.8, 45),
        ("Límite de temperatura normal", 1.5, 40),
        ("Temperatura elevada", 1.5, 55),
        ("Advertencia de temperatura", 1.5, 65),
        ("Posible falla por temperatura", 1.5, 75),
        ("Combinación de riesgos", 2.8, 80)
    ]

    print("\n" + "=" * 60)
    print("              PRUEBAS DEL SISTEMA")
    print("=" * 60)

    for numero, prueba in enumerate(pruebas, start=1):

        nombre, corriente, temperatura = prueba

        print(f"\nPRUEBA {numero}: {nombre}")
        print(f"Corriente: {corriente} A")
        print(f"Temperatura: {temperatura} °C")

        resultado = analizar_motor(corriente, temperatura)

        print(f"Estado: {resultado['estado_motor']}")
        print(f"Riesgo: {resultado['nivel_riesgo']}")

    print("\n" + "=" * 60)
    print("Pruebas finalizadas correctamente.")
    print("=" * 60)


# ================================================================
# 13. HISTORIAL DE MEDICIONES
# ================================================================

def mostrar_historial(historial):

    print("\n" + "=" * 60)
    print("              HISTORIAL DE MEDICIONES")
    print("=" * 60)

    if len(historial) == 0:
        print("No existen mediciones registradas.")
        print("=" * 60)
        return

    for numero, resultado in enumerate(historial, start=1):

        print(f"\nMedición {numero}")
        print(f"Corriente: {resultado['corriente']:.2f} A")
        print(f"Temperatura: {resultado['temperatura']:.2f} °C")
        print(f"Estado: {resultado['estado_motor']}")
        print(f"Riesgo: {resultado['nivel_riesgo']}")

    print("=" * 60)


# ================================================================
# 14. ANÁLISIS DE DATOS Y REGISTRO
# ================================================================

def procesar_medicion(corriente, temperatura, historial):

    resultado = analizar_motor(corriente, temperatura)

    historial.append(resultado)

    mostrar_resultados(resultado)


# ================================================================
# 15. MENÚ PRINCIPAL
# ================================================================

def mostrar_menu():

    print("\n")
    print("=" * 60)
    print("   SISTEMA DE MANTENIMIENTO PREDICTIVO - MVP")
    print("=" * 60)
    print("1. Ingresar datos manualmente")
    print("2. Utilizar datos simulados")
    print("3. Ejecutar pruebas del sistema")
    print("4. Consultar historial")
    print("5. Salir")
    print("=" * 60)


def main():

    historial = []

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":

            corriente, temperatura = ingresar_datos()

            procesar_medicion(
                corriente,
                temperatura,
                historial
            )

        elif opcion == "2":

            corriente, temperatura = datos_simulados()

            procesar_medicion(
                corriente,
                temperatura,
                historial
            )

        elif opcion == "3":

            ejecutar_pruebas()

        elif opcion == "4":

            mostrar_historial(historial)

        elif opcion == "5":

            print("\nSistema finalizado correctamente.")
            break

        else:

            print(
                "\nERROR: Opción no válida. "
                "Seleccione una opción entre 1 y 5."
            )


# ================================================================
# 16. EJECUCIÓN DEL PROGRAMA
# ================================================================

if __name__ == "__main__":
    main()