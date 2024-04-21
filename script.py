import csv

ward_list = (
		'# Malunga Bhedabari - 1', 
		'# Malunga Basindanda - 2',
		'# Malunga Kota/KhadaGaira -3',
		'# Malunga Bajadi/Gau - 4/5',
		'# Malunga Jaukharak - 6',
		'# Malunga Gaira/Chaur - 7',
		'# Malunga Tunibot/Phata - 8',
		'# Malunga Dhangling - 9',
		)

def filter_unique_lists(list_of_lists):
    seen = {}
    result = []
    for inner_list in list_of_lists:
        first_element = inner_list[0]
        if first_element not in seen:
            seen[first_element] = True
            result.append(inner_list)
    return result


def main():
	outfile = 'malunga_contacts.md'
	md_file = open(outfile, 'w')
	for ward in range(1, 10):
		file_appender = '4_5' if ward == 4 else ward
		if ward == 5:
			continue

		filename = 'ward_{}.csv'.format(file_appender)
		csvfile = open(filename, 'r', newline='')

		header_index = ward - 1 if ward < 5 else ward - 2

		md_file.write('{}\n\n'.format(ward_list[header_index], ))
		md_file.write('| SN | Person Name | Contact Num	| Kathmandu Place | Occupation | Members | \n')
		md_file.write('|----| ----- | -----| ----|-----|-----| \n')
		
		csv_reader = csv.reader(csvfile)
		list_items = list(csv_reader)
		list_items.pop(0)
		
		unique_item_list = filter_unique_lists(list_items)
		sorted_rows = sorted(unique_item_list, key=lambda x: x[0])

		for i, row in enumerate(sorted_rows):
			row = ['-' if item == '' else item for item in row]
			row_content = ' | '.join(row)
			md_file.write('| {} | {} | \n'.format(i+1, row_content))

		csvfile.close()
		print("{} loaded successfully .... ".format(filename))
		md_file.write("\n\n")
	md_file.close()


if __name__ == '__main__':
	main()