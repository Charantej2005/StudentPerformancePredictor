# Function: `top_five_students(data)`

## Line-by-Line Explanation

```python
"""Displays top five students."""
```
Describes the purpose of the function.

---

```python
print("\nTop Five Students")
```

Prints the heading **Top Five Students**.

---

```python
print(data.nlargest(5, "Total"))
```

Displays the top **5 students** with the highest **Total** marks.

- `nlargest()` returns the rows with the largest values.
- `5` specifies the number of rows to return.
- `"Total"` is the column used for comparison.

### Syntax

```python
DataFrame.nlargest(number_of_rows, column_name)
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
data.nlargest(5, "Total")
```

Output:

| Name | Total |
|------|------:|
| Charlie | 470 |
| Alice | 435 |
| David | 420 |
| Eva | 410 |
| Frank | 390 |

---

```python
return data
```

Returns the original DataFrame.
