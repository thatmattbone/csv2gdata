import datetime

from csvkit.table import Table
import gviz_api


def type_to_type_string(some_type):
    """Convert a python type to the string form expected by the gviz_api."""
    if type(1) == some_type:
        return "number"
    elif type(1.0) == some_type:
        return "number"
    elif type(u"hi") == some_type:
        return "string"
    elif type("hi") == some_type:
        return "string"
    elif type(datetime.date.today()) == some_type:
        return "date"
    elif type(datetime.date.now()) == some_type:
        return "date"


def table_to_gdata(table):
    """Convert the columns from the csvkit Table into the dictionary format expected by the gviz_api. 

    For example with the headers ["number", "letter"]::
      [[1, 2, 3], ["a", "b", "c"]]

    Becomes::
      [{"number": 1, "letter": "a"},
       {"number": 2, "letter": "b"},
       {"number": 3, "letter": "c"},]
    """
    column_names = [column.name for column in table]
    gdata = []
    for row in table.to_rows():
        gdata.append(dict(zip(column_names, row)))
    return gdata


def table_to_gdata_description(table): 
    """Convert the column names and types from the csvkit Table into the dictionary format expected by the gviz_api.

    For example, a table with two columns name (a string) and age (an integer) becomes::
      {"name": ("string", "name"),
        "age": ("integer", "age")}
    """
    return dict([(column.name, (type_to_type_string(column.type), column.name)) for column in table])


def gdata_to_json(table):
    """Convert a csvkit Table to a json string expected by the google.visualization.DataTable API.

    See: http://code.google.com/apis/chart/interactive/docs/reference.html#DataTable
    """
    gdata_description = table_to_gdata_description(table)
    gdata = table_to_gdata(table)

    data_table = gviz_api.DataTable(gdata_description)
    data_table.LoadData(gdata)

    json = data_table.ToJSon(columns_order=[column.name for column in table],
                                        order_by=table[0].name)
    return json


def motion_chart(json):
    return """<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load('visualization', '1', {'packages':['motionchart']});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable(""" + json + """, 0.6);
        var chart = new google.visualization.MotionChart(document.getElementById('chart_div'));
        chart.draw(data, {width: 600, height:300});
      }
    </script>
  </head>

  <body>
    <div id="chart_div" style="width: 600px; height: 300px;"></div>
  </body>
</html>"""


def serve_content(content):
    from wsgiref.util import setup_testing_defaults
    from wsgiref.simple_server import make_server

    
    def simple_app(environ, start_response):
        setup_testing_defaults(environ)

        status = '200 OK'
        headers = [('Content-type', 'text/html')]

        start_response(status, headers)

        return content

    httpd = make_server('', 8000, simple_app)
    print "Serving on port 8000..."
    httpd.serve_forever()

    
