import os

def count_file_content(input_file, output_file):
    # Initialize counters
    line_count = 0
    word_count = 0
    char_count = 0

    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            # Loop through each line in the file
            for line in file:
                line_count += 1  # Increment line count
                words = line.split()  # Split the line into words
                word_count += len(words)  # Increment word count
                char_count += len(line)  # Increment character count (includes spaces and newline)

        # Write results to output file
        with open(output_file, 'w') as result_file:
            result_file.write(f"Lines: {line_count}\n")
            result_file.write(f"Words: {word_count}\n")
            result_file.write(f"Characters: {char_count}\n")

        print(f"Results written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")



base_folder = 'F:\xenosis\Assignment_4' 
sub_folder = 'Files'
input_file = os.path.join(base_folder, sub_folder, 'input.txt')
output_file = os.path.join(base_folder, 'output.txt')

count_file_content(input_file, output_file)
