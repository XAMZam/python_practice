#Variable naming *rules of variable;
#1. variable must start with an alphabet number(-z or A-Z) or underscore(_). example; abc or _abc
#2. variable must not start with a number. example; 1abc
#3. the first character can be followed by number(0-9),alphabet and underscore(_) example; abc123 or _abc123
#underscore(_)is the only special character.
#4. variable name are case sensitive.example a100 is different from A100
#5. Reserved words cannot be used as variable name. example;help("keywords")

#snake_case-should be used for functions and variable names.
number_of_college_graduates = 2500
#MACRO_CASE
NUMBEROFCOLLEGEGRADUATES =2500
#camelCase
numberOfCollegeGraduates= 2500
#Pascal_Case- should be used for class names.
NumberOfCollegeGraduates = 2500
print(number_of_college_graduates,NUMBEROFCOLLEGEGRADUATES,numberOfCollegeGraduates,NumberOfCollegeGraduates)


#list of the Python keywords
help("keywords")
#Python Indentation
help('lambda')