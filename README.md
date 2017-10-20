
# Application Architecture:

##### What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?

- Read file from input
- Clean input text from file
- Generate Histogram from input text
- Generate Stochastic sample from Histogram

##### Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?'

- define variable, modules and functions for single use case
- clearly define name to its functionality/purpose

##### What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?

- use local variables
- use classes

##### Are the functions small and clearly specified, with as few side effects as possible?

- make sure variables are contained within local scope
- make copies, rather than modify original

##### Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?

- use class to maintain state - such as a dictionary
- use methods to update, change state of properties within the class
- identify similarities amongst all classes - is there a base method each class will need, use inheritance.

##### Can files be used as both modules and as scripts?

- use main in each module, enable it to be used as a script

##### Do modules all depend on each other or can they be used independently?

- structure so that each is an extension
- read > normalize > histogram > stochastic | utility