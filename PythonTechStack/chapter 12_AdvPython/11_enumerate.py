#Enumerate in python imp:
'''
enumerate() is a built-in Python function that takes a collection (like a list, tuple, or string)
and returns both the index (counter) and the value at the same time during a loop.

Instead of manually maintaining a counter variable, enumerate() tracks it for you
'''

# fruits = ["apple", "banana", "mango"]

# # Needing both index and item without enumerate
# i = 0
# for fruit in fruits:
#     print(i, fruit)
#     i += 1

#can be simplied into : using enumerate
fruits = ["apple", "banana", "mango"]

for i, fruit in enumerate(fruits):
    print(f"The fruit at {i} position is {fruit}")

'''
VV IMP THEORY

### Top 4 Real-World & DSA Uses

#### 1. Custom Starting Index (1-based ranking / numbered lists)

You can pass a second argument `start=` so counting doesn't have to start at `0`.

```python
tasks = ["Write code", "Test edge cases", "Deploy"]

for rank, task in enumerate(tasks, start=1):
    print(f"{rank}. {task}")
# Output:
# 1. Write code
# 2. Test edge cases
# 3. Deploy

```

#### 2. Storing Indices in Hash Maps (Essential for DSA)

In problems like **Two Sum**, you must remember each number's position while iterating:

```python
nums = [2, 7, 11, 15]
seen = {}

for index, val in enumerate(nums):
    seen[val] = index  # Maps {2: 0, 7: 1, 11: 2, 15: 3}

```

#### 3. In-Place Modifications of a List

When you need to update a list based on both the item and its position:

```python
scores = [45, 82, 33, 90]

for i, score in enumerate(scores):
    if score < 40:
        scores[i] = 40  # Directly replace failing scores using the index

print(scores)  # [45, 82, 40, 90]

```

#### 4. Iterating Strings with Character Positions

Handy for parsing strings or validating parentheses/syntax:

```python
word = "code"

for idx, char in enumerate(word):
    print(f"Character '{char}' is at index {idx}")

```
'''