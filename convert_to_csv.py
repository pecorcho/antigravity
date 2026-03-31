import json
import csv

# Path to the input file
input_path = r'C:\Users\usuario\.gemini\antigravity\brain\e752173f-c1f6-4c88-a856-2a21c288f8e6\.system_generated\steps\56\output.txt'
# Path to the output CSV
output_path = r'C:\Users\usuario\.gemini\antigravity\scratch\cuadernos_notebooklm.csv'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

notebooks = data.get('notebooks', [])

with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['Title', 'Ownership', 'Source Count', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for nb in notebooks:
        writer.writerow({
            'Title': nb.get('title'),
            'Ownership': nb.get('ownership'),
            'Source Count': nb.get('source_count'),
            'URL': nb.get('url')
        })

print(f"Successfully created CSV at {output_path}")
