def liquid_distribution(liters, bottles):
    '''
       liters: an integer value, litters of hazardous liquid. 
       bottles: an integer array, bottles sizes to distribute the substance
       return minValue: integer, minimum number of bottles needed to distribute all of the liquid
    '''
    calculator = DistributionCalculator()
    minValue = -1
    # validation for liters and bottles
    if(liters > 0 and len(bottles) > 0):
        # odd = 0
        # even = 0
        permissionToPass = 0
        # For optimization maybe could split bottles array to get a even and odd arrays
        if(liters % 2 == 0):
            for i in range(len(bottles)):
                if(bottles[i] % 2 == 0 and bottles[i] <= liters):
                    permissionToPass = 1
                    break
        else:
            for i in range(len(bottles)):
                if(bottles[i] % 2 != 0 and bottles[i] <= liters):
                    permissionToPass = 1
                    break

        if(permissionToPass == 1):
            # we can pass to combination algo only if we have a odd if litter is odd or if litter is even
            result = calculator.getCombinationSum(liters, bottles)
            # set min size
            minValue = len(result[0])
            for i in range(len(result)):
                if (len(result[i]) < minValue or minValue == -1):
                    minValue = len(result[i])
    return minValue


class DistributionCalculator(object):
    def getCombinationSum(self, sum_goal, set_integers):
        # Create list type from sequence of iterable elements with distinct elements
        set_integers = list(set(set_integers))
        combinations = []
        self.findCombinations(set_integers, sum_goal, combinations, {})
        return combinations

    def findCombinations(self, set_integers, sum_goal, combinations, unique, i=0, current=[]):
        if sum_goal == 0:  # found a comination
            temp = [i for i in current]
            temp_to_add = temp
            temp.sort()  # Sort the current set
            temp = tuple(temp)  # a tuple is an immutable sequence type.
            if temp not in unique:
                # chinkink if temp is in unique and if not we add the new combination
                unique[temp] = 1
                combinations.append(temp_to_add)
            return
        if sum_goal < 0:
            return

         # //go for the next elements for combination Could use doubly
        for x in range(i, len(set_integers)):
            current.append(set_integers[x])
            new_sum_goal = sum_goal - set_integers[x]
            self.findCombinations(set_integers, new_sum_goal,
                                  combinations, unique, i, current)
            current.pop(len(current)-1)

# TESTING

# Examples:
# For liters = 18 and bottles = [1, 2, 5, 10],
# the output should be
# liquid_distribution(liters, bottles) = 4.

# You have access to bottles with sizes 10, 5, 2, and 1, and will use one bottle of each size.

# For liters = 9 and bottles = [1, 4, 6],
# the output should be
# liquid_distribution(liters, bottles) = 3.


# You can use two bottles of size 4 and one bottle of size 1.
def testLiquid():
    # original test
    assert liquid_distribution(18, [1, 2, 5, 10]) == 4, "Should be 4"
    # imposible test: odd and even test
    assert liquid_distribution(127, [2, 4, 6, 8]) == -1, "Should be -1"
    # # original test
    assert liquid_distribution(9, [1, 4, 6]) == 3, "Should be 3"
    assert liquid_distribution(1, [1, 2, 7]) == 1, "Should be 1"
    # # empty liter test
    assert liquid_distribution(0, [1, 2, 7]) == -1, "Should be -1"
    # negative liter test
    assert liquid_distribution(-1, [1, 2, 7]) == -1, "Should be -1"
    print("Test passed")


# 444.702 seconds the worst
# Final time 0.339 second
testLiquid()
