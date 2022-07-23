"""
Symmetric difference is the opposite of intersection

Can only use the operators such as - & ^ with sets

Methods used
.symmetric_difference()
^=  is the .symmetric_difference_update() method

"""
morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}
morning_list = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon_list = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = morning ^ afternoon
print(possible_courses)

# Can pass any iterable to the method
possible_courses_list = set(morning_list).symmetric_difference(afternoon_list)
print(possible_courses_list)


