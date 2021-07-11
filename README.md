# energy-meter
Energy Meter is services that get energy meter.

## Setup Dependencies
* Install Python v3.9
* Install PostgreSQL, this is because we use django that use postgre as default.
* Install required library with
  
  `pip3 install -r meter_usage_web/requirements/local.txt`

## Proto file
The `.proto` file is in `proto/` directory. We can compile to python with the command:

`protoc -I=proto/ --python_out=proto/ proto/meter.proto`

Copy the result files: `meter_pb2_grpc.py` and `meter_pb2.py` to where we want to use the proto.

## Data Preparation
CSV file for measurement is saved in `grpc/` directory. We can run migration using command:

`python3 migrate.py`

The command will put the data in csv to sqlite database for easy retrieval.

## Run gRPC Server
gRPC Server we use is on the grpc directory. To run it, go to grpc directory use the command:

`python3 server.py`

## Run web server
The web server is in `meter_usage_web/` directory. It build using django cookie cutter so it have a lot of unused files.
To run the webserver we can use either docker or command line. But the docker is currently not maintained because time constraint.

To run webserver go to `meter_usage_web/` and run:
`python3 manage.py runserver --settings=config.settings.local`

Webserver if succesfully run will be on the address:
`http://localhost:8000`

## Using the meter
You will see the title `Measurement Meter Chart` and it will accept to input: start date and end date in field `START` and `END`. Because the data is only from 2019-01-01 to 2019-01-31, the wweb is defaulted to that date.
Click `Plot Chart` to generate chart for measurement for that time range.

## How it works
The grpc server is providing the time series data and accept data for range start to end. Currently no pagination provided because time constraint and the next step can be using streaming to send data.

The webserver receive the time series data and send it to client.

Client call it using AJAX and use the time series data to plot the chart.

The key files for the webserver code is in `energy-meter/meter_usage_web/meter_usage_web/api` and `energy-meter/meter_usage_web/meter_usage_web/web` folders

For the html and javascript is in: `energy-meter/meter_usage_web/meter_usage_web/templates/pages/home.html`


## Decision Log
* I use Unary gRPC because it is the simplest grpc method. Plan to use other method like streaming but don't have enough time.
* I use django cookie cutter from here: `https://github.com/pydanny/cookiecutter-django` to speed up development for the webserver. It has a lot of unused file, because it is designed for production ready services with all bell and whistles. But most of it not used now due to time constraint.
* I use jquery for the webpage because I know jquery and it is simple enough to do what I need.
* I use chart.js to better present the time series data, because I have some time to not just print the json result. The problem I encounter is updating the chart is complicated, I choose to remove the html node and recreate it with new chart.
* It is better to use the compiled proto as shared library but to make it work need some times, I choose to copy it to wherever it is needed.
* I pick timestamp not date for saving the time series data so it should compatible with different timezones. But this still not properly implemented, because I still use local timezone. Because I use local timezone, data migration is needed because so it will be run in your timezone. This is one of the part that need to be fixed next.
