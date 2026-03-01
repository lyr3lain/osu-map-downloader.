import requests

id_map = input('Введите цифры после beatmapsets/: ').strip()

link = f'https://beatconnect.io/b/{id_map}'
filename = f'{id_map}.osz'

print(f'Качаю карту: {link}')

try:
    with requests.get(link, stream=True, timeout=10) as res:
        res.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in res.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
                    print(".", end="", flush=True)

    print(f'\nГотово! {filename}')
except Exception as e:
    print(f'\nОшибка: {e}')
