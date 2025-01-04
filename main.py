#sv_grenade_trajectory_prac_pipreview
from pymem import *

patch = b'\x0F\x85'
location = rb'\x0F\x84....\x8B\x05....\x48\x89\x9C\x24....\xBB' 
# 0F 84 ? ? ? ? 8B 05 ? ? ? ? 48 89 9C 24 ? ? ? ? BB

pm = Pymem('cs2.exe')
client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

address = pymem.pattern.pattern_scan_module(pm.process_handle, client, location)
if not address: raise Exception("Signature not found.")

print("[+] found signature @ %s" % hex(address))

pm.write_bytes(address, patch, len(patch))

print("[+] patched bytes")

"""
WARNING: Byte patching should be detected by VAC.
Don't use it on a good account.

This script swaps the grenade preview behavior,
displaying it when sv_grenade_trajectory_prac_pipreview is set to 0 instead of 1.
"""
