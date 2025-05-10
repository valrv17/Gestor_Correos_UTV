'''
Ejercicio: Validador y Gestor de Correos Electrónicos para Biblioteca Universitaria

Contexto:
La biblioteca de la Universidad Tecnológica del Valle ha decidido mejorar el manejo de la comunicación con sus usuarios. Para ello, necesita una aplicación sencilla de consola que permita registrar, validar y administrar direcciones de correo electrónico de estudiantes y docentes.

Descripción del Ejercicio:
En equipos de 2 a 3 personas, desarrollarán una aplicación de consola en Python que cumpla con los siguientes requisitos:

📌 Requisitos de la Aplicación:
Menú principal:

- Registrar un nuevo correo electrónico.
- Ver correos registrados.
- Buscar un correo específico.
- Salir de la aplicación.


Registro de correos electrónicos:

- Solicitar al usuario que ingrese una dirección de correo electrónico.
- Validar la dirección usando una expresión regular sencilla.
- Clasificar automáticamente el correo como 'estudiante' o 'docente', basándose en la estructura del correo:
   • Estudiantes: terminan con "@estudiante.utv.edu.co"
   • Docentes: terminan con "@utv.edu.co"
- Almacenar los correos válidos junto con su clasificación en una colección adecuada.


Visualización de correos registrados:

- Mostrar todos los correos registrados, indicando claramente si pertenecen a un estudiante o a un docente.


Búsqueda de correos específicos:

- Permitir que el usuario ingrese parte o la totalidad de un correo.
- Utilizar ciclos y condicionales para buscar coincidencias dentro de la colección de correos registrados.
- Mostrar todas las coincidencias encontradas.
🔧 Aspectos técnicos obligatorios:
✅ Uso correcto de tipos de datos (strings, booleanos, etc.).
✅ Manejo de condicionales (if-elif-else).
✅ Implementación de ciclos (for o while).
✅ Uso de colecciones (listas o diccionarios).
✅ Manipulación y búsqueda de strings.
✅ Validación mediante expresiones regulares (regex).

📍 Consideraciones adicionales:
La interfaz de consola debe ser amigable y clara.
Manejar adecuadamente los errores y casos especiales (por ejemplo, correo no válido).
Documentar brevemente el código indicando claramente la función de cada sección.

📦 Entregable:
Código fuente de la aplicación (.py).
Una breve explicación (comentarios en el código) sobre cómo resolvieron los puntos solicitados.
'''

# gestor_correos_utv.py
# Aplicación de consola para registrar y gestionar correos de estudiantes y docentes
# Universidad Tecnológica del Valle - Proyecto académico
# Desarrollado en Python 3

# gestor_correos_utv.py
# Sistema Profesional de Gestión de Correos Institucionales
# Universidad Tecnológica del Valle

# gestor_correos_utv.py
# Sistema Profesional de Gestión de Correos Institucionales
# Universidad Tecnológica del Valle

# gestor_correos_utv.py
# Sistema Profesional de Gestión de Correos Institucionales
# Universidad Tecnológica del Valle

import re  # Importamos la librería de expresiones regulares para validar los correos
import os  # Librería para ejecutar comandos del sistema (limpiar pantalla)
import sys  # Librería del sistema (aunque no se usa directamente, podría servir en futuro)
import time  # Librería para pausar la ejecución o esperar un tiempo
from datetime import datetime  # Para obtener la fecha y hora actual

# ----------------------------- CONFIGURACIONES ----------------------------- #

# Expresión regular para validar el formato del correo
REGEX_CORREO = r'^[\w\.-]+@([\w\.-]+)\.\w+$'

# Lista para almacenar los correos registrados
correos_registrados = []

# Diccionario de dominios válidos, asociando cada tipo de usuario con su dominio correspondiente
DOMINIOS_VALIDOS = {
    "Estudiante": "@estudiante.utv.edu.co",
    "Docente": "@utv.edu.co"
}

# ----------------------------- CLASES Y COLORES ----------------------------- #

