# ssh_connection.py
import paramiko
from concurrent.futures import ThreadPoolExecutor

def connect_ssh(ip, username, password):
    try:
        print(f"Connecting to {ip}...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)
        print(f"Successfully connected to {ip}!")
        client.close()
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")

def connect_to_multiple_ips(ip_list, username, password):
    with ThreadPoolExecutor(max_workers=5) as executor:  # Aynı anda 5 bağlantı açar
        for ip in ip_list:
            executor.submit(connect_ssh, ip, username, password)
