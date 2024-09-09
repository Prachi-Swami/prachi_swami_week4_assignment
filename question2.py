# Create a script that processes a CSV file containing student grades and calculates the average grade for each student.
import csv

def calculate_average_grades(input_csv, output_csv):
    try:
        with open(input_csv, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row (Name, Math, English, Science)

            # Prepare a list to hold student averages
            student_averages = []

            # Process each student
            for row in csv_reader:
                name = row[0]  # Student's name
                grades = list(map(float, row[1:]))  # Convert grades to floats
                average_grade = sum(grades) / len(grades)  # Calculate the average
                student_averages.append([name, average_grade])

        # Write the results to a new CSV file
        with open(output_csv, 'w', newline='') as result_file:
            csv_writer = csv.writer(result_file)
            csv_writer.writerow(['Name', 'Average Grade']) 

          
            for student in student_averages:
                csv_writer.writerow(student)

        print(f"Average grades written to {output_csv}")

    except FileNotFoundError:
        print(f"Error: {input_csv} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
input_csv = 'F:\xenosis\Assignment_4\grades.csv' 
output_csv = 'F:\xenosis\Assignment_4\student_averages.csv'  
calculate_average_grades(input_csv, output_csv)