# Definimos una clase para organizar los colores y formatos de la consola
class Colores:
    OK = '\033[92m'  # Verde (éxito)
    FAIL = '\033[91m'  # Rojo (error)
    INFO = '\033[96m'  # Cian (información)
    WARN = '\033[93m'  # Amarillo (advertencia)
    BOLD = '\033[1m'  # Negrita
    RESET = '\033[0m'  # Restablece formato
    CYAN = '\033[36m'  # Cian
    TITLE = '\033[95m'  # Violeta (título)
    GRIS = '\033[90m'  # Gris

# ----------------------------- UTILIDADES ----------------------------- #

# Función para limpiar la pantalla (dependiendo del sistema operativo)
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para pausar la ejecución y esperar que el usuario presione Enter
def pausar():
    input(f"\n{Colores.INFO}Presione Enter para continuar...{Colores.RESET}")

# Función para imprimir una línea divisoria en la pantalla
def linea_divisoria():
    print(f"{Colores.GRIS}" + "-" * 60 + f"{Colores.RESET}")

# ----------------------------- INTERFAZ ----------------------------- #

# Función para mostrar el encabezado del sistema con título y la fecha actual
def mostrar_encabezado():
    limpiar_pantalla()
    print(f"""{Colores.TITLE}{Colores.BOLD}
╔════════════════════════════════════════════════════╗
║       SISTEMA DE GESTIÓN DE CORREOS UTV            ║
║    Biblioteca - Universidad Tecnológica del Valle  ║
╚════════════════════════════════════════════════════╝{Colores.RESET}""")
    print(f"{Colores.CYAN}Fecha: {datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}{Colores.RESET}\n")

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print(f"""
{Colores.BOLD}MENÚ PRINCIPAL{Colores.RESET}
[1] Registrar un nuevo correo
[2] Ver todos los correos registrados
[3] Buscar un correo por término
[4] Ver estadísticas del sistema
[5] Eliminar un correo existente
[6] Salir del sistema\n""")

# ----------------------------- FUNCIONALIDAD ----------------------------- #

# Función para clasificar el correo según el dominio
def clasificar_correo(correo):
    for tipo, dominio in DOMINIOS_VALIDOS.items():
        if correo.endswith(dominio):
            return tipo  # Retorna el tipo de usuario si el dominio coincide
    return None  # Si no se encuentra un dominio válido, retorna None

# Función para verificar si un correo ya está registrado
def correo_duplicado(correo):
    return any(c['correo'].lower() == correo.lower() for c in correos_registrados)

# Función para registrar un correo nuevo
def registrar_correo():
    correo = input("Ingrese el correo electrónico: ").strip()

    # Validación del formato del correo
    if not re.match(REGEX_CORREO, correo):
        print(f"{Colores.FAIL}Formato inválido. Intente nuevamente.{Colores.RESET}")
        return

    # Verificación de que el correo no esté duplicado
    if correo_duplicado(correo):
        print(f"{Colores.WARN}El correo ya está registrado.{Colores.RESET}")
        return

    # Clasificación del correo según el dominio
    tipo = clasificar_correo(correo)
    if tipo:
        correos_registrados.append({"correo": correo, "tipo": tipo})  # Lo registramos
        print(f"{Colores.OK}Correo registrado como {tipo}.{Colores.RESET}")
    else:
        print(f"{Colores.FAIL}Dominio no reconocido. Solo correos institucionales.{Colores.RESET}")

# Función para ver los correos registrados
def ver_correos():
    if not correos_registrados:
        print(f"{Colores.WARN}No hay correos registrados.{Colores.RESET}")
        return

    # Filtrar los correos por tipo
    estudiantes = [c for c in correos_registrados if c['tipo'] == 'Estudiante']
    docentes = [c for c in correos_registrados if c['tipo'] == 'Docente']

    # Mostrar los correos de estudiantes y docentes
    print(f"{Colores.INFO}Lista de Correos Registrados:{Colores.RESET}")
    linea_divisoria()
    print(f"{Colores.BOLD}Estudiantes:{Colores.RESET}")
    for idx, item in enumerate(estudiantes, start=1):
        print(f"{idx:02d}. {item['correo']} - {Colores.OK}{item['tipo']}{Colores.RESET}")

    print(f"\n{Colores.BOLD}Docentes:{Colores.RESET}")
    for idx, item in enumerate(docentes, start=1):
        print(f"{idx:02d}. {item['correo']} - {Colores.INFO}{item['tipo']}{Colores.RESET}")
    linea_divisoria()

