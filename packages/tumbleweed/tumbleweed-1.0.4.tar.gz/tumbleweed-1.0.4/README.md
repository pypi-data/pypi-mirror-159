# tumbleweed

*A simple framework for all your blogging needs*

### Setup

1. Initialize the blog object

```
blog = td.Blog(
        title="The Burger Historian",
        description="Brief snippets of the origin of my favorite food",
        author="Daniel"
        )
```


2. Add a post to your blog. *Notice that markdown and inline html is fully supported!*

```
blog.add('Why Vim is better than Emacs', 
    """
    1. Because I say so
    2. My hands are **too small** to type C-y
    3. Refer to item 1
    """
)
```

3. Run your app

```
blog.run(port=8000)
```

### Details

The `Blog` object inherits the default Flask object, so you can use any default
flask options to start the server
