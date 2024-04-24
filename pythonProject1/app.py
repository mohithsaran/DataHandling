import json

def read_interview_file(file_path):
    try:
        with open(file_path, 'r') as file:
            interview_data = json.load(file)
        return interview_data
    except Exception as e:
        print(f"Error reading JSON file {file_path}: {e}")
        return None


file_path = 'interview_data.json'
interview_data = read_interview_file(file_path)
if interview_data:
    print(interview_data)
