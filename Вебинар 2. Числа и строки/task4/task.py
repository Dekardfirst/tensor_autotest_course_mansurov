def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    parts = file_path.split('\\')
    file_with_extension = parts[-1]
    file_name = file_with_extension.rsplit('.', 1)[0]
    disk_name = ''
    if len(parts) > 0 and ':' in parts[0]:
        disk_name = parts[0].replace(":",'')

    root_folder = parts[1] if len(parts) > 1 else ''

    return file_name, disk_name, root_folder