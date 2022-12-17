#1. What is the result of the code, and explain?
#>>> X = 'iNeuron'
#>>> def func():
#print(X)
#>>> func()
#ans"- The Result of this code is iNeuron, it's because the function intially looks for the variable X in its local scope,But since there is no local variable X, its returns the value of global variable x ie iNeuron
X = 'iNeuron'
def func():
    print(X)
func()

#2. What is the result of the code, and explain?
#>>> X = 'iNeuron'
#>>> def func():
#X = 'NI!'
#>>> func()
#>>> print(X)

#ans:- The global variables are access in side the functions in python. But we can not access function variable out side function.
# Since x is golbal variable we are able to print it out side of the function solution = 'iNeuron'
X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)

#3. What does this code print, and why?
#>>> X = 'iNeuron'
#>>> def func():
#X = 'NI'
#print(X)
#>>> func()
#>>> print(X)

#ans:-The output of the code is NI and iNeuron. X=NI is in the local scope of the function func() hence the function prints the x value as NI. X = 'iNeuron' is in the global scope. hence print(X) prints output as iNeuron
X = 'iNeuron'
def func():
    X = 'NI'
    print(X)
func()
print(X)

#4. What output does this code produce? Why?
#>>> X = 'iNeuron'
#>>> def func():
#global X
#X = 'NI'
#>>> func()
#>>> print(X)

#ans:-The output of the code is NI. the global keyword allows a variable to be accessible in the current scope. since we are using global keyword inside the function func it directly access the variable in X in global scope. and changes its value to NI. hence the output of the code is NI

X = 'iNeuron'
def func():
    global X
    X = 'NI'
func()
print(X)

#5. What about this code—what’s the output, and why?
#>>> X = 'iNeuron'
#>>> def func():
#X = 'NI'
#def nested():
#print(X)
#nested()
#>>> func()
#>>> X

#ans:-the nested() function will print 'iNeuron', Then func() does not display anything,
# and x ='NI' is not accessible out
#side the function.
#Solution : 'iNeuron'

X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)

nested()
func()
X

#6. How about this code: what is its output in Python 3, and explain?
#>>> def func():
#X = 'NI'
#def nested():
#nonlocal X
#X = 'Spam'
#nested()
#print(X)
#>>> func()

#ans:-#Nonlocal variables are used in nested functions whose local scope is not defined.
#This means that the variable can be neither in the local nor the global scope. it print the updated value from nested
#function

def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)
func()