"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1>Hi there</h1>

heading_generator('Hi there', '3')
<h3>Hi there</h3>
"""


def heading_generator(title, heading_type):
    if 6 >= int(heading_type) >= 1:
        return f'<h{heading_type}>{title}</h{heading_type}>'
    else:
        return "Heading size not supported"


print(heading_generator('hello', '1'))
