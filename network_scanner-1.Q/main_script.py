# main_script.py
from network_scanning import scan_network
from ssh_connection import connect_to_multiple_ips

def main():
    # Ağ tarama
    network = "172.29.0.0/16"  # Hedef ağ
    ip_list = scan_network(network)
    
    # Bulunan IP adreslerini yazdır
    print("Discovered IP addresses:", ip_list)
    
    # SSH bağlantısı için kullanıcı bilgileri
    username = "your_username"  # Kullanıcı adınızı buraya girin
    password = "your_password"  # Parolanızı buraya girin
    
    # Her bir IP adresine bağlanmayı dene
    connect_to_multiple_ips(ip_list, username, password)

if __name__ == "__main__":
    main()
