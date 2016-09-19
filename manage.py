from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
	return 'Bienvenido al bot con Flaks!'

if __name__ == '__main__':
	app.run(PORT = 8000)