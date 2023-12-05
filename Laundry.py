import random
class Laundry:
  def __init__(self, name, pickup, delivery):
    self.name = name
    self.schedule_pickup = pickup
    self.delivery_rate = delivery
    self.orders = dict()

  def getName(self):
    return self.name

  def show_schedule(self, type):
    if type == "pickup":
      return self.schedule_pickup
    
    elif type == "delivery":
      return self.delivery_rate
  
  def place_order(self, client_name):
    order_id = len(self.orders) + 1
    self.orders[str(order_id)] = {
      "order_id": order_id,
      "client_name": client_name, 
      "estimasi_pengiriman": random.choice(self.schedule_pickup),
    }

    return f"Berhasil memesan. Order ID : {order_id}\n{self.orders[str(order_id)]}"
  
  def get_orders(self, name):
    name_orders = [order for order_id, order in self.orders.items() if order["client_name"] == name]
    if not name_orders:
      return "Pelanggan tidak memiliki Order"
    return "\n".join(f"{order}" for order in name_orders)