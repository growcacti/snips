import datetime
from tkinter.filedialog import askopenfilename
def get_filepath():
    filepath = askopenfilename(filetypes=[("Comma Separted Values", "*.csv"), ("All Files", "*.*"),])
    if not filepath:
        return 
    return filepath
def read_file_and_remove_duplicates():
    custom_string = ''
    
    filepath = get_filepath()
    with open(filepath, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]
    unique_lines = list(set(cleaned_lines))

    # Generating a unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{custom_string}_{timestamp}.csv"

    # Create a list with formatted items
    formatted_items = [f"{custom_string}_{timestamp}_{item}" for item in unique_lines]

    with open(output_filename, 'w') as file:
        for item in formatted_items:
            file.write(f"{item}\n")
            
    print(formatted_items)
    return formatted_items


read_file_and_remove_duplicates()
