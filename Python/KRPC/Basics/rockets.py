import krpc

conn = krpc.connect()
vessel = conn.space_center.active_vessel # active current vessel

vessel.control.throttle = 1 # gas sett, 0-1
vessel.control.sas = True
vessel.control.activate_next_stage() # go next stage

f = True

while True:
    if vessel.flight().mean_altitude > 30000 and f:
        f = False
        vessel.control.throttle = 0
        vessel.control.activate_next_stage()
        vessel.control.sas = False
    if vessel.flight().mean_altitude >= 5000 and vessel.flight().mean_altitude <= 5100:
        vessel.control.yaw = 0.791 # right -> +, left -> -
    else:
        vessel.control.yaw = 0
    if vessel.flight().mean_altitude < 2000:
        vessel.control.yaw = 0
        vessel.control.roll = 0
        vessel.control.pitch = 0
        vessel.control.sas = True