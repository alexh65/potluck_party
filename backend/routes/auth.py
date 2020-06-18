from app import app

@app.route('/')
def hello():
  return 'Hello World'

@app.route('/ping')
def ping_pong():
  return 'ponpingg'