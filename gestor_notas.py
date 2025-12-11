# =======================================================================================================
# FUNCIONES
# =======================================================================================================


def agregar_alumno(notas):
    while True:
        nombre = input("Ingrese el nombre del nuevo alumno (deje en blanco para salir): ").lower()
        if nombre == "":
            print("Volviendo al menú principal...")
            break

        materia = input("Ingrese la materia: ").lower()
        if not materia:
            print("No puede estar vacío")
            continue

        examenes = int(input("Ingrese el número total de exámenes: "))
        if examenes <= 0:
            print("Valor invalido")
            continue

        lista_notas = []
        for i in range(examenes):
            while True:
                try:
                    nota = float(input("Ingrese la nota del examen: "))
                    if nota < 0 or nota > 10:
                        print("Nota no válida (debe ser entre 0-10)")
                        continue
                    lista_notas.append(nota)
                    break
                except ValueError:
                    print("Ingrese un número válido")

        alumno = {"NOMBRE": nombre, "MATERIA": materia, "NOTAS": lista_notas,
                  "PROMEDIO": sum(lista_notas) / len(lista_notas)}
        notas.append(alumno)

def mostrar_registro(notas):
    if not notas:
        print("NO HAY REGISTRO DE NOTAS")
    else:
        print("-" * 20, "REGISTRO ACTUAL", "-" * 20)
        for indice, alumno in enumerate(notas, 1):
            print("Nombre: ", alumno['NOMBRE'].title())
            print("Materia: ", alumno['MATERIA'].title())
            print("Notas: ", alumno['NOTAS'])
            print("Promedio: ", alumno['PROMEDIO'])
            print("-" * 40)

def eliminar_alumno(notas):
    while True:
        if not notas:
            print("No hay mas alumnos para eliminar")
            break

        print("-" * 16, "ELIGA QUE ALUMNO ELIMINAR", "-" * 16)
        for indice, alumno in enumerate(notas, 1):
            print(indice, "Nombre:", alumno['NOMBRE'].title(), "Materia:",
                  alumno['MATERIA'].title(), "Notas:", alumno['NOTAS'], "Promedio:", alumno['PROMEDIO'])

        entrada = input("Ingrese el numero asignado al alumno que se desea eliminar (deje en blanco para salir): ")
        if entrada == "":
            print("Volviendo al menú principal...")
            break
        try:
            indice = int(entrada) - 1
            if indice < 0 or indice > len(notas):
                print("Alumno no encontrado")
                continue
            alumno_eliminado = notas.pop(indice)
            print("Alumno", alumno_eliminado['NOMBRE'].title(), "eliminado correctamente")
        except ValueError:
            print("Ingrese un número válido")
            continue


def generar_archivo_txt(notas):
    if not notas:
        print("No hay alumnos registrados para crear el archivo")
        return

    promedios_generales = []
    for alumno in notas:
        promedio = alumno["PROMEDIO"]
        promedios_generales.append(promedio)
    promedio_general = sum(promedios_generales) / len(promedios_generales)

    with open("alumnos.txt", "w", encoding="utf-8") as archivo:
        print("=" * 50, file=archivo)
        print("REGISTRO DE ALUMNOS", file=archivo)
        print("=" * 50, file=archivo)
        print("Número total de alumnos: ", len(notas), file=archivo)
        print("Promedio general del curso: ", round(promedio_general, 2), file=archivo)
        print("=" * 50, file=archivo)
        # print("\n", file=archivo)

        print("DETALLE DE ALUMNOS:", file=archivo)
        print("=" * 50, file=archivo)

        for alumno in notas:
            nombre_formateado = alumno['NOMBRE'].title()
            materia_formateada = alumno['MATERIA'].title()
            notas_str = ", ".join(format(nota, ".2f") for nota in alumno['NOTAS'])
            promedio_alumno = alumno['PROMEDIO']

            print("Alumno:", nombre_formateado, file=archivo)
            print("Materia:", materia_formateada, file=archivo)
            print("Notas:", notas_str, file=archivo)
            print("Promedio individual:", round(promedio_alumno, 2), file=archivo)
            print("-" * 50, file=archivo)

    print("Archivo 'alumnos.txt' creado correctamente.")


# =======================================================================================================
# PROGRAMA PRINCIPAL
# =======================================================================================================


notas = []

print("-" * 60, "LISTA DE OPCIONES", "-" * 60, "1. Agregar nuevo alumno",
        "2. Ver registro de alumnos", "3. Eliminar un alumno",
        "4. Crear archivo", "5. Salir del sistema.", sep="\n")

try:
    while True:
        opcion = input("Ingrese su opcion: ")

        if opcion < '1' or opcion > '6':
            print("Opción no válida. Por favor ingrese 1, 2, 3, 4, o 5")
            continue
        elif opcion == '1':
            agregar_alumno(notas)
        elif opcion == '2':
            mostrar_registro(notas)
        elif opcion == '3':
            eliminar_alumno(notas)
        elif opcion == '4':
            generar_archivo_txt(notas)
        elif opcion == '5':
            print("ADIOS")
            break

except ValueError:
    print("Valor NO valido")
except:
    print("Error inesperado")