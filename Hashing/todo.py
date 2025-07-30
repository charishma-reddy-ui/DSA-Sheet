# 🔗 Hashing with Chaining Problems
# 1. Insert and Search in Hash Table (Using Chaining)
# Q: Design a hash table using chaining (linked list). Support:

# insert(val)

# search(val)

# 📌 Use val % 10 as hash function.

# Input Example:

# python
# Copy
# Edit
# insert(10)
# insert(20)
# insert(25)
# search(20)  # Found
# search(15)  # Not Found
# 2. Delete a Value from Hash Table (Chaining)
# Q: Extend your chaining-based hash table to support delete(val).

# Example:

# python
# Copy
# Edit
# insert(10)
# insert(20)
# delete(10)
# search(10)  # Should print Not Found
# 🧠 Try deleting from:

# Beginning of the linked list

# Middle

# End

# 3. Count Elements at a Particular Index
# Q: After inserting some values in the hash table, write a function to count how many values are stored at a particular index.

# Example:

# python
# Copy
# Edit
# insert(10)
# insert(20)
# insert(30)
# # All go to index 0 (if using mod 10)

# countAtIndex(0)  # Output: 3
# 4. Print All Keys in Sorted Order
# Q: After inserting values, print all elements in sorted order.

# 📌 Since hash table is unordered, this will test if you can:

# Traverse all linked lists

# Store elements in a new array

# Sort and print