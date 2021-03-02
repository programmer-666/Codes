import krpc
conn = krpc.connect(
    address='192.168.1.7',
    rpc_port=50000, stream_port=50001)
ves = conn.space_center.active_vessel
ves.control.activate_next_stage()