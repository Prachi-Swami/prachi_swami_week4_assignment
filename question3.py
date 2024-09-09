
import logging


logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_process_file(file_path):
    try:
        # Attempt to open the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
          
            for line in lines:
                data = line.strip()
                
                number = int(data) 
                print(f"Processed number: {number}")
    
    except FileNotFoundError:
        error_message = f"File not found: {file_path}"
        print(error_message)
        logging.error(error_message)  # Log the FileNotFoundError
    
    except ValueError as e:
        error_message = f"ValueError encountered: {e}"
        print(error_message)
        logging.error(error_message)  # Log the ValueError

    except Exception as e:
        # Catch any other unforeseen errors
        error_message = f"An unexpected error occurred: {e}"
        print(error_message)
        logging.error(error_message) 

file_path = 'data.txt' 
read_and_process_file(file_path)
