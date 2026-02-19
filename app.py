from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route("/index")
def index():
    return render_template("base.html", title="Заготовка")


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


planet_slovar = {
    "Марс": {
        "description": "Эта планета близка к Земле;",
        "resources": "На ней много необходимых ресурсов;",
        "atmosphere": "На ней есть вода и атмосфера;",
        "magnetic_field": "На ней есть небольшое магнитное поле;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Земля": {
        "description": "Это наша родная планета;",
        "resources": "На ней есть всё, что нужно для жизни;",
        "atmosphere": "На ней есть воздух и вода;",
        "magnetic_field": "На ней есть магнитное поле;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Венера": {
        "description": "Эта планета — жаркий и токсичный мир;",
        "resources": "На ней есть металлы, но в условиях, не подходящих для жизни;",
        "atmosphere": "На ней есть плотная атмосфера из углекислого газа;",
        "magnetic_field": "На ней практически нет магнитного поля;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Юпитер": {
        "description": "Это гигант — самая большая планета;",
        "resources": "На ней есть водород, гелий и другие элементы;",
        "atmosphere": "На ней есть гигантские облака и ветры;",
        "magnetic_field": "На ней есть очень сильное магнитное поле;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Сатурн": {
        "description": "Эта планета известна своими кольцами;",
        "resources": "На ней есть газы и лёд, но не для жизни;",
        "atmosphere": "На ней есть тонкая атмосфера из метана и водорода;",
        "magnetic_field": "На ней есть магнитное поле, но слабее, чем у Юпитера;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Уран": {
        "description": "Эта планета вращается на боку;",
        "resources": "На ней есть водород, гелий и метан;",
        "atmosphere": "На ней есть атмосфера с синим оттенком из метана;",
        "magnetic_field": "На ней есть магнитное поле, но сильно смещено;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Нептун": {
        "description": "Эта планета — холодный и ветренистый мир;",
        "resources": "На ней есть водород, гелий и метан;",
        "atmosphere": "На ней есть сильные ветры и тёмная атмосфера;",
        "magnetic_field": "На ней есть сильное магнитное поле;",
        "beauty": "Наконец, она просто красивая!"
    },
    "Меркурий": {
        "description": "Эта планета — самый близкий к Солнцу;",
        "resources": "На ней есть металлы и редкие элементы;",
        "atmosphere": "На ней почти нет атмосферы;",
        "magnetic_field": "На ней есть слабое магнитное поле;",
        "beauty": "Наконец, она просто красивая!"
    }
}


@app.route("/choice/<planet_name>")
def choice_planet(planet_name):
    return render_template("choice.html", planet_name=planet_name,
                           description=planet_slovar[planet_name]["description"],
                           resources=planet_slovar[planet_name]["resources"],
                           atmosphere=planet_slovar[planet_name]["atmosphere"],
                           magnetic_field=planet_slovar[planet_name]["magnetic_field"],
                           beauty=planet_slovar[planet_name]["beauty"])


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)


@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html", title="отбор астронавтов")


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
