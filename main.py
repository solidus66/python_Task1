orig_list = [1, 2, 6, 5, 6, 8, 6, 5, 7, 3]
print("\nOriginal list: " + str(orig_list) + "\n")

new_list = []
for element in orig_list:
    if element not in new_list:
        new_list.append(element)

print("List after removing duplicates: " + str(new_list))
