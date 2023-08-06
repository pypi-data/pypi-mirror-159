import os

import transistordatabase as tdb


#tdb.print_tdb()
tdb.update_from_fileexchange()
t1 = tdb.load('CREE_C3M0060065J')


dpt_save_dict = {
    'path': '/home/nikolasf/Downloads/C3M0060065J 400V/*.csv',
    'dataset_type': 'graph_i_e',
    'comment': '',
    'load_inductance': 750e-6,
    'commutation_inductance': 15.63e-9,
    'commutation_device': 'IDH06G65C6',
    'measurement_date': None,
    'measurement_testbench': 'LEA-UPB Testbench',
    'v_g': 15,
    'v_g_off': -4,
    'energies': 'both',
    'r_g': 2.55,
    'r_g_off': 2.55,
    'integration_interval': 'IEC 60747-9',
    'mode': 'analyze'}




dict = tdb.dpt_save_data(dpt_save_dict)
t1.add_dpt_measurement(dict)


#t1.export_json()

## rename folder data
# os.chdir('/home/nikolasf/Downloads/C3M0060065J 400V/')
# filenames_list = os.listdir()
#
#
# new_filenames_list = []
#
# for filename in filenames_list:
#     filename = filename.replace('Eon','ON')
#     filename = filename.replace('Eoff','OFF')
#
#     new_filenames_list.append(filename)
#
# print(f"{filenames_list = }")
# print(f"{new_filenames_list = }")
#
# for count, value in enumerate(filenames_list):
#     os.replace(filenames_list[count], new_filenames_list[count])

#tdb.print_tdb()

# print(t1.switch.e_on_meas)
# t1.compare_measurement_datasheet()


a = 5

if
