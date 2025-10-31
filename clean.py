import csv

def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        previous_row = None
        for row in reader:
            if len(row) == 5:
                if previous_row:
                    row.insert(0, previous_row[0])
            writer.writerow(row)
            previous_row = row

input_file = 'olympic_medal_table.csv'
output_file = 'olympic_medal_table_cleaned.csv'
process_csv(input_file, output_file)

