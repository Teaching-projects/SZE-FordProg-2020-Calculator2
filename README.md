# FordProgPY

The purpose of this assignment was to get a hands-on experience with one of the parser generators.
<br>
I wanted to experiment with Python - and at the time of creation - the most referred parsing tool was [PYL](https://www.dabeaz.com/ply/).
<br>
<br>
FordProgPY is capable of handling the below mentioned tasks:
  - Doing basic mathematic calculations.
  - Declaring and initializing integer and float type variables.
  - Assigning new value to a variable.
  - Understanding conditional statements.

## Tokens - Lexer

The first part of the project was to create the tokens we would like to use in our program.
<br>
The lexer's role is to divide the input into tokens.

## Abstract Syntax Tree - Parser
The parser's part is to do a syntax check on the input.

## Getting started
1. Downloading and installing Python (tested on v3.7.6).
   - [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
2. Cloning the repository.
   - $git clone https://github.com/Teaching-projects/SZE-FordProg-2020-Calculator2.git
3. Running the code with python
   - $python calculator.py
     - In order to exit from the program press Ctrl + C / Ctrl + Z

### Doing basic mathematic calculations
Below are examples with expected output.
```
$python calculator.py
>>1+2
3
>>1*2+3
2                     <-- result of 1 * 2
5                     <-- result of 2 + 3
>>1+3/2
1.5                   <-- result of 3 / 2
2.5                   <-- result of 1 + 1.5
```

### Declaring and initializing integer and float type variables
Exact syntax has to be followed else the declaration/initialization is going to be rejected.
```
>>a = 5;
a is an undeclared variable!
>>int a = 5;
Syntax error found!
>>integer a := 5;
Illegal character!
Syntax error found!
>>integer a = 5;                    <-- accepted initialization
Variable 'a' has a value as '5'
>>a                                 <-- printing the value of the variable 'a'
5
>>integer b = 2.5;
Variable 'b' has a value as '2'
>>b
2                                   <-- decimal value is going to be ignored, becase of the type
>>float c = 9.5
Variable 'c' has a value as '2.5'
>>c
9.5
```

### Assigning new value to a variable
Assume we already have a variable called 'a'.
<br>
By entering the correct input the program is able to redefine the value of 'a' no matter what was its previous value.
```
>>a = 1 + 2 * 3;
6                               <-- result of 2 * 3
7                               <-- result of 1 + 6
>>a
7                               <-- current value of 'a'
```

### Understanding conditional statements
Please note FordProgPY currently supports only inline conditional statements.
```
>>integer x = 5;
Variable 'x' has a value as '5'
>>if(x > 10){ x = 1; } else { x = 0; }
>>x                                       
0                                               <-- 0 is the expected output, because 5 > 10 is not true.
```

### "Complex" example

**Input:**
```
int x = 5;
x = 1 + 2 * 3;
if ( x > 10) {
  x = 1;
} else {
  x = 0;
}
print(x);
```
**Using the program to calculate the above example:**
```
>>integer x = 5;
Variable 'x' has a value as '5'
>>x
5
>>x = 1 + 2 * 3;
6
7
>>x
7
>>if ( x > 10 ) { x = 1; } else { x = 0; }
>>x                                                 
0                                                   <-- x's current value is 0, because 7 is less than 10.
```
### Reference:
  - [howCode's YoutTube channel - Making your Own Calculator in Python](https://www.youtube.com/watch?v=Hh49BXmHxX8&list=PLBOh8f9FoHHg7Ed_4yKhIbq4lIJAlonn8&index=1)
  - [Marcelo Andrade's blogpost about Writing your own programming language and compiler with Python on Medium](https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)
