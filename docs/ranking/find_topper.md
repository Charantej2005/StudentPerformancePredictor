# Function: `find_topper(data)`

## Line-by-Line Explanation

```python
"""Displays the overall topper."""
```
Describes the purpose of the function.

---

```python
topper = data.loc[data["Total"].idxmax()]
```

Finds the student with the highest **Total** marks.

- `data["Total"]` selects the **Total** column.
- `idxmax()` returns the index of the highest value in the **Total** column.
- `loc[]` retrieves the complete row at that index.
- The row is stored in the `topper` variable.

### Example

Suppose the DataFrame is:

| Index | Name | Total |
|------:|------|------:|
| 0 | Alice | 435 |
| 1 | Bob | 365 |
| 2 | Charlie | 470 |

```python
data["Total"].idxmax()
```

Output:

```text
2
```

Then,

```python
data.loc[2]
```

returns:

| Name | Total |
|------|------:|
| Charlie | 470 |

This row is stored in `topper`.

---

```python
print("\nOverall Topper")
```

Prints the heading **Overall Topper**.

---

```python
print(topper)
```

Displays the topper's complete details.

---

```python
return topper
```

Returns the topper's data.
