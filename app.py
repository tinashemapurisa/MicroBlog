
from flask import Flask,redirect,url_for,render_template,request
from libs.blog_database import BlogDatabase 
app=Flask(__name__)


@app.route('/add',methods = ["POST","GET"])
def add():
    if request.method =="POST":
        
        title_text= request.form['title']
        author_text= request.form['author']
        article_text= request.form['article']

        BlogDatabase().add_article(title_text,author_text,article_text)

    return redirect("/")

@app.route('/add_page')
def add_page():
    return render_template("add.html")



@app.route('/blog/<id>')
def blog(id):
    data  = BlogDatabase().view_article(id)
    return render_template("blog.html",article = data)

@app.route('/')
def home():
    return render_template('home.html',articles =BlogDatabase().get_articles())

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5001,debug=True)

