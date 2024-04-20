import csv

ward_list = ('# Malunga Bhedabari - 1', )

def write_ward_headings(file, ward):
	file.write('{}\n\n'.format(ward_list[ward-1], ))

	return file


def main():
	outfile = 'malunga_contacts.md'
	md_file = open(outfile, 'w')
	for ward in range(1, 10):
		filename = 'ward_{}.csv'.format(ward)
		csvfile = open(filename, 'r', newline='')
		md_file = write_ward_headings(md_file, ward)
		csv_reader = csv.reader(csvfile)
		md_file.write('| SN | Person Name | Contact Num	| Kathmandu Place | Occupation | Members | \n')
		md_file.write('|----| ----- | -----| ----|-----|-----| \n')
		for i, row in enumerate(csv_reader):
			if i == 0:
				continue
			# todo sort by alphabetical order
			row_content = ' | '.join(row)
			md_file.write('| {} | {} | \n'.format(i+1, row_content))
		csvfile.close()
	md_file.close()




# Opening the CSV file in read mode
# with open(file_path, 'r', newline='') as csvfile:
#     # Creating a CSV reader object
#     csv_reader = csv.reader(csvfile)
    
#     # Looping through each row in the CSV file
#     for row in csv_reader:
#         # 'row' is a list containing each field in the row
#         # You can access individual fields by index, e.g., row[0], row[1], etc.
#         print(row)


if __name__ == '__main__':
	main()