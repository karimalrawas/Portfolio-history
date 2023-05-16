from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    # Fetch and pass news articles to the template
    news_articles = [
        {'title': 'News Article 1', 'content': 'Lorem ipsum dolor sit amet.'},
        {'title': 'News Article 2', 'content': 'Consectetur adipiscing elit.'},
        {'title': 'News Article 3', 'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'}
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
