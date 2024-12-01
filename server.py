from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

# 设置服务器地址和端口
host = 'localhost'
port = 8000

# 创建服务器
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

# 自动打开浏览器
webbrowser.open(f'http://{host}:{port}/index.html')

print(f"服务器运行在 http://{host}:{port}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
    print("\n服务器已关闭") 