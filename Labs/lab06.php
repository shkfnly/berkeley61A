<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> 
  <head>
    <meta name="description" content ="CS61A: Structure and Interpretation of Computer Programs" /> 
    <meta name="keywords" content ="CS61A, Computer Science, CS, 61A, Programming, John DeNero, Berkeley, EECS" />
    <meta name="author" content ="John DeNero, Soumya Basu, Jeff Chang, Brian Hou, Andrew Huang, Robert Huang, Michelle Hwang, Richard Hwang,
                                  Joy Jeng, Keegan Mann, Stephen Martinis, Bryan Mau, Mark Miyashita, Allen Nguyen, Julia Oh, Vaishaal
                                  Shankar, Steven Tang, Sharad Vikram, Albert Wu, Chenyang Yuan" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> 
    <style type="text/css">@import url("../lab_style.css");</style>
    <style type="text/css">@import url("../61a_style.css");</style>

    <title>CS 61A Fall 2013: Lab 6</title> 

      </head> 
  <body style="font-family: Georgia,serif;">
    <h1>CS 61A Lab 6</h1>
<h2>Inheritance and Recursive Data Structures</h2>
<p>We've provided a starter file with skeleton code for the exercises in
the lab. You can get it at the following link:</p>

<ul>
<li><a href="./lab6.py">lab6.py</a></li>
</ul>

<h3>Inheritance</h3>

<p>You can find additional practice problems from this
<a href="http://www-inst.eecs.berkeley.edu/~cs61a/sp13/labs/lab07/lab7.php">lab on OOP</a>
from Spring 2013 helpful.</p>

<p><strong>Problem 1</strong>: Consider the following code:</p>

<pre><code>class Animal(object):
    def __init__(self):
        self.is_alive = True  # It's alive!!

class Pet(Animal):
    def __init__(self, name, year_of_birth, owner=None):
        Animal.__init__(self)   # call the parent's constructor
        self.name = name
        self.age = current_year - year_of_birth
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print("...")
</code></pre>

<p>Implement a <code>Cat</code> class that inherits from <code>Pet</code>. Use superclass
methods wherever possible.</p>

<pre><code>class Cat(Pet):
    def __init__(self, name, year_of_birth, owner, lives=9):
        "*** YOUR CODE HERE ***"

    def talk(self):
        """A cat says 'Meow!' when asked to talk."""
        "*** YOUR CODE HERE ***"

    def lose_life(self):
        """A cat can only lose a life if they have at least one
        life. When there are zero lives left, the 'is_alive'
        variable becomes False.
        """
        "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton0">Toggle Solution</button>
  <div id="toggleText0" style="display: none">
    <pre><code>class Cat(Pet):
    def __init__(self, name, year_of_birth, owner, lives=9):
        Pet.__init__(self, name, year_of_birth, owner)
        self.lives = lives

    def talk(self):
        print('Meow!')

    def lose_life(self):
        if self.lives &gt; 0:
            self.lives -= 1
            if self.lives == 0
                self.is_alive = False
        else:
            print('This cat has no more lives to lose x_x')
</code></pre>

  </div>
<p><strong>Problem 2</strong>: Now implement a <code>NoisyCat</code> class, which inherits from
<code>Cat</code>. A <code>NoisyCat</code> is just like a normal <code>Cat</code> except, when asked to
talk, it says what a normal <code>Cat</code> says twice.</p>

<pre><code>class NoisyCat(Cat):
    def __init__(self, name, year_of_birth, owner, lives=9):
        "*** YOUR CODE HERE ***"
        # hint: do you need to write another __init__?

    def talk(self):
        """A NoisyCat will always repeat what he/she said
        twice."""
        "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton1">Toggle Solution</button>
  <div id="toggleText1" style="display: none">
    <pre><code>class NoisyCat(Cat):
    def __init__(self, name, year_of_birth, owner, lives=9):
        Cat.__init__(self, name, year_of_birth, owner, lives)

    def talk(self):
        Cat.talk(self)
        Cat.talk(self)
</code></pre>

<p>Observe two things:
1. The <code>__init__</code> method is actually unnecessary, since it does
   exactly what the superclass <code>__init__</code> does. As such, we could
   arrive at the correct functionality by simply removing the
   <code>__init__</code> method in <code>NoisyCat</code>.
