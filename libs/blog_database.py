from pysondb import db
from datetime import datetime


class BlogDatabase:

    def __init__(self):
        self.db = db.getDb("libs/blogdatabase.json")

    def add_article(self, article_title: str, article_author: str, article_content :str ):
        self.db.add({
            "article_author": f'{article_author}',
            "article_title": f"{article_title}",
            "article_content": f'{article_content}',
            "date": f"{datetime.now()}"
        })

    def get_articles(self):

    	data = self.db.getAll()

    	return data
    def delete_article(self,id):
    	self.db.deleteById(id)

    def view_article(self,id):
        data = self.db.getById(id)
        return data
    	