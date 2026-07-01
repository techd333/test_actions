def add(a, b):
  """add function

  Args:
      a (_type_): _description_
      b (_type_): _description_

  Returns:
      _type_: _description_
      
  >>> add(1, 2)
  3
  """
  return a + b


def test_add():
  assert add(1, 2) == 3
