from dataclasses import dataclass
from mcstatus import JavaServer
from typing import Dict


@dataclass
class ProxyStatus:
  players_online: int
  players_max: int
  latency_ms: int


@dataclass
class ServerStatus:
  players_online: int
  players_max: int
  latencies: Dict[str, int]


def proxy_status(addr: str) -> ProxyStatus:
  try:
    server = JavaServer.lookup(addr)
    status = server.status()
    return ProxyStatus(
      players_online=status.players.online,
      players_max=status.players.max,
      latency_ms=round(status.latency),
    )
  except:
    import traceback

    traceback.print_exc()

    return ProxyStatus(players_online=0, players_max=0, latency_ms=-1)