2. In <code>talk</code>, notice we do not use <code>self.talk()</code>. This would cause an
   infinite recursive loop. Why?</p>

  </div>
<h3>Recursive Lists</h3>

<p>In lecture, we introduced the OOP version of an <code>Rlist</code>:</p>

<pre><code>class Rlist:
    """A recursive list consisting of a first element and the rest.

    &gt;&gt;&gt; s = Rlist(1, Rlist(2, Rlist(3)))
    &gt;&gt;&gt; print(rlist_expression(s.rest))
    Rlist(2, Rlist(3))
    &gt;&gt;&gt; len(s)
    3
    &gt;&gt;&gt; s[1]
    2
    """

    class EmptyList:
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)
</code></pre>

<p>Just like before, these <code>Rlists</code> have a first and a rest. The difference is
that, now, the <code>Rlists</code> are mutable.</p>

<p>To check if an <code>Rlist</code> is empty, compare it against the class variable
<code>Rlist.empty</code>:</p>

<pre><code>if rlist is Rlist.empty:
    return 'This rlist is empty!'
</code></pre>

<p>Don't construct another <code>EmptyList</code>!</p>

<p>In this lab, we will be using <code>rlist_expression</code> to print a string
representation of an Rlist.</p>

<pre><code>def rlist_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Rlist.empty:
        rest = ''
    else:
        rest = ', ' + rlist_expression(s.rest)
    return 'Rlist({0}{1})'.format(s.first, rest)
</code></pre>

<p><strong>Problem 3</strong>: Predict what Python will display when the following lines are
typed into the interpreter:</p>

<pre><code>&gt;&gt;&gt; print(rlist_expression(Rlist(1, Rlist(2))))
_____
&gt;&gt;&gt; Rlist()
_____
&gt;&gt;&gt; rlist = Rlist(1, Rlist(2, Rlist(3)))
&gt;&gt;&gt; rlist.first
_____
&gt;&gt;&gt; rlist.rest.first
_____
&gt;&gt;&gt; rlist.rest.rest.rest is Rlist.empty
_____
&gt;&gt;&gt; rlist.first = 9001
&gt;&gt;&gt; rlist.first
_____
&gt;&gt;&gt; rlist.rest = rlist.rest.rest
&gt;&gt;&gt; rlist.rest.first
_____
&gt;&gt;&gt; rlist = Rlist(1)
&gt;&gt;&gt; rlist.rest = rlist
&gt;&gt;&gt; rlist.rest.rest.rest.rest.first
_____
</code></pre>

  <button id="toggleButton2">Toggle Solution</button>
  <div id="toggleText2" style="display: none">
    <ol>
<li>Rlist(1, Rlist(2))</li>
<li>TypeError</li>
<li>1</li>
<li>2</li>
<li>True</li>
<li>9001</li>
<li>3</li>
<li>1</li>
</ol>

  </div>
<h3>List folding</h3>

<p>A recursive list can be represented as a series of <code>Rlist</code> constructors, where
<code>Rlist.rest</code> is either another recursive list or the empty list.</p>

<p>We represent such a list in the diagram below:</p>

<p><img src="./rightfold.png" alt="Right fold" /></p>

<p>In this diagram, the recursive list</p>

<pre><code>Rlist(1, Rlist(2, Rlist(3, Rlist(4,Rlist(5)))))
</code></pre>

<p>is represented with <code>:</code> as the constructor and <code>[]</code> as the empty list.</p>

<p>We define a function <code>foldr</code> that takes in a function <code>f</code> which takes two
arguments, and a value <code>z</code>. <code>foldr</code> essentially replaces the <code>Rlist</code> constructor
with f, and the empty list with <code>z</code>. It then evaluates the expression and
returns the result. This is equivalent to:</p>

<pre><code>f(1, f(2, f(3, f(4, f(5, z)))))
</code></pre>

<p>We call this operation a right fold.</p>

<p>Similarily we can define a left fold <code>foldl</code> that folds a list starting from the
beginning, such that the function <code>f</code> will be applied this way:</p>

<pre><code>f(f(f(f(f(z, 1), 2), 3), 4), 5)
</code></pre>

<p><img src="./leftfold.png" alt="Left fold" /></p>

