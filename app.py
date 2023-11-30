from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/game/mir4")
def game_market_list():
    return render_template('gamemarket_main_page.html')

if __name__ == "__main__":
    app.run(
      host = '0.0.0.0',
      debug = True
    )