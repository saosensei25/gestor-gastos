import json
import os 

# Archivo donde guardaremos los gastos
ARCHIVO = "gastos.json"

# Cargamos los gaastos si existen 
def cargar_gastos():
  if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r") as f:
      return json.load(f)
  else:
      return []  
  
# Guardamos los gastos
def guardar_gastos(gastos):
     with open(ARCHIVO, "w") as f:
        json.dump(gastos, f, indent=4)

# Mostrar menu
def mostrar_menu():
   print("\n--- GESTOR DE GASTOS ---")
   print("1. Agregar gasto")
   print("2. Ver todos los gastos")
   print("3. Ver total gastado")
   print("4. Filtrar por categoria")
   print("5. Salir")

# Agregar un gasto nuevo
def agregar_gasto(gastos):
   descripcion = input("Descripcion del gasto: ")
   monto = float(input("Monto: "))
   categoria = input ("Categoria (ej:comida, transporte, ocio): ")
   gasto = {
      "descripcion": descripcion,
      "monto": monto,
      "categoria": categoria
   }
   gastos.append(gasto)
   guardar_gastos(gastos)
   print("✅ Gasto agregado exitosamente.")

# Ver todos los gastos
def ver_gastos(gastos):
   if not gastos:
      print("No hay gastos registrados.")
      return
   for i, g in enumerate(gastos, 1):
      print(f"{i}. {g['descripcion']} - ${g['monto']} [{g['categoria']}]")

# Ver total gastado
def ver_total(gastos):
     total = sum(g['monto'] for g in gastos)
     print(f"💰 Total gastado: ${total}")

# Filtrar por categoria
def filtrar_categoria(gastos):
     categoria = input("Categoria a filtrar: ")
     filtrados = [g for g in gastos if g ['categoria'].lower() == categoria.lower()]
     if not filtrados:
        print("No hay gastos en esa categoria.") 
     else:
        for g in filtrados:
            print(f"- {g['descripcion']} - ${g['monto']}")

# Programa principal
def main():
   gastos = cargar_gastos()
   while True:
      mostrar_menu()
      opcion = input("Elige una opcion: ")
      if opcion == "1":
         agregar_gasto(gastos)
      elif opcion == "2":
         ver_gastos(gastos)
      elif opcion == "3":
         ver_total(gastos)
      elif opcion == "4":
         filtrar_categoria(gastos) 
      elif opcion == "5":
         print("Saliendo... Hasta luego!")
         break
      else:
         print("Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
