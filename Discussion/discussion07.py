def square_tree(t):
  if t:
    t.entry = t.entry ** 2
    square_tree(t.left)
    square_tree(t.right)
  

def height(t):
  if not t:
    return 0
  return 1 + max(height(t.left), height(t.right))
  result = 0
  if t.left:
    result = max(height(t.left), result)
  if t.right:
    result = max(height(t.right), result)
  return 1 + result


def tree_size(t):
  if not t:
    return None
  return 1 + tree_size(t.left) + tree_size(t.right)

def find_path(t, entry):
  if not t:
    return None
  elif t.entry == entry:
    return tuple(t.entry)
  find_path(t.left, entry)
  find_path(t.right, entry)

def print_inorder(t):
  if t.left == None and t.right == None:
    print(t.entry)
  elif t.left:
    print_inorder(t.left)
  elif t.right:
    print_inorder(t.right)
  Desparately Need help  with Trees


  
  find_path(t.left, entry)
  find_path(t.right, entry)


  def list_to_bst(lst):
    m = len(lst) // 2
    left = list_to_bst(lst[:mid])
    right = list_to_bst(lst[mid+1:])
    return Tree(lst[mid], left, right)
  


  def find_path_bst(t, val):
    if not t:
     return None
    elif t.entry = val:
      return tuple(t.entry)
    elif val < t.entry:
      return find_path_bst(t.left, val)
    elif val > t.entry:
      return find_path_bst(t.right, val)
    

    i