<p>Also notice that a left fold is equivilant to python's <code>reduce</code> with 3 arguments.</p>

<p><strong>Problem 4</strong>: Write the left fold function by filling in the blanks.</p>

<pre><code>def foldl(rlist, fn, z):
    """ Left fold
    &gt;&gt;&gt; lst = Rlist(3, Rlist(2, Rlist(1)))
    &gt;&gt;&gt; foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    &gt;&gt;&gt; foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    &gt;&gt;&gt; foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if rlist is Rlist.empty:
        return z
    return foldl(______, ______, ______)
</code></pre>

  <button id="toggleButton3">Toggle Solution</button>
  <div id="toggleText3" style="display: none">
    <pre><code>foldl(rlist.rest, fn, fn(z, rlist.first))
</code></pre>

  </div>
<p><strong>Problem 5</strong>: Now write the right fold function.</p>

<pre><code>def foldr(rlist, fn, z):
    """ Right fold
    &gt;&gt;&gt; lst = Rlist(3, Rlist(2, Rlist(1)))
    &gt;&gt;&gt; foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    &gt;&gt;&gt; foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    &gt;&gt;&gt; foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton4">Toggle Solution</button>
  <div id="toggleText4" style="display: none">
    <pre><code>def foldr(rlist, fn, z):
    if rlist is Rlist.empty:
        return z
    return fn(rlist.first, foldr(rlist.rest, fn, z))
</code></pre>

  </div>
<p>Now that we've written the fold functions, let's write some useful functions
  using list folding!</p>

<p><strong>Problem 6</strong>: Write the <code>mapl</code> function, which takes in a Rlist <code>lst</code> and a
function <code>fn</code>, and returns a new Rlist where every element is the function
applied to every element of the original list. Use either <code>foldl</code> or
<code>foldr</code>. Hint: it is much easier to write with one of them than the other!</p>

<pre><code>def mapl(lst, fn):
    """ Maps FN on LST
    &gt;&gt;&gt; lst = Rlist(3, Rlist(2, Rlist(1)))
    &gt;&gt;&gt; mapped = mapl(lst, lambda x: x*x)
    &gt;&gt;&gt; print(rlist_expression(mapped))
    Rlist(9, Rlist(4, Rlist(1)))
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton5">Toggle Solution</button>
  <div id="toggleText5" style="display: none">
    <pre><code>def mapl(lst, fn):
    return foldr(lst, lambda x, xs: Rlist(fn(x), xs), Rlist.empty)
</code></pre>

  </div>
<p><strong>Problem 7</strong>: Write the <code>filterl</code> function, using either <code>foldl</code> or <code>foldr</code>.</p>

<pre><code>def filterl(lst, pred):
    """ Filters LST based on PRED
    &gt;&gt;&gt; list = Rlist(4, Rlist(3, Rlist(2, Rlist(1))))
    &gt;&gt;&gt; filtered = filterl(lst, lambda x: x % 2 == 0)
    &gt;&gt;&gt; print(rlist_expression(filtered))
    Rlist(4, Rlist(2))
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton6">Toggle Solution</button>
  <div id="toggleText6" style="display: none">
    <pre><code>def filterl(lst, pred):
    def filtered(x, xs):
        if pred(x):
            return Rlist(x, xs)
        return xs
    return foldr(lst, filtered, Rlist.empty)
</code></pre>

  </div>
<p><strong>Problem 8</strong>: Use foldl to write <code>reverse</code>, which takes in a recursive list and
  reverses it. Hint: It only takes one line!</p>

<pre><code>def reverse(lst):
    """ Reverses LST with foldl
    &gt;&gt;&gt; reversed = reverse(Rlist(3, Rlist(2, Rlist(1))))
    &gt;&gt;&gt; print(rlist_expression(reversed))
    Rlist(1, Rlist(2, Rlist(3)))
    &gt;&gt;&gt; reversed = reverse(Rlist(1))
    &gt;&gt;&gt; print(rlist_expression(reversed))
    Rlist(1)
    &gt;&gt;&gt; reversed = reverse(Rlist.empty)
    &gt;&gt;&gt; reversed == Rlist.empty
    True
    """
    "*** YOUR CODE HERE ***"
</code></pre>