# Función para buscar correos por término
def buscar_correo():
    termino = input("Ingrese el término de búsqueda: ").strip().lower()
    resultados = [c for c in correos_registrados if termino in c['correo'].lower()]

    if resultados:
        print(f"\n{Colores.INFO}Resultados encontrados:{Colores.RESET}")
        for r in resultados:
            print(f"- {r['correo']} ({r['tipo']})")
    else:
        print(f"{Colores.FAIL}No se encontraron coincidencias.{Colores.RESET}")

# Función para mostrar estadísticas del sistema
def mostrar_estadisticas():
    total = len(correos_registrados)
    estudiantes = sum(1 for c in correos_registrados if c['tipo'] == 'Estudiante')
    docentes = sum(1 for c in correos_registrados if c['tipo'] == 'Docente')

    print(f"""{Colores.BOLD}Estadísticas del Sistema:{Colores.RESET}
- Total registrados: {Colores.BOLD}{total}{Colores.RESET}
- Estudiantes: {Colores.OK}{estudiantes}{Colores.RESET}
- Docentes: {Colores.INFO}{docentes}{Colores.RESET}
""")

# Función para eliminar un correo registrado
def eliminar_correo():
    correo = input("Ingrese el correo que desea eliminar: ").strip().lower()
    for c in correos_registrados:
        if c['correo'].lower() == correo:
            correos_registrados.remove(c)  # Elimina el correo
            print(f"{Colores.OK}Correo eliminado correctamente.{Colores.RESET}")
            return
    print(f"{Colores.FAIL}No se encontró el correo especificado.{Colores.RESET}")

# Función para mostrar los créditos del sistema
def mostrar_creditos():
    print(f"""
{Colores.CYAN}{Colores.BOLD}╔══════════════════════════════════════╗
║   Sistema creado por:                ║
║   Equipo de Desarrollo UTV – 2025    ║
║   Uso académico y administrativo     ║
╚══════════════════════════════════════╝{Colores.RESET}\n""")

# ----------------------------- PROGRAMA PRINCIPAL ----------------------------- #

# Función principal que gestiona el menú y las interacciones con el usuario
def main():
    while True:
        mostrar_encabezado()  # Muestra el encabezado
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Seleccione una opción (1-6): ").strip()

        # Ejecución de la opción seleccionada por el usuario
        if opcion == "1": registrar_correo()
        elif opcion == "2": ver_correos()
        elif opcion == "3": buscar_correo()
        elif opcion == "4": mostrar_estadisticas()
        elif opcion == "5": eliminar_correo()
        elif opcion == "6":
            mostrar_creditos()
            print(f"{Colores.OK}Gracias por utilizar el sistema. Hasta pronto.{Colores.RESET}")
            time.sleep(1.5)
            break  # Sale del programa
        else:
            print(f"{Colores.FAIL}Opción inválida. Intente nuevamente.{Colores.RESET}")

        pausar()  # Pausa para que el usuario pueda leer el mensaje

# Llamada a la función principal
if __name__ == "__main__":
    main()





'''
Menú: Se usa un while con opciones para registrar, ver, buscar correos y salir.

Registro: Se pide un correo, se valida con una expresión regular y se clasifica según el dominio (@estudiante.utv.edu.co o @utv.edu.co).

Almacenamiento: Los correos válidos se guardan como diccionarios en una lista.

Visualización: Se imprimen todos los correos registrados con su tipo.

Búsqueda: Se permite buscar por parte del correo y se muestran coincidencias.

Técnicas usadas: Condicionales, ciclos, listas, diccionarios, manejo de strings y regex.
'''