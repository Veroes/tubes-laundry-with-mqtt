import random
import sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
from Laundry import Laundry

class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ("/RPC2",)

# pickup dan delivery Laundry Bojong
pickup_bojong = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
delivery_bojong = random.randint(1, 6)

# pickup dan delivery Laundry Soang
pickup_soang = ["Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
delivery_soang = random.randint(1, 6)

# Server Laundry Bojong
laundry_bojong = Laundry("Laundry Bojong", pickup_bojong, delivery_bojong)
server_bojong = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server_bojong.register_instance(laundry_bojong)

# Server Laundry Soang
laundry_soang = Laundry("Laundry Soang", pickup_soang, delivery_soang)
server_soang = SimpleXMLRPCServer(("localhost", 8001), requestHandler=RequestHandler)
server_soang.register_instance(laundry_soang)

print("Laundry Bojong server listening on port 8000...")
print("Laundry Soang server listening on port 8001...")

# Mulai threads pada server
thread_bojong = threading.Thread(target=server_bojong.serve_forever, daemon=True)
thread_soang = threading.Thread(target=server_soang.serve_forever, daemon=True)

thread_bojong.start()
thread_soang.start()

server_bojong.serve_forever()
server_soang.serve_forever()
try:
  while True:
    pass  # Keep the main thread 
except KeyboardInterrupt:
  print("\nKeyboard interrupt received, shutting down servers.")
  server_bojong.shutdown()
  server_soang.shutdown()

# Tunggu untuk threads selesai
thread_bojong.join()
thread_soang.join()

print("Closing Server....")
sys.exit(0)