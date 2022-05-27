from flask import Flask, render_template, url_for
app = Flask(__name__, static_folder="static_dir")

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

@app.route("/video")
def video():
    return render_template('video.html')

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/shablon")
def shablon():
    return render_template('shabnews.html')

@app.route("/staff")
def staff():
    return render_template('staff.html')

@app.route("/timetable")
def timetable():
    return render_template('timetable.html')

@app.route("/news1")
def news1():
    return render_template('z_news_1.html')

@app.route("/news2")
def news2():
    return render_template('z_news_2.html')

@app.route("/news3")
def news3():
    return render_template('z_news_3.html')

@app.route("/news4")
def news4():
    return render_template('z_news_4.html')

@app.route("/news5")
def news5():
    return render_template('z_news_5.html')

@app.route("/smiaboutus")
def smiaboutus():
    return render_template('smiaboutus.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
