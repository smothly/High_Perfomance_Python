@profile
def test_list():
    _list = [0 for i in range(1, 1000000)]
    for i in _list:
        pass

@profile
def test_generator():
    _generator = (0 for i in range(1, 1000000))
    for i in  _generator:
        pass

test_list()
test_generator()