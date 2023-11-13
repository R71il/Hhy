from TVonline import app
from TVonline.routes import thread

if __name__ == "__main__":
  thread.start()
  app.run(port=8080, host="0.0.0.0")
