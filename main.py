import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Blog(db.Model):

    blog_id = db.StringProperty(required = True)
    title = db.StringProperty(required = True)
    blog_text = db.TextProperty(required = True)
    ##created = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.response.write('Hello world!')

    # def get(self):
    #     self.render("blog.html")

class BlogPage(Handler):
    def get(self):
        text = "test"
        t = jinja_env.get_template("blog.html")
        content = t.render(text = text)
        self.render(content)

class NewPost(Handler):
    def get(self):
        self.render("newpost.html")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/blog', BlogPage),
    ('/newpost', NewPost)
], debug=True)
