from csp import *
import sys
import time

# difficulty 0
kakuro1 = [['*', '*', '*', [6, ''], [3, '']],
           ['*', [4, ''], [3, 3], '_', '_'],
           [['', 10], '_', '_', '_', '_'],
           [['', 3], '_', '_', '*', '*']]

# difficulty 0
kakuro2 = [
    ['*', [10, ''], [13, ''], '*'],
    [['', 3], '_', '_', [13, '']],
    [['', 12], '_', '_', '_'],
    [['', 21], '_', '_', '_']]

# difficulty 1
kakuro3 = [
    ['*', [17, ''], [28, ''], '*', [42, ''], [22, '']],
    [['', 9], '_', '_', [31, 14], '_', '_'],
    [['', 20], '_', '_', '_', '_', '_'],
    ['*', ['', 30], '_', '_', '_', '_'],
    ['*', [22, 24], '_', '_', '_', '*'],
    [['', 25], '_', '_', '_', '_', [11, '']],
    [['', 20], '_', '_', '_', '_', '_'],
    [['', 14], '_', '_', ['', 17], '_', '_']]

# difficulty 2
kakuro4 = [
    ['*', '*', '*', '*', '*', [4, ''], [24, ''], [11, ''],
        '*', '*', '*', [11, ''], [17, ''], '*', '*'],
    ['*', '*', '*', [17, ''], [11, 12], '_', '_', '_',
        '*', '*', [24, 10], '_', '_', [11, ''], '*'],
    ['*', [4, ''], [16, 26], '_', '_', '_', '_', '_',
        '*', ['', 20], '_', '_', '_', '_', [16, '']],
    [['', 20], '_', '_', '_', '_', [24, 13], '_', '_', [
        16, ''], ['', 12], '_', '_', [23, 10], '_', '_'],
    [['', 10], '_', '_', [24, 12], '_', '_', [16, 5],
        '_', '_', [16, 30], '_', '_', '_', '_', '_'],
    ['*', '*', [3, 26], '_', '_', '_', '_', ['', 12],
        '_', '_', [4, ''], [16, 14], '_', '_', '*'],
    ['*', ['', 8], '_', '_', ['', 15], '_', '_',
        [34, 26], '_', '_', '_', '_', '_', '*', '*'],
    ['*', ['', 11], '_', '_', [3, ''], [17, ''], ['', 14],
        '_', '_', ['', 8], '_', '_', [7, ''], [17, ''], '*'],
    ['*', '*', '*', [23, 10], '_', '_', [3, 9], '_',
        '_', [4, ''], [23, ''], ['', 13], '_', '_', '*'],
    ['*', '*', [10, 26], '_', '_', '_', '_', '_',
        ['', 7], '_', '_', [30, 9], '_', '_', '*'],
    ['*', [17, 11], '_', '_', [11, ''], [24, 8], '_', '_',
        [11, 21], '_', '_', '_', '_', [16, ''], [17, '']],
    [['', 29], '_', '_', '_', '_', '_', ['', 7], '_',
        '_', [23, 14], '_', '_', [3, 17], '_', '_'],
    [['', 10], '_', '_', [3, 10], '_', '_', '*',
        ['', 8], '_', '_', [4, 25], '_', '_', '_', '_'],
    ['*', ['', 16], '_', '_', '_', '_', '*',
        ['', 23], '_', '_', '_', '_', '_', '*', '*'],
    ['*', '*', ['', 6], '_', '_', '*', '*', ['', 15], '_', '_', '_', '*', '*', '*', '*']]


