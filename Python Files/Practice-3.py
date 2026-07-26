"""
==============================================
Python File Operations - Notes + Runnable Code
==============================================
"""

# ============================================
# 1. OPENING A FILE
# ============================================

# Basic way (not preferred - must close manually)
# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Problem: if an error happens before file.close(), the file stays open.

# Preferred way - using "with" (auto-closes the file, even on error)
with open("sample.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
# file created here first so the read examples below actually work

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed after this block


# ============================================
# 2. FILE MODES SUMMARY (as comments)
# ============================================
# "r"   -> Read only. File must exist, errors if not found.
# "w"   -> Write. Creates file if missing. OVERWRITES existing content.
# "a"   -> Append. Creates file if missing. Adds to END, keeps existing content.
# "r+"  -> Read + Write. File must exist. Doesn't auto-erase.
# "w+"  -> Write + Read. Creates file. ERASES existing content first.
# "a+"  -> Append + Read. Creates file if missing.
# "x"   -> Exclusive create. Errors if file already exists.
# Add "b" to any mode (e.g. "rb", "wb") for binary files (images, PDFs).


# ============================================
# 3. READING FILES
# ============================================

# Read entire file as one string
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Read one line at a time
with open("sample.txt", "r") as file:
    line = file.readline()
    print(line)

# Read all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)   # ['Line 1\n', 'Line 2\n', 'Line 3\n']

# Loop through file line by line (memory-efficient - preferred for large files)
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())   # .strip() removes trailing \n

# Why loop line-by-line for large files?
# .read() loads the ENTIRE file into memory at once.
# Looping reads only one line at a time - similar in spirit to generators.


# ============================================
# 4. WRITING FILES
# ============================================

# "w" mode - creates new file OR overwrites existing content completely
with open("output.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is line 2\n")
# Running this block again will WIPE and rewrite the file from scratch

# Writing multiple lines at once
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("output.txt", "w") as file:
    file.writelines(lines_to_write)

# GOTCHA: write() does NOT add a newline automatically
with open("no_newline_demo.txt", "w") as file:
    file.write("Hello")
    file.write("World")
# Result in file: "HelloWorld" - no space or newline between them

with open("no_newline_demo.txt", "r") as file:
    print(file.read())


# ============================================
# 5. APPENDING FILES
# ============================================

# "a" mode - adds to the END of the file, keeps existing content
with open("output.txt", "a") as file:
    file.write("This line gets appended\n")

# Run this block multiple times -> each run ADDS a line, nothing erased
with open("output.txt", "r") as file:
    print(file.read())

# Difference recap:
# "w" run twice  -> second run ERASES the first
# "a" run twice  -> BOTH writes are kept


# ============================================
# 6. "r+" MODE (Read + Write)
# ============================================

with open("sample.txt", "r+") as file:
    existing_content = file.read()        # read first - moves cursor to END
    print(existing_content)
    file.write("New line added via r+\n")  # writes at CURRENT cursor position
    # since .read() moved cursor to end, this effectively appends

with open("sample.txt", "r") as file:
    print(file.read())

# To overwrite from the BEGINNING using r+, move the cursor manually:
with open("sample.txt", "r+") as file:
    file.seek(0)                                  # move cursor to very start
    file.write("Overwritten first line!!!\n")      # overwrites from position 0

with open("sample.txt", "r") as file:
    print(file.read())


# ============================================
# 7. seek() AND tell() - CURSOR CONTROL
# ============================================

with open("sample.txt", "r") as file:
    print(file.tell())         # 0 -> cursor starts at position 0

    partial = file.read(5)      # read only first 5 characters
    print(partial)
    print(file.tell())         # 5 -> cursor moved forward by 5

    file.seek(0)                # move cursor back to the start
    print(file.read(5))         # re-reads the same first 5 characters


# ============================================
# 8. CHECKING FILE EXISTENCE & HANDLING ERRORS
# ============================================

import os

if os.path.exists("sample.txt"):
    with open("sample.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist")

# Safer error handling with try-except
try:
    with open("missing_file_demo.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")


# ============================================
# 9. WORKING WITH CSV FILES
# ============================================

import csv

# Writing a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Region", "Cases", "Date"])              # header row
    writer.writerow(["Massachusetts", 120, "2026-07-20"])
    writer.writerow(["California", 300, "2026-07-20"])

# Reading a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# NOTE: newline="" when writing CSVs on Windows prevents extra
# blank lines from appearing between rows.


# ============================================
# QUICK REFERENCE (as comments)
# ============================================
# "r"   -> just reading
# "w"   -> want a FRESH file every time (overwrites)
# "a"   -> want to keep ADDING without erasing (e.g. logs)
# "r+"  -> read + write together, cursor-position dependent
# "w+"  -> write + read, erases first
