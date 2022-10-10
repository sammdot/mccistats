from prometheus_client import Gauge

from tubnetstats.constants import ADDRESSES

PLAYERS_ONLINE = Gauge(
  "tubnet_players_online", "Number of players connected to the server"
)
PLAYERS_MAX = Gauge(
  "tubnet_players_max",
  "Maximum number of players allowed on the server at one time",
)

LATENCY = Gauge(
  "tubnet_latency_ms", "Latency in milliseconds to the proxy", ["proxy"]
)

AVAILABLE = Gauge("tubnet_available", "Availability of the proxy", ["proxy"])
