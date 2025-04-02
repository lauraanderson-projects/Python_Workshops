from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

class PasswordGenerator:
    def __init__(self, length=16, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols
        
    def generate(self):
        characters = ""
        if self.use_upper:
            characters += string.ascii_uppercase
        if self.use_lower:
            characters += string.ascii_lowercase
        if self.use_numbers:
            characters += string.digits
        if self.use_symbols:
            characters += string.punctuation
        if not characters:
            return "Error: No character set selected."
        
        return ''.join(random.choice(characters) for _ in range(self.length))

@app.route('/generate-password', methods=['POST'])
def get_password():
    data = request.json
    #print(data)  # Print the received data
    password_generator = PasswordGenerator(
		length=int(data.get('length', 16)),
		use_upper=data.get('use_upper', True),
		use_lower=data.get('use_lower', True),
		use_numbers=data.get('use_numbers', True),
		use_symbols=data.get('use_symbols', True)
	)
    return jsonify({'password': password_generator.generate()})

if __name__ == '__main__':
	app.run(debug=True)
  
