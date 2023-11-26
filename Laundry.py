class Laundry:
  def __init__(self, name, pickup, delivery):
    self.name = name
    self.schedule_pickup = pickup
    self.schedule_delivery = delivery
    self.clients = dict()
    self.orders = dict()

  def accept_client(self, client_name):
    if client_name not in self.clients:
      self.clients[client_name] = True
      return f"{client_name} berhasil mengikuti laundry {self.name}"
    else:
      return f"Anda sudah mengikuti laundry {self.name}"
  
  def show_schedule(self, client_name, type):
    if client_name not in self.clients:
      return f"Anda belum meng-follow laundry {self.name}"
    else:
      if type == "pickup":
        return self.schedule_pickup
      elif type == "delivery":
        return self.schedule_delivery
  
  def place_order(self, client_name, pickup_time):
    if client_name not in self.clients:
      return f"Anda belum meng-follow laundry {self.name}"
    else:
      order_id = len(self.orders) + 1
      self.orders[order_id] = {
        "client_name": client_name, 
        "pickup_time": pickup_time,
      }
      return f"Berhasil memesan. Order ID : {order_id}"
  
  def get_orders(self, client_name):
    if client_name not in self.clients:
      return f"Anda belum meng-follow laundry {self.name}"
    else:
      return {k: v for k, v in self.orders.items() if v["client_name"] == client_name}