# Function: `generate_rank(data)`

## Line-by-Line Explanation

```python
"""Generates rank based on total marks."""
```
Describes the purpose of the function.

```python
data = data.sort_values(
    by="Total",
    ascending=False
)
```
Sorts the DataFrame in descending order based on the **Total** marks.

```python
data["Rank"] = range(1, len(data) + 1)
This line creates a new **Rank** column and assigns rank numbers to each student.

- `len(data)` returns the total number of rows (students) in the DataFrame.
- `range(start, stop)` generates a sequence of numbers.
- `1` is the starting rank.
- `len(data) + 1` is used because the **stop value in `range()` is not included**
```
Creates a new **Rank** column starting from 1 up to the total number of students.

```python
print("Ranks generated successfully.\n")
```
Prints a success message.

```python
return data
```
Returns the updated DataFrame with the **Rank** column.
