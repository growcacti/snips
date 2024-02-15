def read_file_and_remove_duplicates(file_path):
    input_file_path = 'your_file.csv'
    custom_string = 'new'
    output_file = read_file_and_remove_duplicates(input_file_path, custom_string)


    with open(file_path, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]
    unique_lines = list(set(cleaned_lines))

    # Generating a unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{custom_string}_{timestamp}.csv"

    with open(output_filename, 'w') as file:
        for item in unique_lines:
            file.write(f"{item}\n")

        return output_filename

# Example usage
input_file_path = 'your_file.csv'
custom_string = ' '
output_file = read_file_and_remove_duplicates(input_file_path, custom_string)

print(f"Unique items written to {output_file}")

