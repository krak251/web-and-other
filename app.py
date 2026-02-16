from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route("/index")
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def promotion():
    return """
    <h1>Человечество вырастает из детства.</h1>
    <h2>Человечеству мала одна планета.</h2>
    <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
    <h4>И начнем с Марса!</h4>
    <h1>Присоединяйся!</h1>
    """


@app.route("/image_mars")
def image_mars():
    return render_template("image_mars.html")


@app.route("/promotion_image")
def promotion_image():
    return render_template("promotion_image.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
