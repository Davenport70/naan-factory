# Import naan factory functions
# Define and run tests

from naan_factory_functions import *

#1
# As a user, I can use the make_dough with water and flour to make dough.
print('make_dough with water and flour, expect dough as a result')
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

print('')

print('make_dough with water and cement, expect cement as a result')
print(make_dough('water', 'cement') == ' not dough')
print('got:', make_dough('water', 'cement'))

#2
# As a user, I can use the bake_dough with dough to get naan.
print('bake_dough with dough , expect naan as a result')
print(bake_dough('bake_dough', 'dough') == 'naan')
print('got:', bake_dough('bake_dough', 'naan'))




#3
# As a user, I can use the run_factory with water and flour and get baked naan.
print('run_factory with water and flour, expect baked naan as a result')
print(run_factory('water', 'flour') == 'baked naan')
print('got:', run_factory('water', 'flour'))