import pandas as pd


def dataset_analysis(data):
    """Displays basic information about the dataset."""

    print("\nShape of Dataset:")
    print(data.shape)

    print("\nColumns:")
    print(data.columns.tolist())

    print("\nData Types:")
    print(data.dtypes)


def numerical_summary(data):
    """Displays statistical summary."""

    print("\nStatistical Summary:")
    print(data.describe())


def missing_values(data):
    """Displays missing values."""

    print("\nMissing Values:")
    print(data.isnull().sum())


def unique_value(data):
    """Displays the number of unique values in each column."""

    print("\nUnique Values:")

    for column in data.columns:
        print(f"{column}: {data[column].nunique()}")
