import os

app = Flask(__name__)

@app.route("/")
def helloworld():
    print("1")
    return "worked"

print(__name__)
if __name__ == "__main__":
    print("0")
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
print("0.5")