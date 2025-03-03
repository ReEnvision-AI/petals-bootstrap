from urllib.error import HTTPError, URLError
import torch
from urllib.request import urlopen
import json

# URL to fetch the initial peers from
INITIAL_PEERS_URL = "https://sociallyshaped.net/initial-peers"

PUBLIC_INITIAL_PEERS_BACKUP = [
    '/ip4/50.106.9.34/tcp/8788/p2p/QmXQMr1yy6sJ81QM6Rxxz3Zpnxw5rUVgZabxPHaVvH7gRG'
]

try:
  with urlopen(INITIAL_PEERS_URL, timeout=5) as response:
    data = json.loads(response.read().decode())
    if isinstance(data, list) and data and all(isinstance(item, str) for item in data):
      PUBLIC_INITIAL_PEERS = data
    else:
      print("Invalid or empty data from initial peers API")
      PUBLIC_INITIAL_PEERS = PUBLIC_INITIAL_PEERS_BACKUP
except (HTTPError, URLError, json.JSONDecodeError) as e:
  print(f"Failed to fetch initial peers: {e}")
  PUBLIC_INITIAL_PEERS = PUBLIC_INITIAL_PEERS_BACKUP

# The reachability API is currently used only when connecting to the public swarm
REACHABILITY_API_URL = "https://sociallyshaped.net/health"

DTYPE_MAP = dict(bfloat16=torch.bfloat16, float16=torch.float16, float32=torch.float32, auto="auto")
