import sys

# ahora para evitar errores como por ejempo que se se divida por cero y causar un error,  incluimos la función try para poder evaluar la antes
# Luego le damos una exepsión la cual menciona que si se divide por cero, se debe salir del sistema 
# hay que tener en cuenta que para poder salir del error importamos al inicio del codigo  import sys, el cual si adquiere el valor de 1 sale de la ejecución del programa

x = int(input("x: "))
y = int(input("y: "))

try: result =x/y

except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
