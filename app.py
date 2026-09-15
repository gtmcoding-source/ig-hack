from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    # 1. Point to your trusted mkcert certificate files
    # Make sure 'localhost.pem' and 'localhost-key.pem' are in the same folder as this script
    ssl_context = ('localhost.pem', 'localhost-key.pem')
    
    # 2. Run on port 443 with your trusted context
    # Note: Using 'localhost' instead of '0.0.0.0' guarantees the certificate matches the URL
    app.run(host='localhost', port=443, ssl_context=ssl_context)
