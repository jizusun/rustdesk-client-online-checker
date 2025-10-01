from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
from rustdesk_online import check_rustdesk_online

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract remote ID from URL path
        path_parts = self.path.strip('/').split('/')
        if len(path_parts) >= 2 and path_parts[0] == 'online':
            target_id = path_parts[1]
        else:
            self.send_response(400)
            self.end_headers()
            return
        
        source_id = "123456789"
        server_ip = os.getenv("SERVER_IP")
        
        online = check_rustdesk_online(source_id, target_id, server_ip)
        
        response_data = {
            "source_id": source_id,
            "target_id": target_id,
            "server_ip": server_ip,
            "is_online": online
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=2).encode())

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    server_ip = os.getenv("SERVER_IP")
    
    server = HTTPServer((host, port), Handler)
    print(f"Server starting on {host}:{port}")
    print(f"RustDesk Server IP: {server_ip}")
    server.serve_forever()