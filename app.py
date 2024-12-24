from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    print("got me")
    query = request.args.get('content')
    if query is not None:
        print(query)
    return render_template('index.html')


if __name__ == "__main__":
        app.run(debug=True)