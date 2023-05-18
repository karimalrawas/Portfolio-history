from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    # Fetch and pass news articles to the template
    news_articles = [
        {'title': 'The Great Pyramid of Giza', 'content': 'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.'},
        {'title': 'The Sphinx', 'content': 'The Sphinx is a mythical creature with the body of a lion and the head of a human or animal. It is believed to represent royal power and protection.'}
    ]
    return render_template('index.html', articles=news_articles)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
