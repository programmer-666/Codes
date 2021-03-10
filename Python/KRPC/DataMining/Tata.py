#   Mission TRUE DATA
#   Collecting various data during rocket's takeoff and flight

import krpc
import time
import os
import sqlite3
import datetime

sq3 = sqlite3.connect('tata_data.db')

flag = False
conn = krpc.connect(name = 'TATA_CLIENT', address = '127.0.0.1', rpc_port = 50000, stream_port = 50001)
ves = conn.space_center.active_vessel

while (True):
    COLLECTED_DATA = {
    'v_name':ves.name,
    #'v_type':ves.type,
    #'v_situation':ves.situation,
    'v_biome':ves.biome,
    #'v_comms':ves.comms,
    #'v_crew_capacity':ves.crew_capacity,
    #'v_crew_count':ves.crew_count,
    #'v_resources':ves.resources,
    'v_mass':ves.mass,
    'v_dry_mass':ves.dry_mass,
    'v_thrust':ves.thrust,
    'v_position_x':round(ves.position(ves.reference_frame)[0], 3),
    'v_position_y':round(ves.position(ves.reference_frame)[1], 3),
    'v_position_z':round(ves.position(ves.reference_frame)[2], 3),
    'v_velocity_x':round(ves.velocity(ves.reference_frame)[0], 3),
    'v_velocity_y':round(ves.velocity(ves.reference_frame)[1], 3),
    'v_velocity_z':round(ves.velocity(ves.reference_frame)[2], 3),
    'v_rotation_x':round(ves.rotation(ves.reference_frame)[0], 3),
    'v_rotation_y':round(ves.rotation(ves.reference_frame)[1], 3),
    'v_rotation_z':round(ves.rotation(ves.reference_frame)[2], 3),
    'v_direction_x':round(ves.direction(ves.reference_frame)[0], 3),
    'v_direction_y':round(ves.direction(ves.reference_frame)[1], 3),
    'v_direction_z':round(ves.direction(ves.reference_frame)[2], 3),
    'v_f_velocity_x':round(ves.flight().velocity[0], 3),
    'v_f_velocity_y':round(ves.flight().velocity[0], 3),
    'v_f_velocity_z':round(ves.flight().velocity[0], 3),
    'v_f_speed':round(ves.flight().speed, 3),
    #'v_f_horizontal_speed':ves.flight().horizontal_speed,
    #'v_f_vertical_speed':ves.flight().vertical_speed,
    'v_f_center_of_mass_x':ves.flight().center_of_mass[0],
    'v_f_center_of_mass_y':ves.flight().center_of_mass[1],
    'v_f_center_of_mass_z':ves.flight().center_of_mass[2],
    'v_f_pitch':round(ves.flight().pitch, 3),
    'v_f_heading':round(ves.flight().heading, 3),
    'v_f_roll':ves.flight().roll,
    #'v_c_source':ves.control.source,
    'v_r_names':ves.resources.names,
    'v_r_amount':[ves.resources.amount(ves.resources.names[i]) for i in range(len(ves.resources.names))],
    's_alt':round(ves.flight().surface_altitude, 3), 
    'sea_alt':round(ves.flight().mean_altitude, 3),
    'time_real':datetime.datetime.strftime(datetime.datetime.now(), '%X')}

    """with open('tester_Data.csv', 'a') as file:
        file.write(str(COLLECTED_DATA.items()))
	file.write('\n')"""

    cursor = sq3.cursor()
    cursor.execute("INSERT INTO TESTER VALUES ('"+COLLECTED_DATA.get("v_name")+"','"+COLLECTED_DATA.get("v_biome")+"',"+str(COLLECTED_DATA.get("v_mass"))+","+str(COLLECTED_DATA.get("v_dry_mass"))+","+str(COLLECTED_DATA.get("v_thrust"))+","+str(COLLECTED_DATA.get("v_position_x"))+","+str(COLLECTED_DATA.get("v_position_y"))+","+str(COLLECTED_DATA.get("v_position_z"))+","+str(COLLECTED_DATA.get("v_velocity_x"))+","+str(COLLECTED_DATA.get("v_velocity_y"))+","+str(COLLECTED_DATA.get("v_velocity_z"))+","+str(COLLECTED_DATA.get("v_rotation_x"))+","+str(COLLECTED_DATA.get("v_rotation_y"))+","+str(COLLECTED_DATA.get("v_rotation_z"))+","+str(COLLECTED_DATA.get("v_direction_x"))+","+str(COLLECTED_DATA.get("v_direction_y"))+","+str(COLLECTED_DATA.get("v_direction_z"))+","+str(COLLECTED_DATA.get("v_f_velocity_x"))+","+str(COLLECTED_DATA.get("v_f_velocity_y"))+","+str(COLLECTED_DATA.get("v_f_velocity_z"))+","+str(COLLECTED_DATA.get("v_f_speed"))+","+str(COLLECTED_DATA.get("v_f_center_of_mass_x"))+","+str(COLLECTED_DATA.get("v_f_center_of_mass_y"))+","+str(COLLECTED_DATA.get("v_f_center_of_mass_z"))+","+str(COLLECTED_DATA.get("v_f_pitch"))+","+str(COLLECTED_DATA.get("v_f_heading"))+","+str(COLLECTED_DATA.get("v_f_roll"))+",'"+str(COLLECTED_DATA.get("v_r_names"))+"','"+str(COLLECTED_DATA.get("v_r_amount"))+"',"+str(COLLECTED_DATA.get("s_alt"))+","+str(COLLECTED_DATA.get("sea_alt"))+",'"+str(COLLECTED_DATA.get("time_real"))+"')")
    sq3.commit()
    sq3.close()

    break