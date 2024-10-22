import pandas as pd
import numpy as np
import sqlite3

# Fix column names for SQLite (removing spaces, special characters, and duplicates)
def sanitize_column_names(df):
    df.columns = df.columns.str.replace('[^0-9a-zA-Z_]+', '_', regex=True)
    df.columns = df.columns.str.strip('_').str.lstrip('0123456789')
    
    seen_columns = {}
    for i, col in enumerate(df.columns):
        if col in seen_columns:
            seen_columns[col] += 1
            df.columns.values[i] = f"{col}_{seen_columns[col]}"
        else:
            seen_columns[col] = 0

    return df

# Handle missing values by filling numeric columns with the mean
def handle_missing_values(df):
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].apply(lambda col: col.fillna(col.mean()), axis=0)
    return df

# Normalize numeric columns
def normalize_data(df):
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].apply(lambda col: (col - col.min()) / (col.max() - col.min()), axis=0)
    return df

# Save cleaned data to SQLite database
def save_to_sqlite(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Data saved to {db_name} in the table {table_name}.")
    except Exception as e:
        print(f"Error saving data to SQLite: {e}")
    finally:
        conn.close()

def main():
    # Step 1: Load the dataset
    df_raw = pd.read_csv('/Users/reecelance/Desktop/mn.csv')

    # Step 2: Load and replace headers
    headers = pd.read_csv('/Users/reecelance/Desktop/mn_headers.csv', header=None)
    
    if headers.shape[0] != df_raw.shape[1]:
        headers = headers.iloc[:df_raw.shape[1]]  # Truncate headers if needed
    
    df_raw.columns = headers.iloc[:, 0].values  # Replace headers

    # Step 3: Handle column mismatch (if any) and check missing headers
    missing_headers = [header for header in headers.iloc[:, 0].values if header not in df_raw.columns]
    
    # Step 4: Remove duplicates
    df_cleaned = df_raw.drop_duplicates()

    # Step 5: Handle missing values
    df_cleaned = handle_missing_values(df_cleaned)

    # Step 6: Normalize numeric data
    df_cleaned = normalize_data(df_cleaned)

    # Step 7: Fix column names for SQLite
    df_cleaned = sanitize_column_names(df_cleaned)

    # Step 8: Save cleaned data to SQLite database
    save_to_sqlite(df_cleaned, '/Users/reecelance/Desktop/cleaned_data.db', 'cleaned_data')

if __name__ == "__main__":
    main()
