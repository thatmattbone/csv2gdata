Overview
========

csv2gdata is a set of tools for converting CSVs into Google charts.

Essentially it is a very thin wrapper around the wonderful `csvkit
<http://csvkit.rtfd.org/>`_ and `Google's python wrapper for
generating visualizations
<http://code.google.com/p/google-visualization-python/>`_.

The first tool, ``csv2gdatatable``, takes CSVs and converts them into
the `JSON format expected
<http://code.google.com/apis/chart/interactive/docs/reference.html#dataparam>`_ by a
``google.visualization.DataTable`` class.  For example, the simple
CSV::

 name, age
 bob, 42

Becomes::

  {"rows": [{"c": [{"v": "bob"}, 
                   {"v": 42}]}], 
    "cols": [{"type": "string", 
              "id": "name", 
              "label": "name"}, 
             {"type": "number", 
              "id": "age", 
              "label": "age"}]}

One important restriction on the CSV is that a header row is required
to generate the names and labels in this JSON format.

The second tool, ``gdatawrap`` takes this JSON format as input and wraps
it in very simple HTML templates to create the different kinds of
charts.  Currently there are templates for line charts, scatter
charts, pie charts, and motion charts.

Keep in mind that not all CSVs will work with all charts.
Fundamentally csv2data is simply converting a CSV (a tabular format)
into a `google.visualization.DataTable
<http://code.google.com/apis/chart/interactive/docs/reference.html#DataTable>`_
(another tabular format).  So, since a ``DataTable`` instance would
need to have timestamps in the first column in order to use it to
render a motion chart, so too would a CSV need timestamps in the first
column to render a motion chart with csv2gdata.




Installation
============

If you want to use csv2gdata::

  pip install http://google-visualization-python.googlecode.com/files/gviz_api_py-1.8.0.tar.gz#egg=gviz_api.py
  pip install git+git://github.com/thatmattbone/csv2gdata.git#egg=csv2gdata

(I can't figure out how to get pip to look at my ``dependency_links``
directive in ``setup.py``. If you find what I've done wrong, you get a
pony (not really)).

If you want to hack on csv2gdata::

  git clone git://github.com/thatmattbone/csv2gdata.git
  cd csv2gdata
  pip install -r requirements.txt
  #submit pull request :)



Some Examples
=============

Let's start by looking at a simple CSV about the `Chicago Transit
Authority's Ridership numbers by year <http://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv>`_.  
Here's a sample of what it
looks like::

  year,bus,paratransit,rail,total
  1988,430089500,435400,174436000,604960900
  1989,420572700,924800,168658800,590156300
  ...


Now, to download, pipe the data through gdata converter, wrap it in
some line chart code and serve up the results locally, we simply::

  curl http://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv | csv2gdatatable | gdatawrap line_chart --serve

To see the chart, navigate to `localhost:8000 <http://localhost:8000>`_. Likewise, we can serve up a scatter plot:

  curl http://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv | csv2gdatatable | gdatawrap scatter_chart --serve

Notice that these charts use the first column as the x-axis and all
subsequent columns are series along the y-axis.  Because csv2gdata
relies on csvkit, we can use ``csvcut`` to eliminate some columns.  Let's
just look at the bus and rail columns::

  curl http://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv | csvcut -c year,bus,rail | csv2gdatatable | gdatawrap scatter_chart --serve

Motion and pie chart examples coming soon...

Include the data table coming soon, too. This will optionally include the javascript g-charts table at the bottom.

Why Would I Use This?
=====================

Maybe you don't want to.  If you're trying to load a CSV into google
charts from some web service that is frequently updated, for example,
then you most certainly want to use the `CSV Data Sources Protocol
<http://code.google.com/apis/chart/interactive/docs/dev/implementing_data_source.html#csvdatatable>`_. But,
if you're trying to take a quick peek at some data you have sitting
around and maybe even share it with your friend over HTTP, this might
be of use.  Or, if you just forget how to bootstrap google charts or
generate the `data table JSON
<http://code.google.com/apis/chart/interactive/docs/reference.html#dataparam>`_,
you can take the generated data or HTML and hack away.



