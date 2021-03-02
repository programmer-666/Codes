import krpc
from os import system
from time import sleep
FL1 = False
FL2 = False
ALT = 6000

conn = krpc.connect(name="FRC-C")
ves = conn.space_center.active_vessel

print("[CONTROL] OPERATION STARTED")
sleep(1.34)
ves.control.throttle = 0.5
ves.control.sas = True
if ves.control.sas:
    print("[CONTROL] SAS ACTIVATED")
sleep(0.5)
ves.control.activate_next_stage()

while ves.flight().mean_altitude < ALT:
    FL1 = True
    print("[CONTROL] ALTITUDE {:.2f}".format(ves.flight().mean_altitude))
    if ves.flight().mean_altitude > ALT and FL1:
        print("[CONTROL] FL1 TRUE")        
        break
while ves.flight().mean_altitude > ALT and not FL2:
    print("[CONTROL] ALTITUDE ({:.2f}) GTH {} FL1 TRUE".format(ves.flight().mean_altitude, ALT))
    while ves.flight().mean_altitude < ALT and FL1:
        ves.control.activate_next_stage()
        FL2 = True
        print(f"[CONTROL] ALTITUDE LTH {ALT} FL1 TRUE FL2 TRUE")        
        break
while ves.flight().surface_altitude > 0:
    print("[CONTROL] ALTITUDE {:.2f}".format(ves.flight().surface_altitude))
    if ves.flight().surface_altitude <= 2:
        print("[CONTROL] OPERATION FINISHED")
        break