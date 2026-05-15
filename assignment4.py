# Python Lists Assignment (Beginner Level)
# 1. Create a list of 5 fruits and print the list.
fruits = ["Watermelon", "Apple", "Banana", "Grapes", "Mango"]
print(fruits)
# 2. Add a new fruit to the end of the list using append().
fruits.append("Cherry")
print(f"the updated list is {fruits}")
# 3. Insert a fruit at position 2 in your list.
fruits.insert(2, "Pear")
print(f"the updated list is {fruits}")
# 4. Remove the last item from the list using pop().
fruits.pop()
print(f"the updated list is {fruits}")
# 5. Remove a specific fruit from the list using remove().
fruits.remove("Pear")
print(f"the updated list is {fruits}")
# 6. Create a list of numbers and sort it in ascending order.
numbers = [3, 5, 1, 4, 2, 6, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.sort()
print(f"the sorted list is {numbers}")
# 7. Reverse the order of a list using reverse().
numbers.reverse()
print(f"the reversed list is {numbers}")
# 8. Count how many times a number appears in a list using count().
count = numbers.count(4)
print(f"The number 4 appears {count} times in the list.")
# 9. Find the index of a specific element in a list using index().
index = numbers.index(5)
print(f"the index of 5 is {index}")
# 10. Create two lists and combine them into one list.
list1 = ["Watermelon", "Apple", "Banana", "Grapes", "Mango"]
list2 = [3, 5, 1, 4, 2, 6, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
combined_list = list1 + list2
print(combined_list)