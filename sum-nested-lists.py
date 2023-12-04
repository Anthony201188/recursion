## Write a recursive function to find the sum of all elements in a nested list.

def sum_nested_list(nested_list):
    total_sum = 0
    for element in nested_list: #iterates nested list
        if isinstance(element, list): # opens the nested lists and iterated over them, then in the next line adds them to total_sum
            total_sum += sum_nested_list(element) # "sum_nested_list(element)" is like an address to find element with the function name as the stree name and the element as the door number"
        else:
            total_sum += element # adds the sum of all non nested elements
    return total_sum

# Testing the function
nested = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]
result = sum_nested_list(nested)
print(f"The sum of elements in the nested list is {result}.")