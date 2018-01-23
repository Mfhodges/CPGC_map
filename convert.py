#!/usr/bin/python


import sys, getopt
import csv
import json
import spreadsheet




#Get Command Line Arguments
def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print 'convert.py -i <path to inputfile or '+ '\'sheet\''+'> -o <path to outputfile> -f <dump/pretty> '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'convert.py -i <path to inputfile or '+ '\'sheet\''+'> -o <path to outputfile> -f <dump/pretty>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg

    if input_file == 'sheet':
        read_sheet(output_file, format)
    else:
        read_csv(input_file, output_file, format)


"""
var places = {
"type": "FeatureCollection",
"features": [
{
"type": "Feature",
"geometry": {
  "type": "Point",
  "coordinates":  [ -75.171022,39.944101 ]
  },
"properties": {
    ...
    ...
}
...
... ]
}
"""


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames # should remove lat and long from this because they have no use as properties
    #    title.remove("Latitude")
    #    title.remove("Longitude")
        for row in reader:
            #print row
            lat = row["Latitude"]
            lon = row["Longitude"]
            csv_rows.extend([{"type": "Feature", "geometry": { "type": "Point", "coordinates": [ lon,lat ] },"properties":{title[i]:row[title[i]] for i in range(len(title))}}])
#        print csv_rows[0]
        write_json(csv_rows, json_file, format)

#Read CSV File
def read_sheet(json_file, format):
    #Get spreadsheet!
    input_data = spreadsheet.pullsheet()
    #print(input_data) # this variable is stored properly
    sheet_rows = []

    fieldnames = input_data[0].keys() # should remove lat and long from this because they have no use as properties
#    print("fieldnames= ", fieldnames)  # this variable is stored properly
    for row in input_data:
        #print row
        lat = row["Latitude"]
        lon = row["Longitude"]
        sheet_rows.extend([{"type": "Feature", "geometry": { "type": "Point", "coordinates": [ lon,lat ] },"properties":{fieldnames[i]:row[fieldnames[i]] for i in range(len(fieldnames))}}])
#    print "first Feature obj",sheet_rows[0]
#    print json.dumps(sheet_rows)
#    write_json(sheet_rows, json_file, format)
   # print("got here")

    with open(json_file, "w") as f:
        f.write("data ='[{\"type\": \"FeatureCollection\",\"features\":")
        f.write(json.dumps(sheet_rows))
        f.write("}]';")



#Convert data into json and write it
def write_json(data, json_file, format):
#    print "in write_json"
#    print data
    with open(json_file, "w") as f:
        f.write("data ='[{\"type\": \"FeatureCollection\",\"features\":")
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
           # f.write(data)
            f.write(json.dumps(data))
        f.write("}]';")

if __name__ == "__main__":
   main(sys.argv[1:])
