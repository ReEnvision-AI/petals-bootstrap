import torch

# The reachability API is currently used only when connecting to the public swarm
REACHABILITY_API_URL = "https://sociallyshaped.net/health"

DTYPE_MAP = dict(bfloat16=torch.bfloat16, float16=torch.float16, float32=torch.float32, auto="auto")
