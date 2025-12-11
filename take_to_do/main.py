from database import Database
import time


def main():
    db = Database()

    while True:
        time.sleep(1)
        print("\n----- TO DO LIST -----")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("\nIngresá una opción: ")

        if option == "1":
            title = input("¿Qué tarea deseas agregar?: ").strip()
            while not title:
                title = input("No ingresaste una tarea válida, intenta de nuevo: ").strip()
            db.insert_task(title)
            print("\n-------------------------------------------")
            print("Tarea agregada.")
            print("-------------------------------------------")

        elif option == "2":
            tasks = db.get_all_tasks()
            if len(tasks) == 0:
                print("\n-------------------------------------------")
                print("No hay tareas.")
                print("-------------------------------------------")
            else:
                print("\n-------------------------------------------")
                for task in tasks:
                    print(task)
                print("-------------------------------------------")

        elif option == "3":
            task_id = int(input("ID de la tarea: "))
            db.mark_done(task_id)
            print("\n-------------------------------------------")
            print("Tarea marcada como hecha.")
            print("-------------------------------------------")

        elif option == "4":
            task_id = int(input("ID de la tarea: "))
            db.delete_task(task_id)
            print("\n-------------------------------------------")
            print("Tarea eliminada.")
            print("-------------------------------------------")

        elif option == "5":
            db.close()
            print("\n-------------------------------------------")
            print("Hasta la proxima 👋")
            print("-------------------------------------------\n")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
