# Function: `calculate_total_marks(data)`

## Purpose

The `calculate_total_marks()` function calculates the total marks obtained by each student by adding the marks from all subjects. The calculated value is stored in a new column named **`Total`** in the DataFrame.

---

## Function Definition

```python
def calculate_total_marks(data):
```

### Explanation

- `def` is the Python keyword used to define a function.
- `calculate_total_marks` is the function name.
- `data` is a pandas DataFrame containing student records and subject marks.

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `pandas.DataFrame` | Contains student information and subject marks. |

---

## Returns

| Return Value | Type | Description |
|--------------|------|-------------|
| `data` | `pandas.DataFrame` | Returns the updated DataFrame with a new `Total` column. |

---

## Complete Function

```python
def calculate_total_marks(data):
    """Calculates total marks of each student."""

    subjects = [
        "Maths",
        "Physics",
        "Chemistry",
        "English",
        "Computer_Science"
    ]

    data["Total"] = data[subjects].sum(axis=1)

    print("\nTotal marks calculated successfully.")

    return data
```

---

# Line-by-Line Explanation

## 1. Docstring

```python
"""Calculates total marks of each student."""
```

### Purpose

A **docstring** describes what the function does. It helps developers understand the function without reading the implementation.

---

## 2. Creating the Subject List

```python
subjects = [
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Computer_Science"
]
```

### Explanation

A Python list is created to store the names of all subject columns.

Using a list makes the code cleaner and easier to maintain. If a new subject is added later, only this list needs to be updated.

Example:

```python
subjects = [
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Computer_Science",
    "Biology"
]
```

No other part of the function needs to be changed.

---

## 3. Calculating Total Marks

```python
data["Total"] = data[subjects].sum(axis=1)
```

This line calculates the total marks for every student.

### Step 1: `data`

`data` is a pandas DataFrame containing student records.

Example:

| Name | Maths | Physics | Chemistry | English | Computer_Science |
|------|------:|--------:|----------:|---------:|-----------------:|
| Alice | 90 | 85 | 80 | 88 | 92 |
| Bob | 70 | 75 | 68 | 80 | 72 |

---

### Step 2: `subjects`

`subjects` is a list containing the names of the subject columns.

```python
[
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Computer_Science"
]
```

Selecting these columns:

```python
data[subjects]
```

returns:

| Maths | Physics | Chemistry | English | Computer_Science |
|------:|--------:|----------:|---------:|-----------------:|
| 90 | 85 | 80 | 88 | 92 |
| 70 | 75 | 68 | 80 | 72 |

---

### Step 3: `.sum(axis=1)`

The `sum()` function adds numerical values.

Syntax:

```python
DataFrame.sum(axis)
```

`axis` specifies the direction of the operation.

- `axis=0` → Adds values vertically (column-wise).
- `axis=1` → Adds values horizontally (row-wise).

Since we want the total marks for each student, we use:

```python
axis=1
```

Calculation:

```
Alice
90 + 85 + 80 + 88 + 92 = 435

Bob
70 + 75 + 68 + 80 + 72 = 365
```

---

### Step 4: `data["Total"]`

A new column named **`Total`** is created to store the calculated marks.

Before:

| Name | Maths | Physics |
|------|------:|--------:|
| Alice | 90 | 85 |

After:

| Name | Maths | Physics | Total |
|------|------:|--------:|------:|
| Alice | 90 | 85 | 435 |

---

## 4. Printing a Success Message

```python
print("\nTotal marks calculated successfully.")
```

Displays a confirmation message after the calculation is completed.

The `\n` creates a blank line before the message, making the terminal output easier to read.

---

## 5. Returning the Updated DataFrame

```python
return data
```

Returns the updated DataFrame so that it can be used by other functions in the project, such as:

- `calculate_average_marks()`
- `assign_grade()`
- `pass_fail_status()`

---

# Example

### Input

| Name | Maths | Physics | Chemistry | English | Computer_Science |
|------|------:|--------:|----------:|---------:|-----------------:|
| Alice | 90 | 85 | 80 | 88 | 92 |
| Bob | 70 | 75 | 68 | 80 | 72 |

### Processing

```
Alice
90 + 85 + 80 + 88 + 92 = 435

Bob
70 + 75 + 68 + 80 + 72 = 365
```

### Output

| Name | Total |
|------|------:|
| Alice | 435 |
| Bob | 365 |

---

## Key Takeaways

- Calculates the total marks for each student.
- Uses a Python list to select multiple subject columns.
- Uses `sum(axis=1)` to perform row-wise addition.
- Creates a new `Total` column in the DataFrame.
- Returns the updated DataFrame for use in later processing steps.
