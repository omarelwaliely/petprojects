import csv
import datetime

def new_table(inputfile, outputfile, *columns):
    with open(inputfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        written_rows = set()
        for row in reader:
            output_row = []
            for col in columns:
                cell_value = row[col-1].strip()
                output_row.append(cell_value)
            if tuple(output_row) not in written_rows:
                writer.writerow(output_row)
                written_rows.add(tuple(output_row))
            
def multi_value_table(inputfile, outputfile, key_cols, semicolon_col):
    with open(inputfile, 'r') as infile, open(outputfile, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        headers = [header[i-1] for i in key_cols]
        headers.append(header[semicolon_col-1])
        writer.writerow(headers)
        written_rows = set()
        for row in reader:
            if row[semicolon_col-1] != '':
                key_values = [row[i-1].strip() for i in key_cols]
                semicolon_values = row[semicolon_col-1].split(';')
                for value in semicolon_values:
                    value = value.strip()
                    new_row = key_values + [value]
                    if tuple(new_row) not in written_rows:
                        writer.writerow(new_row)
                        written_rows.add(tuple(new_row))

def remove_extra(inputfile, outputfile):
    with open(inputfile, newline='') as infile:
        csv_reader = csv.reader(infile)
        with open(outputfile, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            for row in csv_reader:
                cleanrow= [cell.replace('\n', '').replace(',','') for cell in row]
                csv_writer.writerow(cleanrow)




new_table('olx.csv', 'sellero.csv', 2, 4,5,26) #seller
new_table('olx.csv','car.csv', 10,11,16) #car
new_table('olx.csv','adold.csv',6,7,8,9,13,15,24,12,17,18,19,20,21,22,23) #ad
multi_value_table('olx.csv','features.csv',(10,11,16,),25) #features
multi_value_table('olx.csv','phonenumbers.csv',(6,),3) #phone numbers
remove_extra('adold.csv','ad.csv')
with open('sellero.csv', 'r') as infile, open('seller.csv', 'w', newline='') as outfile: #converting to format that sql can read
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    for row in reader:
        date_str = row[2]
        date = datetime.datetime.strptime(date_str, '%b %Y')
        mysql_date_str = date.strftime('%Y-%m-%d')
        row[2] = mysql_date_str
        writer.writerow(row)
new_table('olx.csv','sellercar.csv', 10,11,16,2,26) #sellercar
new_table('olx.csv','carlisting.csv', 10,11,16,6) #carlisting