#  All participants must be grouped into teams where each team has exactly two candidates and the sum of their skill must be equal for all the teams.
# The efficiency of a team is the productof the skills of its members, e.g. for a team with skills [2, 3], theefficiency of the team is 2* 3 = 6
#  The skill of a team is the sum of the skill of its members.
#  Find the sum of the efficiencies of the teams, if there is no way to create a team that satisfy the conditions, return -1.

# Rephrase:
#  Given a list of integers, find all possible combinations of two integers that sum to the same value.
# Return the sum of the efficiencies of the teams, if there is no way to create a team that satisfy the conditions, return -1.

# Examples:
#  Input: [1, 2, 3, 4, 5, 6]
#  Output: 60

#  Input: [1, 1, 1, 1, 1, 1]
#  Output: 3

# Edge Cases:
# The list can be empty
# The list can contain duplicates
# The list can contain only one number

# Approach:
# 1. Create a dictionary to store the number of times each number appears in the list
# 2. Create a list of all possible combinations of two numbers that sum to the same value
# 3. For each combination, calculate the efficiency of the team
# 4. Return the sum of the efficiencies of the teams, if there is no way to create a team that satisfy the conditions, return -1.


# Solution:
def solution(skills):
    efficiency = 0
    left= 0
    right = len(skills) - 1
    skills.sort()
    if len(skills) < 2:
        return -1
    if len(skills) == 2:
        return skills[0] * skills[1]
    if len(skills) > 2:
        while left<right:
            if skills[left] + skills[right] != skills[left] + skills[right]:
                return -1
            else:
                efficiency += skills[left] * skills[right]
                left += 1
                right -= 1
        return efficiency




out = solution([1, 3,2,2])
print(out)