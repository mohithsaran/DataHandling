import json


def read_interview_file(file_path):
    try:
        with open(file_path, 'r') as file:
            interview_data = json.load(file)
        return interview_data
    except Exception as e:
        print(f"Error reading JSON file {file_path}: {e}")
        return None


def save_filtered_questions(filtered_questions, output_file):
    data = {
        'filtered_questions': filtered_questions}
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Filtered questions saved to {output_file}")
    except Exception as e:
        print(f"Error saving filtered questions to {output_file}: {e}")


file_path = 'interview_data.json'
interview_data = read_interview_file(file_path)
if interview_data:
    print(interview_data)
filtered_questions = [
    {'question': 'What is Python?', 'difficulty_level': 'Beginner', 'tags': ['Python', 'Programming']},
    {'question': 'What is SQL?', 'difficulty_level': 'Intermediate', 'tags': ['SQL', 'Database']}
]
output_file = 'filtered_questions.json'
save_filtered_questions(filtered_questions, output_file)
