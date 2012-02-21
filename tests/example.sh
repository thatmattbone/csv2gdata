#!/bin/bash
curl http://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD | csv2gdatatable | gdatawrap line_chart --serve