from flask import Flask, render_helloworld

app = Flask(__name__)

@app.route('/')
def index():
     return render_helloworld('index.html')

if __name__ == '__main__':
      app.run(debug=True)
