ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

# What you should see

# Wait there's not 10 things in that list, let's fix that.
# Adding:  Boy
# There's 7 items now.
# Adding:  Girl
# There's 8 items now.
# Adding:  Banana
# There's 9 items now.
# Adding:  Corn
# There's 10 items now.
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do some things with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone#Light

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

# >>> # Replace some items:
# ... a[0:2] = [1, 12]
# >>> a
# [1, 12, 123, 1234]
# >>> # Remove some:
# ... a[0:2] = []
# >>> a
# [123, 1234]
# >>> # Insert some:
# ... a[1:1] = ['bletch', 'xyzzy']
# >>> a
# [123, 'bletch', 'xyzzy', 1234]
# >>> # Insert (a copy of) itself at the beginning
# >>> a[:0] = a
# >>> a
# [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
# >>> # Clear the list: replace all items with an empty list
# >>> a[:] = []
# >>> a
# []

# It is possible to nest lists (create lists containing other lists), for example:

# >>> q = [2, 3]
# >>> p = [1, q, 4]
# >>> len(p)
# 3
# >>> p[1]
# [2, 3]
# >>> p[1][0]
# 2
# >>> p[1].append('xtra')     # See section 5.1
# >>> p
# [1, [2, 3, 'xtra'], 4]
# >>> q
# [2, 3, 'xtra']

