# CPGC_map
An interactive map of previous CPGC funded internships

currently hosted here: http://ds-web.haverford.edu/cpgc/map.html#

---
## CSV to JSON Converter

The file `converter.py` has code to convert a csv file to a json file that the .js can read to make the map. 

The script can be run from the command line as follows:

... `$ python convert.py -i <path to inputfile> -o <path to outputfile>`

The code for this script was largely taken from [here](http://www.idiotinside.com/2015/09/18/csv-json-pretty-print-python/) and was modified to accomadate the geojson structure. 

There are two main assumptions of the csv that is being read - there exists two columns "Latitude" and "Longitude". Without these features the script will throw an error. 

The file should be saved as data.json because it is loaded in the  
js file with the line: `var mydata = JSON.parse(data);`

There are features that are used in the .js function such as "Organization_Information_Website" that should remain the same in the csv for the js code to be able to function.  


