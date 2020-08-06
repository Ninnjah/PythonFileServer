# PythonFileServer
![banner](https://github.com/Ninnjah/PythonFileServer/blob/master/screen.png)
File WebServer on python, just like FTP but HTTP

##Usage
```python
    Enter directories: directory_one, sample, folder of four words
```

## Code
1. Checking directories and creating webpages
```python
def list_dir(dir_, rel_path):

    rel_path = os.path.join(rel_path, dir_)
    
    for i in os.listdir():
        if os.path.isfile(os.path.join(os.getcwd(), i)):
            if i != 'index.html':
                f.write(link to file)
        else:
            f.write(link to folder)
            list_dir(i, rel_path)
            
    os.chdir('..')
```
2. Starting server
```python
def start_server(dir_list):

    for i in dir_list:
        html.write(links to directories)
        
    server_address = ('', 8080)
    html.close()
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()
```
