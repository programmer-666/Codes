import krpc, time
conn = krpc.connect(name="Protocol-A")
vessel = conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1

vessel.control.activate_next_stage()

while True:
    print("%.1f %.1f %.1f" % vessel.position(vessel.orbit.body.reference_frame))