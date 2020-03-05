# define our functions here

#1
# As a user, I can use the make_dough with water and wheat to make dough.

def make_dough(arg1, arg2):
    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    else:
        return 'not dough'
    # if argument 1 is water and argument 2 is flour
    # return dough
    # else return not dough



#2
# As a user, I can use the bake_dough with dough to get naan.

def bake_dough(arg1, arg2):
    if arg1 == 'bake_dough' and arg2 == 'dough':
        return 'naan'
    else:
        return 'not naan'
    # if argument 1 is bake and argument 2 is dough
    # return naan
    # else return not naan

#3
# As a user, I can use the run_factory with water and flour and get naan.

def run_factory(make_dough, bake_dough):
    if make_dough == 'dough' and bake_dough == 'naan':
    # if argument 1 is water and argument 2 is flour
    # return naan
    # else return not naan
        return 'baked naan'
# DONT CALL A FUNCTION HERE
# THIS WILL VIOLATE THE SEPARATION OF CONCERNS
# IT WILL RUN SAID FUNCTIONS WHEN YOU ARE IMPORTING THEM ELSEWHERE