from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_posts = Post()

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/blog_post/<int:id>')
def blog_post(id):
    return render_template("post.html", all_posts=all_posts, id=id)

if __name__ == "__main__":
    app.run(debug=True)
