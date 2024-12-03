# Preguntas y respuestas correctas
preguntas = [
    "1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.\n    a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO",
    "2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.\n    a) Información     b) Datos     c) Programa     d) Código",
    "3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.\n    a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode",
    "4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.\n    a) Proceso     b) Solución     c) Función     d) Algoritmo",
    "5. Conjunto de elementos que se relacionan para cumplir una función determinada.\n    a) Estructura     b) Datos     c) Operación     d) Sistema",
    "6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.\n    a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete",
    "7. Elemento que se usa para almacenar una cantidad donde cambia su valor.\n    a) Constante     b) Variable     c) Librería     d) Tipo de Dato",
    "8. Conjunto de símbolos, letras, números que no tienen un significado.\n    a) Datos     b) Estructura     c) Información     d) Sistema",
    "9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.\n    a) Filosofía     b) Sociología     c) Lógica     d) Argumentación",
    "10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.\n    a) Evento     b) Estándar     c) Calidad     d) Productividad",
    "11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.\n    a) Estructura     b) Sistema     c) Objeto     d) Virtual",
    "12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.\n    a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando"
]

respuestas_correctas = ["b", "a", "c", "d", "d", "d", "b", "a", "c", "b", "a", "c"]

# Variables para almacenar las respuestas del usuario y los aciertos
respuestas_usuario = []
aciertos = 0

# Iterar sobre las preguntas
for i in range(len(preguntas)):
    print(preguntas[i])
    respuesta = input("Tu respuesta: ").lower()
    respuestas_usuario.append(respuesta)
    if respuesta == respuestas_correctas[i]:
        aciertos += 1

# Calcular calificación
calificacion = (aciertos / 12) * 10

# Mostrar resultados
print(f"\nRespuestas correctas: {aciertos}/12")
print(f"Tu calificación es: {calificacion:.2f}")
