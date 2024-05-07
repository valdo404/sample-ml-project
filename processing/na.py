def display_non_missing_data(column):
    non_missing_data = df[column].dropna()
    if not non_missing_data.empty:
        display(HTML(f'<h4>{column}:</h4>'))
        display(non_missing_data)