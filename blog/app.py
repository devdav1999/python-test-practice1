blogs = dict()  # blog_name: blog object

MENU_PROMPT = 'Enter "c" to create a blog, "r" to read one, "p" to create a post or "q" to quit: '

def menu():
    # show user available blogs
    # let user make choice
    # do something with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