<p>Extra for experts: Write a version of reverse that do not use the <code>Rlist</code>
constructor. You do not have to use <code>foldl</code> or <code>foldr</code>.</p>

  <button id="toggleButton7">Toggle Solution</button>
  <div id="toggleText7" style="display: none">
    <pre><code>def reverse(lst):
    return foldl(lst, lambda x, y: Rlist(y, x), Rlist.empty)

def reverse2(lst):
    if lst is Rlist.empty:
        return lst
    elif lst.rest is not Rlist.empty:
        second, last = lst.rest, lst
        lst = reverse2(second)
        second.rest, last.rest = last, Rlist.empty
    return lst
</code></pre>

  </div>
<p><strong>Problem 9 Extra for Experts</strong>: Write foldl using foldr! You only need to fill
  in the <code>step</code> function.</p>

<pre><code>def foldl2(rlist, fn, z):
    """ Write foldl using foldr
    &gt;&gt;&gt; list = Rlist(3, Rlist(2, Rlist(1)))
    &gt;&gt;&gt; foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    &gt;&gt;&gt; foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    &gt;&gt;&gt; foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
    return foldr(rlist, step, identity)(z)
</code></pre>

  <button id="toggleButton8">Toggle Solution</button>
  <div id="toggleText8" style="display: none">
    <pre><code>def foldl2(rlist, fn, z):
    def step(x, g):
        return lambda a: g(fn(a, x))
    return foldr(rlist, step, identity)(z)
</code></pre>

  </div>
<h3>Trees</h3>

<p>Trees are a way we have of representing a hierarchy of information. A family
tree is a good example of something with a tree structure. You have a matriarch
and a patriarch followed by all the descendants. Alternately, we may want to
organize a series of information geographically. At the very top, we have the
world, but below that we have countries, then states, then cities. We can also
decompose arithmetic operations into something much the same way.</p>

<p><img src="./firstTrees.png" alt="Trees" /></p>

<p>The name "tree" comes from the branching structure of the pictures, like real
trees in nature except that they're drawn with the root at the top and the
leaves at the bottom.</p>

<p>Terminology</p>

<ul>
<li><strong>node</strong>: a point in the tree. In these pictures, each node includes
a label (value at each node)</li>
<li><strong>root</strong>: the node at the top. Every tree has one root node children
the nodes directly beneath it. Arity is the number of children that
node has.</li>
<li><strong>leaf</strong>: a node that has no children. (Arity of 0!)</li>
</ul>

<h3>Binary Trees</h3>

<p>In this course, we will only be working with binary trees, where each node as at
most two children. For a general binary tree, order does not matter.
Additionally, the tree does not have to be balanced. It can be as lopsided as
one long chain.</p>

<p>Our implementation of binary trees can be found in <code>lab6.py</code>:</p>

<pre><code>class Tree:
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def copy(self):
        left = self.left.copy() if self.left else None
        right = self.right.copy() if self.right else None
        return Tree(self.entry, left, right)
</code></pre>

<p>We also included a function <code>tree_string</code>, which prints out a string
representation of a tree:</p>

<pre><code>&gt;&gt;&gt; print(tree_string(Tree(1, Tree(3, None, Tree(2)), Tree(4, Tree(5), Tree(6)))))
 -1-
/   \
3   4
 \ / \
 2 5 6
</code></pre>

<p><strong>Problem 10</strong>: Define the function <code>size_of_tree</code> which takes in a tree as an
argument and returns the number of non-empty nodes in the tree.</p>

<pre><code>def size_of_tree(tree):
    r""" Return the number of non-empty nodes in TREE
    &gt;&gt;&gt; print(tree_string(t)) # doctest: +NORMALIZE_WHITESPACE
        -4--
       /    \
       2    1-
      / \  /  \
     8  3  5  3
    /  / \   / \
    7  1 6   2 9
    &gt;&gt;&gt; size_of_tree(t)
    12
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton9">Toggle Solution</button>
  <div id="toggleText9" style="display: none">
    <pre><code>def size_of_tree(tree):
    if not tree:
        return 0
    return 1 + size_of_tree(tree.left) + size_of_tree(tree.right)
</code></pre>

  </div>
<p><strong>Problem 11</strong>: Define the function <code>deep_tree_reverse</code>, which takes a tree and
reverses the given order.</p>

