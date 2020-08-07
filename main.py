import os
import json
import re
from http.server import HTTPServer, CGIHTTPRequestHandler

## Чтение JSON
def json_read(file):                                    
        with open(file, "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        return data

def json_list(list_):
    string = ''
    for i in list_:
        #i = i.maketrans('    ', '"[],')
        string = string + i + '\n'
    return string

## Вывод папки
def list_dir(dir_, rel_path):
    '''
    Проверка папки
    '''
    # Перемещаемся в папку
    os.chdir(dir_)
    f = open('index.html', 'w', encoding='utf-8')
    f.write('''
<!DOCTYPE html>
<html>
<head>
{head}
</head>
<body>
{body}
'''.format(head=json_list(temp.get('json_head')), body=json_list(temp.get('json_body_start'))))

    f.write('<p><a id="parrent" href="{}">{}..</a><p>'.format(os.path.join('/' + rel_path, 'index.html'), rel_path))

    rel_path = os.path.join(rel_path, dir_)
    # Проверяем каждый файл
    for i in os.listdir():
        # Если это файл и это не index.html то
        if os.path.isfile(os.path.join(os.getcwd(), i)):
            if i != 'index.html':
                f.write('{start}<a id="file" href="{link_path}" type="application/file">{link}</a>{end}\n'.format(
                    start=temp.get('json_row_start'), 
                    end=temp.get('json_row_end'),
                    link_path=os.path.join(rel_path, i),
                    link=i
                ))
        # Если это папка то
        else:
            f.write('{start}<a id="dir" href="{link_path}">{link}</a>{end}\n'.format(
                start=temp.get('json_row_start'), 
                end=temp.get('json_row_end'),
                link_path=os.path.join(i, 'index.html'), 
                link=i
            ))
            # Запускаем проверку папки
            list_dir(i, rel_path)
    # Перемещаемся обратно
    f.write('''
</body>
</html>''')
    os.chdir('..')

## Запуск сервера
def start_server(dir_list):
    html = open('index.html', 'w', encoding='utf-8')
    html.write('''
<!DOCTYPE html>
<html>
<head>
{head}
</head>
<body>
{body}
'''.format(head=json_list(temp.get('json_head')), body=json_list(temp.get('json_body_start'))))
    for i in dir_list:
        html.write('{start}<a href="{link}">{link}</a>{end}'.format(
            link=i, start=temp.get('json_row_start'), 
            end=temp.get('json_row_end')))
    server_address = ('', 8080)
    html.write('''{body}</body>
</html>
'''.format(body=temp.get('json_body_end')))
    html.close()
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':

    temp = json_read('template/{}.json'.format('example'))
    
    str_input = input('Enter directories: ')
    dir_list = str_input.split(', ')

    for i in dir_list:
        try:
            list_dir(i, '')
        except:
            pass
    
    start_server(dir_list)
