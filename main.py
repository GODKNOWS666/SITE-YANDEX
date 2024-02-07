from flask import Flask

s = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
     'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

app = Flask(__name__)


@app.route('/')
def index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MARS</title>
    <link rel="stylesheet" type="text/css" href="static/css/style.css">
</head>
<body>
<h1>
    Миссия Колонизация Марса
</h1>


</body>
</html>"""


@app.route('/index')
def index1():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MARS</title>
    <link rel="stylesheet" type="text/css" href="static/css/style.css">
</head>
<body>
<h1>
    И на Марсе будут яблони цвести!
</h1>

</body>
</html>"""


@app.route('/promotion_image')
def promotion_image():
    with open('index.html', 'r', encoding='utf8') as f:
        return f.read()


@app.route('/image_mars')
def image_mars():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MARS</title>
    <link rel="stylesheet" type="text/css" href="static/css/style.css">
</head>
<body>
<h1>
    Жди нас, Марс!
</h1>
<img src="static/css/img/mars.jpg" alt="Картинка Марса">

</body>
</html>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
