
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    words = {}
    for word in strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in words:
            words[sorted_word] = [word]
        elif sorted_word in words:
            words[sorted_word].append(word)
    
    unique_words = []
    for value in words.values():
        unique_words.append(value)
    
    return unique_words

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(n)
    """
    if len(nums) == 0:
        return []
    
    tally = {}
    for num in nums:
        if num in tally:
            tally[num] += 1
        else:
            tally[num] = 1
    
    nums_sorted_by_frequency = sorted(tally, key=tally.get, reverse=True)

    k_most_frequent = []
    for i in range(k):
        k_most_frequent.append(nums_sorted_by_frequency[i])

    return k_most_frequent 


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass



