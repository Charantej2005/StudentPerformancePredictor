import os


def display_separator():
    """Displays a separator line."""

    print("-" * 60)


def display_title(title):
    """Displays a formatted title."""

    display_separator()
    print(title.upper())
    display_separator()


def check_file_exists(file_path):
    """Checks whether the given file exists."""

    if os.path.exists(file_path):
        return True

    print(f"Error: File not found -> {file_path}")
    return False
