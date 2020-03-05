# TDD Naan Factory Exercise

## This exercise is going to bring together a lot of concepts. They are
- Git
- GitHub
- Functions
- TDD
- Seperation of concerns
- DRY code
- DOD
## Installing and running
To run the factory, do the following
```python
import naan_factory
run naan_factory()
```

### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

#### Unit Tests

Tests single pieces of code. Like a function.

**base of a test**
test usually has 3 phases.
- setup phase (known variables)
- calling of the function / piece of code with known variables
- asserting for expected output

### User stories for Naan Factory

```
#1
As a user, I can use the make_dough with water and wheat to make dough.

#2
As a user, I can use the bake_dough with dough to get naan.

#3 
As a user, I can use the run_factory with water and flour and get naan. 

```
