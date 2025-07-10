import pathlib

def remove_digits_and_save():
    """
    Читает данные из "test_file/task1_data.txt",
    удаляет цифры и записывает результат в "test_file/task1_answer.txt".
    """

    input_file_path = pathlib.Path("test_file/task1_data.txt")
    output_file_path = pathlib.Path("test_file/task1_answer.txt")

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            data = infile.read()

        cleaned_data = ''.join(char for char in data if not char.isdigit())

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(cleaned_data)

    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {input_file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

remove_digits_and_save()
