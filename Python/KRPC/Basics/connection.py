import krpc
conn = krpc.connect(name="Protocol-A")
ves = conn.space_center.active_vessel
ves.control.activate_next_stage()