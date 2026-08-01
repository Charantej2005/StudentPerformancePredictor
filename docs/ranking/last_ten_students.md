# Function: `bottom_five_students(data)`

## Line-by-Line Explanation

```python
"""Displays bottom five students."""
```
Describes the purpose of the function.

---

```python
print("\nBottom Five Students")
```

Prints the heading **Bottom Five Students**.

---

```python
print(data.nsmallest(5, "Total"))
```

Displays the bottom **5 students** with the lowest **Total** marks.

- `nsmallest()` returns the rows with the smallest values.
- `5` specifies the number of rows to return.
- `"Total"` is the column used for comparison.

### Syntax

```python
DataFrame.nsmallest(number_of_rows, column_name)
```

### Example

Suppose the DataFrame is:

| Name | Total |
|------|------:|
| Alice | 435 |
| Bob | 365 |
| Charlie | 470 |
| David | 420 |
| Eva | 410 |
| Frank | 390 |

```python
data.nsmallest(5, "Total")
```

Output:

| Name | Total |
|------|------:|
| Bob | 365 |
| Frank | 390 |
| Eva | 410 |
| David | 420 |
| Alice | 435 |

---

```python
return data
```

Returns the original DataFrame.
