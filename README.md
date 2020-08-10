# Kakuro
Kakuro or Kakkuro (Japanese: カックロ) is a kind of logic puzzle that is often referred to as a mathematical transliteration of the crossword. Kakuro puzzles are regular features in many math-and-logic puzzle publications across the world. In 1966,[1] Canadian Jacob E. Funk, an employee of Dell Magazines, came up with the original English name Cross Sums [2] and other names such as Cross Addition have also been used, but the Japanese name Kakuro, abbreviation of Japanese kasan kurosu (加算クロス, "addition cross"), seems to have gained general acceptance and the puzzles appear to be titled this way now in most publications. The popularity of Kakuro in Japan is immense, second only to Sudoku among Nikoli's famed logic-puzzle offerings.

## Objective
The objective of the puzzle is to insert a digit from 1 to 9 inclusive into each white cell such that the sum of the numbers in each entry matches the clue associated with it and that no digit is duplicated in any entry. It is that lack of duplication that makes creating Kakuro puzzles with unique solutions possible. Like Sudoku, solving a Kakuro puzzle involves investigating combinations and permutations. There is an unwritten rule for making Kakuro puzzles that each clue must have at least two numbers that add up to it, since including only one number is mathematically trivial when solving Kakuro puzzles.

## Files and Directories
- __kakuro.py__: contains my code and changes
- __description__: contains
    - a pdf with the project description (in Greek) and some exercises
    - a pdf with some remarks for the project and solutions to the given exercises
- all rest of the code come from AIMA github account https://github.com/aimacode/aima-python

## Execute
 <code> python3 kakuro.py </code>
 <p>In the begining, you'll be asked to choose the difficulty of the game (0,1,2,3 with 3 the most difficult) </p>

## Implementation remarks
- I noticed that there's a class names Kakuro(Nary) and I changed it in order to make constraints Binary and not Nary.This way I can use the already implemented functions in csp.py file
- Added and created the kakuro.py.In this file I made the class MyKakuro(CSP) that inherits from CSP and so I can use all the algorithms of csp.py
- Changed constructor init ,of class Kakuro, and added to MyKakuro <code>sums</code> data member that is a list of sums based on kakuro cells.Also I store the cells id in this </code>sum</code>
- Implemented a function <code>KakuroConstraints</code>,that checks if contraints are valid.Has specifically this format function(A,a,B.b) in order to be compitable with csp functions.
- I use the kakuro puzzles of AIMA
- Experiment with algorithms: __Backtracking, Backtracking με FC,Backtracking με FC και MRV, Backtracking με MAC ,AC3, AC4__

## Execution time
![Execution time](/execution_times.png)
___Time measurement unit : μs (microseconds)___

## Number of assignments
![Number of assignments](/numofAssignements.png)

## Remarks
- Backtracking algorithm without any metrics takes the most time to finish because in every step checks all the comninations.
- By adding FC,MRV,MAC we notice that the algorithm makes some prunning (look-aheads because of the constraints)
- Best algorithm is the backtracking-FC (with the most assignments although)

## Python version
In order to run the program you need at least python 3.3

**Online game** : http://www.kakuro.com
