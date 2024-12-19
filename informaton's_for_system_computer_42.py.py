import psutil
import platform

def system_info():
    print("Важные сведения о системе:")
    print(f"Платформа: {platform.platform()}")
    print(f"Архитектура: {platform.architecture()[0]}")
    
    print("\nБлок информации о CPU:")
    print(f"Количество процессоров: {psutil.cpu_count()}")
    print(f"Загрузка CPU: {psutil.cpu_percent(interval=1)}%")

    print("\nИнформационная строчка о памяти компьютера:")
    mem = psutil.virtual_memory()
    print(f"Общий счёт памяти компьютера: {mem.total / (1024 ** 3):.2f} ГБ")
    print(f"Память, что используется на данный момент: {mem.used / (1024 ** 3):.2f} ГБ")
    print(f"Количество оставшейся свободной памяти: {mem.available / (1024 ** 3):.2f} ГБ")

    print("\nИнформация о дисках:")
    disk = psutil.disk_usage('/')
    print(f"Общее дисковое пространство: {disk.total / (1024 ** 3):.2f} ГБ")
    print(f"Дисковое пространство, что используется на данный момент: {disk.used / (1024 ** 3):.2f} ГБ")
    print(f"Не затронутое дисковое пространство: {disk.free / (1024 ** 3):.2f} ГБ")
    print("")

if __name__ == "__main__":
    system_info()
