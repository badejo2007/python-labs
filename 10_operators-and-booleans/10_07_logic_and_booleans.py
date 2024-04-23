# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

do_two_wrongs_make_right = (not(wrong and wrong)) or (right and wrong)# Combine with logical operators

print(do_two_wrongs_make_right)
