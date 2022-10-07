from prometheus_client import Gauge

from mccistats.constants import ADDRESSES

PLAYERS_ONLINE = Gauge(
  "mcci_players_online", "Number of players connected to the server"
)
PLAYERS_MAX = Gauge(
  "mcci_players_max",
  "Maximum number of players allowed on the server at one time",
)

LATENCY = Gauge(
  "mcci_latency_ms", "Latency in milliseconds to the proxy", ["proxy"]
)

AVAILABLE = Gauge("mcci_available", "Availability of the proxy", ["proxy"])