class MyKakuro(CSP):

    # method init is almost the same as the init of class Kakuro in csp.py
    def __init__(self, puzzle):

        variables = []
        for i, line in enumerate(puzzle):
            # print line
            for j, element in enumerate(line):
                if element == '_':
                    var1 = str(i)
                    if len(var1) == 1:
                        var1 = "0" + var1
                    var2 = str(j)
                    if len(var2) == 1:
                        var2 = "0" + var2
                    variables.append("X" + var1 + var2)

        domains = {}

        for var in variables:
            domains[var] = set(range(1, 10))

        self.sums = []  # i added a list that is going to keep track of every sum and variables that need to be filled

        for i, line in enumerate(puzzle):
            for j, element in enumerate(line):
                if element != '_' and element != '*':
                    # down - column
                    if element[0] != '':
                        x = []
                        for k in range(i + 1, len(puzzle)):
                            if puzzle[k][j] != '_':
                                break
                            var1 = str(k)
                            if len(var1) == 1:
                                var1 = "0" + var1
                            var2 = str(j)
                            if len(var2) == 1:
                                var2 = "0" + var2
                            x.append("X" + var1 + var2)

                        self.sums.append((element[0], x))
                        # append at the list a tupple (sum,[list_of_positions in kakuro])
                    # right - line
                    if element[1] != '':
                        x = []
                        for k in range(j + 1, len(puzzle[i])):
                            if puzzle[i][k] != '_':
                                break
                            var1 = str(i)
                            if len(var1) == 1:
                                var1 = "0" + var1
                            var2 = str(k)
                            if len(var2) == 1:
                                var2 = "0" + var2
                            x.append("X" + var1 + var2)

                        self.sums.append((element[1], x))   # same as above

        neighbors = {}

        # for every variable in the list variables
        for v in variables:
            # i find calue into the dictionary neighbors
            
            neighbors[v] = []
            for s in self.sums:
                if v in s[1]:
                    # if that variable is in the list

                    neighbors[v] += s[1]
                    # del neighbors[v][neighbors[v].index(v)]
                    # remove that v from the list 
                    neighbors[v].remove(v)

        CSP.__init__(self, variables, domains,
                     neighbors, self.KakuroConstraints)

        # store puzzle
        self.puzzle = puzzle


    def KakuroConstraints(self, A, a, B, b):

        # --------- Checking if a and b are different -------------- #
        diff = different_values_constraint(A, a, B, b)

        if diff == False:
            return False

         # --------- Checking if sums are smaller , bigger or equal with wanted results in raws and lines -------------- #
        numbers_toSum = []
        tempValue = 0

        for s in self.sums:

            variables = s[1]    # a list of X-LINE-RAW that we want to sum the result
            wantedResult = s[0]     # an integer

            # if both X exist in list of variables that need to be filled
            if A in variables and B in variables:

                for var in variables:

                    # if it's A or B append it to the list 
                    if var == A:
                        numbers_toSum.append(a)
                    elif var == B:
                        numbers_toSum.append(b)
                    else:
                        
                        # if curr_domains dict is empty or has more than one 
                        if self.curr_domains == None or len(self.curr_domains[var]) > 1:
                            
                            tempValue += 1  # increment tempValue

                        # else add the only possible value that left in the domain to the list
                        elif len(self.curr_domains[var]) == 1:
                            
                            numbers_toSum.append(*self.curr_domains[var])

                # Calculate sum
                Sum = sum(numbers_toSum)

                if tempValue == 0:
                    # if tempValue is 0 , sum must be the wanted , either else constraint failed
                    if Sum == wantedResult:
                        return True
                    else:
                        return False
                
                else:
                    # if sum has overpassed the legible , constraint failed
                    if Sum <= wantedResult:
                        return True
                    else:
                        return False
        
        return True


    # display function is the same as that in Kakuro class in csp.py
    def display(self, assignment=None):
        for i, line in enumerate(self.puzzle):
            puzzle = ""
            for j, element in enumerate(line):
                if element == '*':
                    puzzle += "[*]\t"
                elif element == '_':
                    var1 = str(i)
                    if len(var1) == 1:
                        var1 = "0" + var1
                    var2 = str(j)
                    if len(var2) == 1:
                        var2 = "0" + var2
                    var = "X" + var1 + var2
                    if assignment is not None:
                        if isinstance(assignment[var], set) and len(assignment[var]) is 1:
                            puzzle += "[" + str(first(assignment[var])) + "]\t"
                        elif isinstance(assignment[var], int):
                            puzzle += "[" + str(assignment[var]) + "]\t"
                        else:
                            puzzle += "[_]\t"
                    else:
                        puzzle += "[_]\t"
                else:
                    puzzle += str(element[0]) + "\\" + str(element[1]) + "\t"
            print(puzzle)

difficulty = input("Select difficulty(0,1,2,3): ")
print()
if (difficulty == "0"):
    k = MyKakuro(kakuro1)
elif (difficulty == "1"):
    k = MyKakuro(kakuro2)
elif (difficulty == "2"):
    k = MyKakuro(kakuro3)
elif (difficulty == "3"):
    k = MyKakuro(kakuro4)
else:
    print("Input is an integer among 0 and 3")

print("-> Kakuro game (initial)")
k.display()
print()
print("____________ CSP algorithms ________________")
print()
print("1.Backtracking search:")
startOfAlgorithm = float(round(time.time()*1000))
result = backtracking_search(k)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

print()
print("2.Backtracking search with forward checking:")
startOfAlgorithm = float(round(time.time()*1000))
result = backtracking_search(k, inference=forward_checking)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

print()
print("3.Backtracking search with forward checking and MRV:")
startOfAlgorithm = float(round(time.time()*1000))
result = backtracking_search(k, select_unassigned_variable=mrv, inference=forward_checking)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

print()
print("4.Backtracking search with MAC:")
startOfAlgorithm = float(round(time.time()*1000))
result = backtracking_search(k, inference=mac)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

print()
print("5.AC3:")
startOfAlgorithm = float(round(time.time()*1000))
result = AC3(k)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

print()
print("6.AC4")
startOfAlgorithm = float(round(time.time()*1000))
result = backtracking_search(k, inference=forward_checking)
endOfAlgorithm = float(round(time.time()*1000))
print()
k.display(k.infer_assignment())
print("EXECUTION-TIME: %.2f " % (endOfAlgorithm-startOfAlgorithm))
print("ASSIGNMENTS: ",k.nassigns)

