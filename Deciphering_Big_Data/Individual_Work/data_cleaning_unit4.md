# Data Cleaning Task - Unit 4

## Task Description

This is a task focused on cleaning and processing a [Unicef dataset](./data/unit-4/mn.csv) with 9,008 rows and 159 columns. The aim of this task was to apply a variety of data cleaning techniques to prepare the dataset for further analysis and store the cleaned data in a SQLite database. The key steps included header replacement, handling column mismatches, removing duplicates, dealing with missing values, normalising numeric data, and ensuring the dataset was formatted for SQLite compatibility.

## Learning Objectives

- Gain an understanding and perform the basics and factors of data cleaning.
- Evaluate the critical outcomes for the data design and automation.
- Compile and document Python scripts.
- Compile data sets and convert data into different formats.

## Detailed Objectives

- **Load the dataset** and ensure it is correctly read into memory.
- **Replace headers** from a provided header file, resolving any mismatches between data columns and header rows.
- **Handle column mismatches** by aligning the number of headers with the dataset.
- **Remove duplicate records** to maintain data consistency.
- **Handle missing values** by filling numeric columns with their respective mean values.
- **Normalise numeric columns** for consistent scaling.
- **Sanitise column names** for compatibility with SQLite by removing spaces, special characters, and ensuring column name uniqueness.
- **Save the cleaned dataset** into a SQLite database for future querying and analysis.

## Steps Completed

### 1. **Data Loading**
   - The dataset was successfully loaded with 9,008 rows and 159 columns.
   - A separate header file containing 210 headers was provided, which resulted in a mismatch with the dataset. The headers were truncated to match the 159 columns in the dataset.

### 2. **Replacing Headers**
   - The headers were replaced successfully after truncating them to align with the number of columns in the dataset.

### 3. **Handling Column Mismatches**
   - A mismatch between the number of headers and data columns was handled by truncating the header file to ensure alignment.
   - No missing headers were identified that would impact the data analysis.

### 4. **Removing Duplicates**
   - Duplicates were removed from the dataset, retaining a total of 9,008 unique records.

### 5. **Handling Missing Values**
   - Numeric columns with missing values were filled using the mean of each respective column.

### 6. **Normalising Numeric Data**
   - The numeric columns were normalised, ensuring consistent scaling across the dataset for future analysis.

### 7. **Sanitising Column Names for SQLite**
   - The column names were sanitised by removing special characters and ensuring each column name is unique, making the dataset compatible with SQLite.

### 8. **Saving to SQLite**
   - The cleaned dataset was saved to an SQLite database (`cleaned_data.db`) in the table `cleaned_data`. The data is now accessible for querying and analysis using SQL commands.

## Results

- The final cleaned dataset contains 9,008 rows and 159 columns.
- The data has been cleaned, normalised, and stored in an [SQLite database (`cleaned_data.db`)](./data/unit-4/cleaned_data.db), where it can be easily accessed and queried.

## Instructions for Running the [Code](./scripts/unit-4/data-cleaning.py)

### Prerequisites

- Ensure Python 3.x is installed along with the required libraries:
  ```bash
  pip install pandas numpy sqlite3
