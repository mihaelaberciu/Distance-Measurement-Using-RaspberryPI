import bluetooth

server_bluetooth=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_bluetooth.bind(("",port))
server_bluetooth.listen(1)
client_bluetooth,address = server_bluetooth.accept()
print("Conectat la ",address)
def bluetooth_afisare(dist):
    client_bluetooth.send("Obiect detectat la distanta de: "+ str(dist) + ' cm'+'\n\t\r' )