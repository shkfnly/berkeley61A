data = create_data()
def print_all(data):

  for elem in data:
    print(elem)

while data.current != None:
  print data.current
  data.next


  def get_name(object):
    types = type_tag(object)
    return name_imp([types](object)


name_imp = {}
name_imp[('KM')] = lambda x: x.student_info[0]
name_imp[('JO')] = lambda x: x.student_info['name']

grade_imp = {}
grade_imp[('KM')] = lambda x: x.student_info[1]
grade_imp[('KO')] = lambda x: x.student_info['grade']



grade_info_imp = {}
grade_info_imp[('KM')] = lambda x: x.grade_info[0]
grade_info_imp[('JO')] = lambda x: x.grade_info
def compute_average_total(list):
  total = 0
  for elem in list:
    types = type_tag(elem)
    total += grade_info_imp[types](elem)
  return total/len(list)

  1, 4, 6  'look up answers', 7 (11/12), 8(11/21), 9, 10, 11(11/19)

  Monday Nov 18th

Need help with trees to ordered sequence and partial trees

And the Mario Question
 def ways(n):
        if n == len(level)-1:
            return 1
        if n >= len(level) or level[n] == 'P':
            return 0
        return ways(n+1) + ways(n+2)
    return ways(0)

Pair('+', Pair(1, Pair(2, Pair(Pair(-, Pair(3, Pair(4, nil))), nil))))

Pair('+', Pair(Pair('*', Pair(2, Pair(3, nil))), nil), Pair(4, nil))

1.4
5 , 1

7, 3

elif operator == '-':
  try:
      while len(args) > 1:

  except (Error Type)   *** I don't know***'
      print('Must provide one argument')

elif operator =='/':
  try:
    while len(args) > 2:
      return args.first / args.second
    except ZeroDivisionError

