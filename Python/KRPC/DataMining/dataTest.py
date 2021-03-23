import krpc
import pandas as pd
import numpy as np
import csv
import datetime

conn = krpc.connect(name = 'DataMiner', address = '127.0.0.1', rpc_port = 50000, stream_port = 50001)
vessel = conn.space_center.active_vessel
# connections
header = ['datetime', 'throttle', 'mass', 'altitude', 'sea_level_altitude']
COLLECTED_DATA = []
# csv defines
while True:
    COLLECTED_DATA.append((datetime.datetime.strftime(datetime.datetime.now(), '%X'),round(vessel.control.throttle,2),round(vessel.mass,2),round(vessel.flight().surface_altitude,2),round(vessel.flight().mean_altitude,2)))
    if vessel.flight().surface_altitude < 2:
        break
# data gathering

with open('dataTest.csv', 'wt', newline='') as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(header)
    writer.writerows(COLLECTED_DATA)