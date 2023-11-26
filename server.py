from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import Laundry

class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ("/RPC2",)

# pickup dan delivery Laundry Bojong
pickup_bojong = {}
delivery_bojong = {}

# pickup dan delivery Laundry Soang
pickup_soang = {}
delivery_soang = {}

# Server Laundry Bojong
laundry_bojong = Laundry("Laundry Bojong", pickup_bojong, delivery_bojong)
server_bojong = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server_bojong.register_instance(laundry_bojong)

# Server Laundry Soang
laundry_soang = Laundry("Laundry soang", pickup_soang, delivery_soang)
server_soang = SimpleXMLRPCServer(("localhost", 8001), requestHandler=RequestHandler)
server_soang.register_instance(laundry_soang)

print("Laundry Bojong server listening on port 8000...")
print("Laundry Soang server listening on port 8001...")

thread_bojong = threading.Thread(target=server_bojong.serve_forever)
thread_soang = threading.Thread(target=server_soang.serve_forever)

thread_bojong.start()
thread_soang.start()