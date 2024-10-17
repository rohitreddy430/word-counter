import os

def file_count(file_path):
    words = 0
    print("Current working directory:", os.getcwd())  # Debugging line
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words += len(line.split())
        return words
    except FileNotFoundError:
        print(f"The file path '{file_path}' does not exist.")
        return 0

file_name = input("Enter the file name: ")
word_count = file_count(file_name)

print("Number of words:", word_count)