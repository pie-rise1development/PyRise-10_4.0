import random

def generate_fax_number(area_code):
    # Генерируем случайный номер факса.
    number = f"{area_code}-{random.randint(1000000, 9999999)}"
    return number

if __name__ == "__main__":
    area_code = input("Впишите код страны, для генерации дополнительного fax-number-phone: ")
    fax_number = generate_fax_number(area_code)
    print(f"Вот ваш сгенерированный номер телефона (вида факс): {fax_number}")