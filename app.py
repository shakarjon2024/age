from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age():
    result = ""

    if request.method == "POST":
        age = int(request.form.get("age"))

        if age <= 12:
            result = "Bola"
        elif age <= 19:
            result = "O‘smir"
        else:
            result = "Katta"

    return render_template("age.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
