def min_moves_to_minimize_length(word):
    first_occurrence = {}

    for i, char in enumerate(word):
        if char not in first_occurrence:
            first_occurrence[char] = i

    total_moves = 0

    for i, char in enumerate(word):
        left_distance = i - first_occurrence[char]
        
        right_distance = len(word) - 1 - i - (len(word) - 1 - word.rindex(char))
        
        total_moves += min(left_distance, right_distance)

    return total_moves

