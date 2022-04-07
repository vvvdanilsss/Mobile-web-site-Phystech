from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('NewPhystech.html', title="Новый физтех. Университет ИТМО")

@app.route("/news")
def news():
    return render_template('news.html', title="Новости")

@app.route("/publications")
def publications():
    return render_template('publications.html', title="Публикации")

@app.route("/seminars")
def seminars():
    return render_template('seminars.html')

if __name__ == "__main__":
    app.run(debug=False)