# A sentence is defined as a string of space-separated words that starts with a capital letter followed by lowercase letters and spaces, and ends with a period. That is, it satisfies the regular expression ^[A-Z][a-z]*\.$. Rearrange the words in a sentence while respecting the following conditions:

# 1. Each word is ordered by length, ascending.

# 2. Words of equal length must appear in the same order as in the original sentence.

# 3. The rearranged sentence must be formatted to satisfy the regular expression A-Z][a-z].$

# Example

# sentence = Cats and hats.

# Order the sentence by word's length and keep the original order for the words with the same length.

# Length 3: (and)

# • Length 4: (Cats, hats)

# Reassemble the sequence of words so that the first letter is uppercase, the intermediate letters are lowercase, and the last one is a period.

# The result is 'And cats hats.'

# Function Description

# Complete the function arrange in the editor below.

# arrange has the following parameter(s): string sentence: a well formed sentence string Returns:

# Constraints

# string an formatted, rearranged sentence string

# • 1 s length of sentence < 105Input Format for Custom Testing

# Input from stdin will be processed as follows and passed to the function.

# A single line of space-separated words, sentence.

# ▾ Sample Case 0

# Sample Input 0

# STDIN

# Function

# The lines are printed in reverse order. → sentence = 'The lines are printed in reverse order.'

# Sample Output 0

# In the are lines order printed reverse.

# Explanation 0

# Order the sentence by the lengths of the words and keep the original order for the words with the same length.

# • Length 2: (in)

# Length 3: (the, are). same length, keep the original order.

# Length 5: (lines, order), same length, keep the original order. Length 7: (printed, reverse), same length, keep the original order.

# Reassemble the sequence of words so that the first letter is uppercase, the intermediate letters are lowercase, and the last one is a period.

# The result is' In the are lines order printed reverse.'

# Sample Case 1 Sample Input 1

# STDIN

# Function

# Here come.

# Sample Output 1

# sentence = 'Here i come."

# →

# I here comeExplanation 1 Order the sentence by the lengths of the words and keep the original order for the words with the same length.

# • Length 1: (1)

# • Length 4: (here, come}

# Reassemble the sequence of words so that the first letter is uppercase, the intermediate letters are lowercase, and the last one is a period.

# The result is I here come!.

# ▾ Sample Case 2

# Sample Input 2

# STDIN

# Function

# I love to code.

# sentence

# →

# = 'I love to code.'

# Sample Output 2

# I to love code.

# Explanation 2

# Order the sentence by the lengths of the words and keep the original order for the words with the same length.

# • Length 1: (1)

# • Length 2: (to)

# • Length 4: (love, code)

# Reassemble the sequence of words so that the first letter is uppercase, the intermediate letters are lowercase, and the last one is a period.

# The result is 'I to love code."

# implementation


def arrange(sentence):
#   
#   # Write your code here
    words = sentence.split()
    words.sort(key=len)
    words = [word.lower() for word in words]
    words[0] = words[0].capitalize()
    words[-1] = words[-1][:-1]
    # if len(words) == 1:
    #     return words[0]
    if words[-3].endswith('.'):
  
        words[-3] = words[-3][:-1]
    return ' '.join(words) + '.'
#
# sentence="Cats and hats."
sentence = "The lines are printed in reverse order."
out = arrange(sentence)
print(out)
