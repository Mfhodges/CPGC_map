#!/usr/bin/python

import sys, getopt
import csv
import json

#Get Command Line Arguments
def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print 'convert.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'convert.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
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
... ]}
"""


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames # should remove lat and long from this
    #    title.remove("Latitude")
    #    title.remove("Longitude")
        for row in reader:
            #print row
            lat = row["Latitude"]
            lon = row["Longitude"]
            csv_rows.extend([{"type": "Feature", "geometry": { "type": "Point", "coordinates": [ lon,lat ] },"properties":{title[i]:row[title[i]] for i in range(len(title))}}])
#        print csv_rows[0]
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    #print data
    with open(json_file, "w") as f:
        f.write("data ='[{\"type\": \"FeatureCollection\",\"features\":")
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))
        f.write("}]';")

if __name__ == "__main__":
   main(sys.argv[1:])
