try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

    x, y = e.args
    print(x)
    print(y)
"""
output
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
spam
eggs
"""
