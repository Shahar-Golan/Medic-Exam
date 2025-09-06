import json
import csv
import sys

# Usage: python json_to_csv.py input.json output.csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python json_to_csv.py input.json output.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # CSV columns: Question, Correct, A, B, C, D
    fieldnames = [
        'Question', 'Correct Answer', 'Answer A', 'Answer B', 'Answer C', 'Answer D'
    ]

    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header (matching the HTML table, but without Category)
        writer.writerow(['Question', 'Correct', 'A', 'B', 'C', 'D'])
        for q in data:
            writer.writerow([
                q.get('Question', ''),
                q.get('Correct Answer', ''),
                q.get('Answer A', ''),
                q.get('Answer B', ''),
                q.get('Answer C', ''),
                q.get('Answer D', '')
            ])

if __name__ == '__main__':
    main()
