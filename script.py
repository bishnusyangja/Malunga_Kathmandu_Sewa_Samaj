import csv

ward_list = (
		'# Malunga Bhedabari - 1', 
		'# Malunga Basindanda - 2',
		'# Malunga Kota/KhadaGaira -3',

		)


def main():
	outfile = 'malunga_contacts.md'
	md_file = open(outfile, 'w')
	for ward in range(1, 10):
		if ward == 4:
			ward = 45
		if ward == 5:
			continue

		filename = 'ward_{}.csv'.format(ward)
		csvfile = open(filename, 'r', newline='')

		md_file.write('{}\n\n'.format(ward_list[ward-1], ))
		md_file.write('| SN | Person Name | Contact Num	| Kathmandu Place | Occupation | Members | \n')
		md_file.write('|----| ----- | -----| ----|-----|-----| \n')
		
		csv_reader = csv.reader(csvfile)
		list_items = list(csv_reader)
		list_items.pop(0)
		sorted_rows = sorted(list_items, key=lambda x: x[0])

		for i, row in enumerate(sorted_rows):
			if i == 0:
				continue

			row_content = ' | '.join(row)
			md_file.write('| {} | {} | \n'.format(i, row_content))

		csvfile.close()
	md_file.close()


if __name__ == '__main__':
	main()