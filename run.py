import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Use environment variables for sensitive information
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Temporary data storage (replace with a database in a production environment)
articles = [
    {'title': 'The Great Pyramid of Giza', 'content': 'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.', 'comments': [], 'likes': 0},
    {'title': 'The Sphinx', 'content': 'The Sphinx is a mythical creature with the body of a lion and the head of a human or animal. It is believed to represent royal power and protection.', 'comments': [], 'likes': 0}
]

# Routes
@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        article = {'title': title, 'content': content, 'comments': [], 'likes': 0}
        articles.append(article)
        return render_template('index.html', articles=articles)
    return render_template('post.html')

@app.route('/comment', methods=['POST'])
def comment():
    article_id = int(request.form.get('article_id'))
    comment_text = request.form.get('comment')
    articles[article_id]['comments'].append(comment_text)
    return render_template('index.html', articles=articles)

@app.route('/like', methods=['POST'])
def like():
    article_id = int(request.form.get('article_id'))
    articles[article_id]['likes'] += 1
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    # Use environment variables for host and port
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
