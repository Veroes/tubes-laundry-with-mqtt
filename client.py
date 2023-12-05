import xmlrpc.client

def mainMenu():
  print("======================================")
  print("      Jasa Laundry        ")
  print("1. Laundry Bojong")
  print("2. Laundry Soang")
  print("3. Tampilkan Laundry Paling Cepat")
  print("0. Quit")

  option = int(input("Pilih opsi: "))

  return option

def mainMenuLaundry(laundry_service):
  option = -1

  while option != 0:
    print("======================================")
    print(f"   Jasa {laundry_service.getName()}    ")
    print("1. Tampilkan Schedule Pickup")
    print("2. Pesan Laundry")
    print("3. Tampilakan Pesanan yang dibuat")
    print("0. Balik ke Main Menu")

    option = int(input("Pilih opsi: "))

    match option:
      case 1:
        print(f"Berikut Jadwal Pickup {laundry_service.getName()} ")
        print(laundry_service.show_schedule("pickup"))

      case 2:
        nama = str(input("Masukkan Nama Anda: "))
        print(laundry_service.place_order(nama))
        print("Berhasil Memesan")
        
      case 3:
        nama = str(input("Masukkan Nama Anda: "))
        print(laundry_service.get_orders(nama))

      case 0:
        print("\n\n")
        break

def main():
  BOJONG_PROXY = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
  SOANG_PROXY = xmlrpc.client.ServerProxy("http://localhost:8001/RPC2")

  option = mainMenu()

  while option != 0:
    match option:
      case 1:
        mainMenuLaundry(BOJONG_PROXY)

      case 2:
        mainMenuLaundry(SOANG_PROXY)

      case 3:
        bojong_delivery = BOJONG_PROXY.show_schedule("delivery")
        print(f"Waktu Pengantaran Laundry Bojong: {bojong_delivery} jam")
        soang_delivery = SOANG_PROXY.show_schedule("delivery")
        print(f"Waktu Pengantaran Laundry Soang: {soang_delivery} jam")
        print("\n\n")

      case 0:
        break

    option = mainMenu()

if __name__ == "__main__":
  main()