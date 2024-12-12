from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    # Ensure the app listens on all interfaces for Docker to access it
    app.run(host='0.0.0.0', port=5000)
