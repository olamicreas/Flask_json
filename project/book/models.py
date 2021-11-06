from project import db

class book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  author = db.Column(db.Text)

  def __init__(self, title, author):
    self.title = title
    self.author = authors