When installation of dependencecy is complete (requirements.txt)

- Create the Flask App (backend/app.py)
- Run the Backend

---

## python backend/app.py

Your Flask API should start at http://127.0.0.1:5000/

- Create the Frontend UI
  (frontend/index.html, frontend/script.js, frontend/style.css)

- Run and Test

1. Start the backend

   > python backend/app.py

2. Start Live Server for HTML:
   Open index.html in VS Code and then open with Live Server

##################
Possible Issues
##################

## 127.0.0.1 - - [30/Mar/2025 16:18:40] "GET /generate-password HTTP/1.1" 404

---

1. Check that the Flask app is running in the backend.
2. Check your Flask app (backend/app.py) has the correct route definition:
   @app.route('/generate-password', methods=['GET'])
3. Check URL in Javascript
   const response = await fetch("http://127.0.0.1:5000/generate-password");
4. Restart the Flask Server
5. Debug with Flask Routes
   > flask routes
6. Check for Virtual Enviorment Issues

# On macOS/Linux

source venv/bin/activate

# On Windows

venv\Scripts\activate

Then restart Flask. 7. Check console for Errors

> pip install flask-cors

## Then modify app.py by adding the following to your file:

from flask_cors import CORS

app = Flask(**name**)
CORS(app) # Allow frontend requests

##################
Possible Issues
##################

## 127.0.0.1 - - [30/Mar/2025 16:25:00] "GET /generate-password HTTP/1.1" 200

---

200 is a good sign

1. Check Flask Response
   Test it manually by opening http://127.0.0.1:5000/generate-password in your browser. You should see something like:
   {"password": "A9&k#P1z@Xc"}
