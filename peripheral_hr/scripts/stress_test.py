#!python 

import asyncio
import logging
from bleak import BleakClient
from time import time

HR_ADDRESS="CC:63:74:B3:0A:3D"

async def main():
  print(f"Creating client for device address {HR_ADDRESS}", flush=True)
  client =  BleakClient(HR_ADDRESS)
  print(f"Client: {client}", flush=True)
  print("Trying to connect...", flush=True)
  await client.connect(timeout=20)
  print(f"Is connected: {client.is_connected}")
  for service in client.services:
    print(f"  Service: {service}", flush=True)
  service = client.services.get_service("180d")
  print(f"Service: {service}", flush=True)
  for chrc in service.characteristics:
    print(f"  Characterstic: {chrc}", flush=True)
  chrc = service.get_characteristic("2a38")
  print(f"Charateristic: {chrc}", flush=True)
  n = 50
  print(f"Priming ({n} reads)...", flush=True)
  for i in range(0, n):
    value = await client.read_gatt_char(chrc)
  n = 10
  print(f"Measuring {n} reads...", flush=True)
  millis_before = int(time() * 1000)
  for i in range(0, n):
    value = await client.read_gatt_char(chrc)
    #print(f"* {i:03d} Value: {value}", flush=True)
  millis_after = int(time() * 1000)
  print(f"Performed {n} reads in {millis_after - millis_before} ms", flush=True)
  await client.disconnect()

#logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
asyncio.run(main())





