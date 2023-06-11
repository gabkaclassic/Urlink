from app.urlink import app


@app.route("/")
def reduce():
    return "HI"
