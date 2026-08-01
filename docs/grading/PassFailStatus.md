# Function: `pass_fail_status(data)`

## Line-by-Line Explanation

```python
"""Determines pass/fail status."""
```
Describes the purpose of the function.

```python
result = []
```
Creates an empty list to store the result.

```python
for average in data["Average"]:
```
Loops through each student's average marks.

```python
if average >= 35:
    result.append("Pass")
else:
    result.append("Fail")
```
Checks whether the student has passed or failed based on the average marks.

```python
data["Result"] = result
```
Adds the result as a new **Result** column in the DataFrame.

```python
print("Pass/Fail status generated successfully.")
```
Prints a success message.

```python
return data
```
Returns the updated DataFrame.
