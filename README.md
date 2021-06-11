# Toxic Liquid
## Function Description
Write a function liquid_distribution that distributes a hazardous liquid between special bottles.
The function accepts two parameters:
liters: integer
bottle_sizes: list

You have access to an unlimited amount of bottles of each of the provided sizes.
You must fill every chosen bottle completely.

Your function must return the minimum number of bottles needed to distribute all of the liquid.

Examples:
For liters = 18 and bottles = [1, 2, 5, 10],
the output should be
liquid_distribution(liters, bottles) = 4.

You have access to bottles with sizes 10, 5, 2, and 1, and will use one bottle of each size.

For liters = 9 and bottles = [1, 4, 6],
the output should be
liquid_distribution(liters, bottles) = 3.

You can use two bottles of size 4 and one bottle of size 1.

If there's no way to distribute the liquid as described above, return -1 instead.

## Analysis

The first approach to understanding the problem was hand-drawing the case of the function and the analysis of the first limitations or issues.

From this Analysis looks like a recursive function
### Doubts 
Empty set?
Recursivity?
Objects use?
Combinatory problem?

### Limitations 
- funtion only retorns a integer
- The function accepts two parameters: liters: integer; bottle_sizes: list
- use library? itertools

## Investigation
### Combinatory problem?
Rearch about the math problem 
Consulted resources: 

- [Combination Sum Problem](https://www.codeguru.com/cpp/cpp/algorithms/combinations/article.php/c15409/Dynamic-Programming-Combination-Sum-Problem.htm)
- [AMAZON CODING INTERVIEW QUESTION - COMBINATION SUM II ](https://www.youtube.com/watch?v=IER1ducXujU)
- [Combination Sum in Python](https://www.tutorialspoint.com/combination-sum-in-python)
### Prototype  


function liquid_distribution(liters, bottles)  

    return integer;  


class DistributionCalculator  

    - getCombinationSum  ()


function test_liquid_distribution()  

    (18, [1, 2, 5, 10]) == 4  

    (9, [1, 4, 6]) == 3  



<!-- ![notes]() -->
