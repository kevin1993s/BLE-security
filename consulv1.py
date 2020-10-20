import asyncio
import platform
from bleak import BleakClient
from bleak import BleakScanner




async def run():
    devices = await BleakScanner.discover()
    #print ("Select the Device Number: \n")
    for d in devices:
      print(d)
loop = asyncio.get_event_loop()
loop.run_until_complete(run())


print ("Select the Device Number: \n")      
value = input()     
print (f"You Selected {value}")

mac_addr = value


async def print_services(mac_addr: str):
    device = await BleakScanner.find_device_by_address(mac_addr)
    async with BleakClient(device) as client:
        svcs = await client.get_services()
        print("Services:", svcs)
 


#loop = asyncio.get_event_loop()

loop.run_until_complete(print_services(mac_addr))

