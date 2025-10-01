# RustDesk Online Status Checker

A simple HTTP service to check if a RustDesk client is online.

Special thanks to <https://github.com/Draganis/RustDeskOnlinestat>

## Usage

Send a GET request to `/online/{remote_id}` to check if a RustDesk client is online:

```bash
curl https://rustdesk.home/online/235341605
```

Response:
```json
{
  "source_id": "123456789",
  "target_id": "235341605",
  "server_ip": "hbbs",
  "is_online": true
}
```

## Environment Variables

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `SERVER_IP`: RustDesk server IP/hostname (default: hbbs)

## Docker Deployment

```bash
docker compose up -d
```

The service will be available at `https://rustdesk.home/online/{remote_id}` via Traefik.
