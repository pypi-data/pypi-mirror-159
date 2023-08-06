from flask import Flask, render_template
import datetime as dt
import re


def to_markdown(string):

    string = re.sub(r'^\s*', '', string)

    # italics, bold
    string = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', string)
    string = re.sub(r'\*(.+?)\*', r'<i>\1</i>', string)

    # list
    string = re.sub(r'(\d\.\s)(.+)', r'<p> \1\2</p>', string)
    string = re.sub(r'[\-\*]\s(.+)', r'<p>• \1</p>', string)

    # h1 - h6
    for i in range(1, 7):
        string = re.sub(f'^{"#"*i}\\s(.+)', f'<h{i}>\\1</h{i}>', string)

    # line breaks
    string = re.sub(r'(.+?)\n\n', r'<p>\1</p>', string, flags=re.DOTALL)
   
    # links
    string = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', string)
    return string



class Post:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date.strftime('%Y-%m-%d')

    def render(self):
        return {
            'title': self.title,
            'content': self.content,
            'date': self.date
        }


class Blog(Flask):
    def __init__(self, title, description, author, *args, **kwargs):
        self.title = title
        self.description = description
        self.author = author
        self.posts = []

        super(Blog, self).__init__(__name__, *args, **kwargs)


        self.add_generic_template(
            path='/', 
            title='Home', 
            template='index.html', 
            blog_title=self.title,
            description=self.description,
            author=self.author,
        )

    def add(self, title, content, date=dt.datetime.now()):
        markdown = to_markdown(content)
        post = Post(title, markdown, date)
        self.posts.append(post)

    def add_generic_template(self, path, title, template, **kwargs):
        def add_func():
            return render_template(template, posts=self.posts, **kwargs)

        self.add_url_rule(path, title, add_func)

