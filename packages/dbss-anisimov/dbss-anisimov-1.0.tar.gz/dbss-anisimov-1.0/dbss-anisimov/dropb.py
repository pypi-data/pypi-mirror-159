import dropbox

dbx = dropbox.Dropbox(
    'sl.BLh6WeGcIj4jllx-UJiJQ4HZ7iNw3bHtLzvpnpEqmmUCp255KNoEINT100qdYPyZnF3WvRViFohZsf3xXVehzTDTOZdqeOkBL5peRPJOwgLyLY08Njb9JfFRN09D35GGvrZB5K17a6rl'
)
import os
def push_database(base):
    try:
      dbx.files_delete_v2(f'/{base}.txt')
    except:
        print(f'No such file or directory - {base}')
    with open(f'{base}.txt', 'rb') as file:  # открываем файл в режиме чтение побайтово
        response = dbx.files_upload(file.read(),
                                    f'/{base}.txt')  # загружаем файл: первый аргумент (file.read()) - какой файл; второй - название, которое будет присвоено файлу уже на дропбоксе.

def get_database(base):
    try:
        os.remove(f"base.txt")
    except:
        ...
    metadata, f = dbx.files_download('/' + base+'.txt')
    out = open(base+'.txt', 'wb')
    out.write(f.content)
    out.close()
push_database('data')