<pre><code>def deep_tree_reverse(tree):
    r""" Reverses the order of a tree
    &gt;&gt;&gt; a = t.copy()
    &gt;&gt;&gt; deep_tree_reverse(a)
    &gt;&gt;&gt; print(tree_string(a)) # doctest: +NORMALIZE_WHITESPACE
       --4---
      /      \
      1-     2-
     /  \   /  \
     3  5   3  8
    / \    / \  \
    9 2    6 1  7
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton10">Toggle Solution</button>
  <div id="toggleText10" style="display: none">
    <pre><code>def deep_tree_reverse(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        deep_tree_reverse(tree.left)
        deep_tree_reverse(tree.right)
</code></pre>

  </div>
<p><strong>Problem 12</strong>: Define the function <code>filter_tree</code> which takes in a tree as an
  argument and returns the same tree, but with items included or excluded based
  on the pred argument.</p>

<p>Note that there is ambiguity about what excluding a tree means. For this
function, when you exclude a subtree, you exclude all of its children as well.</p>

<pre><code>def filter_tree(tree, pred):
    r""" Removes TREE if entry of TREE satisfies PRED
    &gt;&gt;&gt; a = t.copy()
    &gt;&gt;&gt; filtered = filter_tree(a, lambda x: x % 2 == 0)
    &gt;&gt;&gt; print(tree_string(filtered)) # doctest: +NORMALIZE_WHITESPACE
       4
      /
     2
    /
    8
    &gt;&gt;&gt; a = t.copy()
    &gt;&gt;&gt; filtered = filter_tree(a, lambda x : x &gt; 2)
    &gt;&gt;&gt; print(tree_string(filtered))
    4
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton11">Toggle Solution</button>
  <div id="toggleText11" style="display: none">
    <pre><code>def filter_tree(tree, pred):
    if tree and pred(tree.entry):
        return Tree(tree.entry,
                    filter_tree(tree.left, pred),
                    filter_tree(tree.right, pred))
</code></pre>

  </div>
<p><strong>Problem 13</strong>: Define the function <code>max_of_tree</code> which takes in a <code>tree</code> as an
  argument and returns the max of all of the values of each node in the tree.</p>

<pre><code>def max_of_tree(tree):
    r""" Returns the max of all the values of each node in TREE
    &gt;&gt;&gt; print(tree_string(t)) # doctest: +NORMALIZE_WHITESPACE
        -4--
       /    \
       2    1-
      / \  /  \
     8  3  5  3
    /  / \   / \
    7  1 6   2 9
    &gt;&gt;&gt; max_of_tree(t)
    9
    """
    "*** YOUR CODE HERE ***"
</code></pre>

  <button id="toggleButton12">Toggle Solution</button>
  <div id="toggleText12" style="display: none">
    <pre><code>def max_of_tree(tree):
    if not tree:
        return None
    return max(filter(lambda t: t is not None, (
        tree.entry,
        max_of_tree(tree.left),
        max_of_tree(tree.right)
        )))
</code></pre>

  </div>
<p></p>

  </body>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
  <script>
          $("#toggleButton0").click(function () {
        $("#toggleText0").toggle();
    });
          $("#toggleButton1").click(function () {
        $("#toggleText1").toggle();
    });
          $("#toggleButton2").click(function () {
        $("#toggleText2").toggle();
    });
          $("#toggleButton3").click(function () {
        $("#toggleText3").toggle();
    });
          $("#toggleButton4").click(function () {
        $("#toggleText4").toggle();
    });
          $("#toggleButton5").click(function () {
        $("#toggleText5").toggle();
    });
          $("#toggleButton6").click(function () {
        $("#toggleText6").toggle();
    });
          $("#toggleButton7").click(function () {
        $("#toggleText7").toggle();
    });
          $("#toggleButton8").click(function () {
        $("#toggleText8").toggle();
    });
          $("#toggleButton9").click(function () {
        $("#toggleText9").toggle();
    });
          $("#toggleButton10").click(function () {
        $("#toggleText10").toggle();
    });
          $("#toggleButton11").click(function () {
        $("#toggleText11").toggle();
    });
          $("#toggleButton12").click(function () {
        $("#toggleText12").toggle();
    });
      </script>
</html>
