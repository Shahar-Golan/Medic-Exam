import os
import json
import csv
import sys

# Usage: python jsons_to_csv.py Question output.csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python jsons_to_csv.py <questions_folder> <output_csv>")
        sys.exit(1)

    questions_folder = sys.argv[1]
    output_csv = sys.argv[2]

    all_questions = []
    for filename in os.listdir(questions_folder):
        if filename.endswith('.json'):
            path = os.path.join(questions_folder, filename)
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_questions.extend(data)
                    elif isinstance(data, dict):
                        all_questions.append(data)
                except Exception as e:
                    print(f"Warning: Could not parse {filename}: {e}")

    with open(output_csv, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Correct', 'A', 'B', 'C', 'D'])
        for q in all_questions:
            writer.writerow([
                q.get('Question', ''),
                q.get('Correct Answer', ''),
                q.get('Answer A', ''),
                q.get('Answer B', ''),
                q.get('Answer C', ''),
                q.get('Answer D', '')
            ])
    print(f"Wrote {len(all_questions)} questions to {output_csv}")

if __name__ == '__main__':
    main()
