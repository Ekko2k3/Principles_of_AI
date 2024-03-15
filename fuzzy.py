def fuzzy_union(set1, set2):
    # Function to compute the fuzzy union of two fuzzy sets
    union_set = {}  # Initialize an empty dictionary to store the union set
    
    # Iterate through elements of set1
    for element in set1:
        # For each element in set1, store the maximum membership value between set1 and set2
        union_set[element] = max(set1[element], set2.get(element, 0))
        
    # Iterate through elements of set2
    for element in set2:
        # If an element in set2 is not in union_set, add it with its membership value
        if element not in union_set:
            union_set[element] = set2[element]
    
    return union_set  # Return the fuzzy union set

def fuzzy_intersection(set1, set2):
    # Function to compute the fuzzy intersection of two fuzzy sets
    intersection_set = {}  # Initialize an empty dictionary to store the intersection set
    
    # Iterate through elements of set1
    for element in set1:
        # If an element in set1 is also in set2, store the minimum membership value
        if element in set2:
            intersection_set[element] = min(set1[element], set2[element])
    
    return intersection_set  # Return the fuzzy intersection set

def display_fuzzy_set(fuzzy_set):
    # Function to display a fuzzy set
    print("{", end="")  # Start printing the fuzzy set with an opening brace
    for element, membership in fuzzy_set.items():
        print(f"{element}:{membership}", end="")  # Print each element and its membership value
    print("}")  # End printing the fuzzy set with a closing brace
    
# Define fuzzy sets set1 and set2
set1 = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
set2 = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'd': 0.9, 'e': 0.2}

# Display fuzzy set 1
print("Fuzzy set 1:")
display_fuzzy_set(set1)

# Display fuzzy set 2
print("Fuzzy set 2:")
display_fuzzy_set(set2)

# Compute and display the fuzzy union of set1 and set2
print("Fuzzy set union:")
union_set = fuzzy_union(set1, set2)
display_fuzzy_set(union_set)

# Compute and display the fuzzy intersection of set1 and set2
print("Fuzzy set intersection:")
intersection_set = fuzzy_intersection(set1, set2)
display_fuzzy_set(intersection_set)
