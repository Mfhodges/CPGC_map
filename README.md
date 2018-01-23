# CPGC_map :earth_americas:
An interactive map of previous CPGC funded internships

currently hosted here: http://ds-web.haverford.edu/cpgc/map.html#

---
## CSV to JSON Converter

The file `converter.py` has code to convert a csv file to a json file that the .js can read to make the map. It is assumed that this csv file is downloaded from the google sheet that contains all CPGC locations.

The script can be run from the command line as follows:
```
$ python convert.py -i <path_to_inputfile> -o <path_to_outputfile>
```

The code for this script was largely taken from [here](http://www.idiotinside.com/2015/09/18/csv-json-pretty-print-python/) and was modified to accommodate the geojson structure.

##### GeoJSON Structure
Since this map is generated with [Mapbox](https://www.mapbox.com/mapbox-gl-js/api) (similar to this [example](https://www.mapbox.com/mapbox-gl-js/example/filter-features-within-map-view/)) it requires that the data be stored as a GeoJSON. **GeoJSON** is a format for encoding a variety of geographic data structures.
Consider the following example:

| name | Latitude | Longitude |
|------|----------|-----------|
|Dinagat Islands| 125.6| 10.1 |

Would become the following GeoJSON *Feature* object.
```
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```
###### <right> ([source](http://geojson.org/)) </right>
Moreover, the scripts in this repo assume every location will have the geometry type of *Point*.

Since the map relies on a GeoJSON structure, there are two main assumptions of the csv that is being read by the py file - there exists two columns "Latitude" and "Longitude". **Without these features in the csv the script will throw an error.**
Additionally there are features that are used in the .js function such as "Organization_Information_Website" that should remain the same in the csv for the js code to be able to function. It is recommended that one review the js before making changes to the csv field names to thoroughly check this dependency.

##### Connecting to the Javascript
Ultimately the .js file is what is reading the GeoJSON to populate the map.

Therefore the GeoJSON file should be saved as a consistent file name ( currently data.json ) because it is loaded in the .js file with the line: `var mydata = JSON.parse(data);` ( note the omission of the '.json')


NOTE: it should be clarified if the following is needed in the html header before the js.

`<script type="text/javascript" src="data.json"></script>`


## Updating the map with google sheets
[google sheet api](https://developers.google.com/sheets/api/guides/concepts)

TBA

The next steps in this project will be to remove the step of downloading the google sheet as an csv and then running `convert.py` and add to the script so that utilize the google sheet api to pull the csv from the web.


## Contributors :tada:
[Maddy Hodges](https://github.com/Mfhodges)
