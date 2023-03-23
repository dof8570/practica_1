from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y la hora actual.
init_time = datetime.now()

print (f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
# Cantidad de resultados correctos
correctos = 0
for i in range (0, times):
    # Se eligen numeros y operador al azar
    number_1 = randrange (10)
    number_2 = randrange (10)
    operator = choice(operators)
    # Se evita la division por cero reseleccionando number_2
    if operator == "/" and number_2 == 0:
        while number_2 == 0:
            number_2 = randrange(10)
    # Se imprime la cuenta.
    print (f"{i+1}- ¿Cuanto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    # Se obtiene el resultado correcto de la operacion
    if operator == "+":
        resultado_operacion = number_1 + number_2
    elif operator == "-":
        resultado_operacion = number_1 - number_2
    elif operator == "*":
        resultado_operacion = number_1 * number_2
    else:
        resultado_operacion =number_1 / number_2
    # Comparamos el resultado del usuario con el correcto
    # Se informa si es correcto o incorrecto y actualiza el contador de correctas
    if round(resultado_operacion, 2) == round(float(result), 2):
       print("El resultado es correcto")
       correctos+=1
    else:
        print("El resultado es incorrecto")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos y las respuestas correctas e incorrectas.
print(f"\n Tardaste {total_time.seconds} segundos\n tenes {correctos} respuestas correctas y {5 - correctos} respuestas incorrectas")