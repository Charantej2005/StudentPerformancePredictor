# Function: `calculate_average_marks(data)`

## Purpose

The `calculate_average_marks()` function calculates the average marks of each student using the previously calculated **Total** marks. The calculated average is stored in a new column named **`Average`** in the DataFrame.

---

## Function Definition

```python
def calculate_average_marks(data):
```

### Explanation

- `def` is the Python keyword used to define a function.
- `calculate_average_marks` is the name of the function.
- `data` is a pandas DataFrame containing student records, including the `Total` column.

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `pandas.DataFrame` | A DataFrame containing student marks and the `Total` column. |

---

## Returns

| Return Value | Type | Description |
|--------------|------|-------------|
| `data` | `pandas.DataFrame` | Returns the updated DataFrame with a new `Average` column. |

---

## Complete Function

```python
def calculate_average_marks(data):
    """Calculates average marks."""

    data["Average"] = (data["Total"] / 5).round(2)

    print("Average marks calculated successfully.")

    return data
```

---

# Function Flow

```text
Input DataFrame
       │
       ▼
Read Total Marks
       │
       ▼
Divide by Number of Subjects (5)
       │
       ▼
Round to 2 Decimal Places
       │
       ▼
Create Average Column
       │
       ▼
Return Updated DataFrame
```

---

# Line-by-Line Explanation

## 1. Docstring

```python
"""Calculates average marks."""
```

### Purpose

The docstring briefly explains that the function calculates the average marks for each student.

---

## 2. Calculating the Average

```python
data["Average"] = (data["Total"] / 5).round(2)
```

This line calculates the average marks and stores the result in a new column named **`Average`**.

### Step 1: `data["Total"]`

Accesses the **Total** column from the DataFrame.

Example:

| Name | Total |
|------|------:|
| Alice | 435 |
| Bob | 365 |

---

### Step 2: `/ 5`

Since there are **5 subjects**, the total marks are divided by **5** to calculate the average.

Calculation:

```
Alice
435 ÷ 5 = 87

Bob
365 ÷ 5 = 73
```

If your project later includes more or fewer subjects, this value should be updated accordingly.

---

### Step 3: `.round(2)`

The `round()` function rounds the result to a specified number of decimal places.

Syntax:

```python
Series.round(decimals)
```

Example:

| Before | After |
|--------:|------:|
| 87.4567 | 87.46 |
| 73.1234 | 73.12 |
| 89.9999 | 90.00 |

Using `.round(2)` makes the output cleaner and easier to read.

---

### Step 4: `data["Average"]`

Creates a new column called **Average**.

Before:

| Name | Total |
|------|------:|
| Alice | 435 |
| Bob | 365 |

After:

| Name | Total | Average |
|------|------:|--------:|
| Alice | 435 | 87.00 |
| Bob | 365 | 73.00 |

---

## 3. Printing a Success Message

```python
print("Average marks calculated successfully.")
```

Displays a confirmation message indicating that the average marks have been calculated successfully.

---

## 4. Returning the Updated DataFrame

```python
return data
```

Returns the updated DataFrame so it can be used by the next functions, such as:

- `assign_grade()`
- `pass_fail_status()`

---

# Example

### Input

| Name | Total |
|------|------:|
| Alice | 435 |
| Bob | 365 |

### Processing

```
Alice
435 ÷ 5 = 87.00

Bob
365 ÷ 5 = 73.00
```

### Output

| Name | Total | Average |
|------|------:|--------:|
| Alice | 435 | 87.00 |
| Bob | 365 | 73.00 |

---

## Key Takeaways

- Calculates the average marks using the `Total` column.
- Divides the total marks by **5**, the number of subjects.
- Uses `.round(2)` to display values up to two decimal places.
- Creates a new `Average` column.
- Returns the updated DataFrame for further processing.
