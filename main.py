#sv_grenade_trajectory_prac_pipreview
from pymem import Pymem, process
from re import search

patch = b'\x0f\x85'
location = rb'\x0f\x84....\x8b\x05....\x48\x89\x74\x24.\xbe' 
# 0f 84 ? ? ? ? 8b 05 ? ? ? ? 48 89 74 24 ? be

pm = Pymem('cs2.exe')

client = process.module_from_name(pm.process_handle, 'client.dll')
clientBytes = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage) 

address = client.lpBaseOfDll + search(location, clientBytes).start()
pm.write_bytes(address, patch, len(patch))