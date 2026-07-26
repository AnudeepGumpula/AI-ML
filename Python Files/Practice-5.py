"""
==================================================================
NumPy & Pandas - Core Methods 
==================================================================

Install first if needed (run in terminal, not here):
    pip install numpy pandas
    or (Anaconda):
    conda install numpy pandas
"""

import numpy as np
import pandas as pd


# ==================================================================
# PART 1: NUMPY

# 1. CREATING ARRAYS
# ============================================

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))            # numpy.ndarray

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# Common array creation shortcuts
print(np.zeros(5))          # [0. 0. 0. 0. 0.]
print(np.ones((2, 3)))      # 2x3 array of 1s
print(np.full((2, 2), 7))   # 2x2 array filled with 7
print(np.arange(1, 10, 2))  # [1 3 5 7 9] - like range(), but returns array
print(np.linspace(0, 1, 5)) # 5 evenly spaced values between 0 and 1
print(np.eye(3))            # 3x3 identity matrix

# Random arrays (very common for practice/testing)
print(np.random.rand(3))          # 3 random floats between 0-1
print(np.random.randint(1, 100, 5))  # 5 random ints between 1-100


# ============================================
# 2. ARRAY PROPERTIES
# ============================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)     # (2, 3) - rows, columns
print(arr.ndim)       # 2 - number of dimensions
print(arr.size)       # 6 - total number of elements
print(arr.dtype)      # data type of elements (e.g. int64)


# ============================================
# 3. INDEXING & SLICING
# ============================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])          # 10
print(arr[-1])         # 50
print(arr[1:4])        # [20 30 40]

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 1])      # row 0, col 1 -> 2
print(arr2d[:, 1])      # all rows, col 1 -> [2 5 8]
print(arr2d[1, :])      # row 1, all cols -> [4 5 6]

# Boolean indexing / filtering (very commonly used)
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[arr > 3])     # [4 5 6]


# ============================================
# 4. RESHAPING
# ============================================

arr = np.arange(1, 13)          # [1..12]
reshaped = arr.reshape(3, 4)    # reshape into 3 rows, 4 cols
print(reshaped)

flattened = reshaped.flatten()  # back to 1D
print(flattened)


# ============================================
# 5. MATH OPERATIONS (element-wise, no loops needed)
# ============================================

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)     # [11 22 33]
print(a - b)     # [-9 -18 -27]
print(a * b)     # [10 40 90]
print(a / b)     # [0.1 0.1 0.1]
print(a ** 2)    # [1 4 9]

# Scalar operations (applied to every element)
print(a * 10)    # [10 20 30]


# ============================================
# 6. AGGREGATE / STATISTICAL FUNCTIONS
# ============================================

arr = np.array([4, 8, 2, 9, 1, 7])

print(np.sum(arr))       # 31
print(np.mean(arr))      # average
print(np.median(arr))    # median
print(np.std(arr))       # standard deviation
print(np.var(arr))       # variance
print(np.min(arr))       # smallest value
print(np.max(arr))       # largest value
print(np.argmin(arr))    # INDEX of smallest value
print(np.argmax(arr))    # INDEX of largest value
print(np.sort(arr))      # sorted array (returns new array)


# For 2D arrays - specify axis (0 = columns, 1 = rows)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr2d, axis=0))   # sum down each COLUMN -> [5 7 9]
print(np.sum(arr2d, axis=1))   # sum across each ROW -> [6 15]


# ============================================
# 7. USEFUL NUMPY FUNCTIONS
# ============================================

arr = np.array([1, 2, 3, 4, 5])

print(np.where(arr > 3, "High", "Low"))   # conditional labeling
print(np.unique([1, 2, 2, 3, 3, 3]))      # unique values -> [1 2 3]
print(np.concatenate([arr, [6, 7]]))       # join arrays
print(np.isnan(np.array([1, np.nan, 3])))  # check for NaN values


# ==================================================================
# PART 2: PANDAS

# 8. CREATING SERIES & DATAFRAMES
# ============================================

# Series - a single column of labeled data
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
print(s["b"])    # 20

# DataFrame - a table (rows + columns), the main pandas structure
data = {
    "name": ["John", "Mary", "Alex"],
    "age": [21, 22, 23],
    "score": [85, 92, 78]
}
df = pd.DataFrame(data)
print(df)


# ============================================
# 9. READING/WRITING DATA (very common in real projects)
# ============================================

# df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")
# df = pd.read_json("data.json")

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)


# ============================================
# 10. EXPLORING A DATAFRAME
# ============================================

print(df.head())        # first 5 rows (default)
print(df.head(2))       # first 2 rows
print(df.tail(2))       # last 2 rows
print(df.shape)          # (rows, columns)
print(df.columns)        # column names
print(df.index)          # row index
print(df.dtypes)         # data type of each column
print(df.info())         # summary: types, non-null counts, memory
print(df.describe())     # statistical summary (mean, std, min, max, etc.)


# ============================================
# 11. SELECTING DATA
# ============================================

print(df["name"])            # single column -> Series
print(df[["name", "age"]])   # multiple columns -> DataFrame

print(df.loc[0])             # row by LABEL/index
print(df.iloc[0])            # row by POSITION (0-based)

print(df.loc[0, "name"])     # specific cell by label
print(df.iloc[0, 1])         # specific cell by position

