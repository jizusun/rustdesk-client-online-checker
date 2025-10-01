import socket

def check_rustdesk_online(source_id: str, target_id: str, server_ip: str, server_port: int = 21115) -> bool | None:
    # Build payload
    payload = b"\x68\xba\x01\x17\x0a\x0a" + source_id.encode() + b"\x12\x09" + target_id.encode()
    payload = build_rustdesk_payload(source_id,target_id)
    try:
        # Opening TCP-Connection to RustDesk-Relay-Server
        with socket.create_connection((server_ip, server_port), timeout=5) as s:
            s.sendall(payload)
            response = s.recv(7)
    except socket.error as e:
        print(f"Connection error: {e}")
        return None

    # Check answer
    if response == b"\x18\xc2\x01\x03\x0a\x01\x80":
        return True
    elif response == b"\x18\xc2\x01\x03\x0a\x01\x00":
        return False
    else:
        print("Unknown answer:", response.hex())
        return None
def build_rustdesk_payload(source_id: str, target_id: str) -> bytes:
    header = b'\x68\xba\x01\x17'
    source_id_bytes = source_id.zfill(10).encode()
    target_id_bytes = target_id.encode()
    return (
        header +
        bytes([0x0a, len(source_id_bytes)]) + source_id_bytes +
        bytes([0x12, len(target_id_bytes)]) + target_id_bytes
    )

