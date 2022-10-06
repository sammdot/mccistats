from prometheus_client import Gauge

from mccistats.constants import ADDRESSES

PLAYERS_ONLINE = Gauge(
  "players_online", "Number of players connected to the server"
)
PLAYERS_MAX = Gauge(
  "players_max", "Maximum number of players allowed on the server at one time"
)

LATENCY = Gauge("latency_ms", "Latency in milliseconds to the proxy", ["proxy"])

AVAILABLE = Gauge("available", "Availability of the proxy", ["proxy"])
