import krpc
conn = krpc.connect(name = 'Client1', address = '127.0.0.1', rpc_port = 50000, stream_port = 50001)
print(conn.krpc.get_status().version)
