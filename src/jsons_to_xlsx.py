import os
import json
import sys
import openpyxl

# Usage: python jsons_to_xlsx.py Question output.xlsx

def main():
    if len(sys.argv) != 3:
        print("Usage: python jsons_to_xlsx.py <questions_folder> <output_xlsx>")
        sys.exit(1)

    questions_folder = sys.argv[1]
    output_xlsx = sys.argv[2]

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

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Question', 'Correct', 'A', 'B', 'C', 'D'])
    for q in all_questions:
        ws.append([
            q.get('Question', ''),
            q.get('Correct Answer', ''),
            q.get('Answer A', ''),
            q.get('Answer B', ''),
            q.get('Answer C', ''),
            q.get('Answer D', '')
        ])
    wb.save(output_xlsx)
    print(f"Wrote {len(all_questions)} questions to {output_xlsx}")

if __name__ == '__main__':
    main()