print(df.loc[0:1])           # slicing rows by label (inclusive)
print(df.iloc[0:2])          # slicing rows by position (exclusive end)


# ============================================
# 12. FILTERING DATA (very frequently used)
# ============================================

print(df[df["age"] > 21])                       # rows where age > 21
print(df[(df["age"] > 21) & (df["score"] > 80)]) # multiple conditions (AND)
print(df[(df["age"] > 21) | (df["score"] > 80)]) # multiple conditions (OR)
print(df[df["name"].isin(["John", "Alex"])])     # membership check


# ============================================
# 13. ADDING / MODIFYING / DROPPING COLUMNS
# ============================================

df["passed"] = df["score"] >= 80        # add new column based on condition
print(df)

df["age_plus_one"] = df["age"] + 1       # add column from calculation
print(df)

df = df.drop("age_plus_one", axis=1)     # drop a column (axis=1 = column)
print(df)

df = df.rename(columns={"score": "test_score"})  # rename a column
print(df)


# ============================================
# 14. HANDLING MISSING DATA (extremely common in real datasets)
# ============================================

df_missing = pd.DataFrame({
    "name": ["John", "Mary", None],
    "age": [21, None, 23]
})

print(df_missing.isnull())           # True/False for each cell
print(df_missing.isnull().sum())     # count of missing values PER COLUMN

df_dropped = df_missing.dropna()             # drop rows with ANY missing value
print(df_dropped)

df_filled = df_missing.fillna("Unknown")     # fill missing values
print(df_filled)

df_filled_mean = df_missing["age"].fillna(df_missing["age"].mean())
print(df_filled_mean)


# ============================================
# 15. SORTING
# ============================================

print(df.sort_values("test_score"))                    # ascending (default)
print(df.sort_values("test_score", ascending=False))   # descending
print(df.sort_values(["age", "test_score"]))            # sort by multiple columns


# ============================================
# 16. GROUPING & AGGREGATING (a core skill - similar to SQL GROUP BY)
# ============================================

sales = pd.DataFrame({
    "region": ["East", "East", "West", "West", "North"],
    "product": ["A", "B", "A", "B", "A"],
    "amount": [100, 200, 150, 300, 120]
})

print(sales.groupby("region")["amount"].sum())      # total per region
print(sales.groupby("region")["amount"].mean())      # average per region
print(sales.groupby("region").agg({"amount": ["sum", "mean", "count"]}))

# Group by multiple columns
print(sales.groupby(["region", "product"])["amount"].sum())


# ============================================
# 17. APPLYING FUNCTIONS TO COLUMNS
# ============================================

df["test_score"] = df["test_score"].apply(lambda x: x + 5)   # apply to every value
print(df)

# apply() across a whole row (axis=1)
df["summary"] = df.apply(lambda row: f"{row['name']} scored {row['test_score']}", axis=1)
print(df)


# ============================================
# 18. MERGING / JOINING DATAFRAMES (like SQL JOINs)
# ============================================

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["John", "Mary", "Alex"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_id": [1, 2, 1],
    "amount": [250, 400, 150]
})

merged = pd.merge(customers, orders, on="customer_id", how="inner")   # like INNER JOIN
print(merged)

merged_left = pd.merge(customers, orders, on="customer_id", how="left")  # like LEFT JOIN
print(merged_left)

# concat - stacking dataframes together (like UNION)
more_customers = pd.DataFrame({"customer_id": [4], "name": ["Sara"]})
all_customers = pd.concat([customers, more_customers], ignore_index=True)
print(all_customers)


# ============================================
# 19. DATE/TIME HANDLING (relevant for time-series work)
# ============================================

dates_df = pd.DataFrame({
    "date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "cases": [10, 15, 12]
})

dates_df["date"] = pd.to_datetime(dates_df["date"])   # convert string -> datetime
print(dates_df.dtypes)

dates_df["month"] = dates_df["date"].dt.month
dates_df["weekday"] = dates_df["date"].dt.day_name()
print(dates_df)

# rolling average - very useful for time-series trend data
dates_df["rolling_avg"] = dates_df["cases"].rolling(window=2).mean()
print(dates_df)


# ============================================
# 20. VALUE COUNTS & UNIQUE VALUES
# ============================================

print(sales["region"].value_counts())    # count occurrences of each unique value
print(sales["region"].unique())          # array of unique values
print(sales["region"].nunique())         # number of unique values


# ============================================
# REFERENCE
# ============================================
# NUMPY
#   np.array()          -> create array
#   arr.shape/size/ndim  -> array properties
#   arr[start:end]        -> slicing
#   arr[arr > x]           -> boolean filtering
#   np.sum/mean/std/min/max(arr) -> aggregates
#   arr.reshape()          -> change shape
#
# PANDAS
#   pd.DataFrame(data)          -> create table
#   pd.read_csv() / to_csv()    -> read/write files
#   df.head()/tail()/info()/describe()  -> explore data
#   df.loc[] / df.iloc[]        -> select by label / position
#   df[condition]                -> filter rows
#   df.groupby(col)[col2].sum()  -> group & aggregate (like SQL GROUP BY)
#   pd.merge(df1, df2, on=col, how="inner"/"left") -> joins (like SQL JOIN)
#   df.isnull()/dropna()/fillna() -> handle missing data
#   df.sort_values(col)          -> sorting
#   df["col"].apply(fn)          -> apply function to a column
#   pd.to_datetime(df["col"])    -> convert to datetime