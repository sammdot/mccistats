from tubnetstats.constants import ADDRESSES
from tubnetstats.ping import proxy_status, ServerStatus
from tubnetstats.metrics import AVAILABLE, LATENCY, PLAYERS_MAX, PLAYERS_ONLINE


def server_status():
  try:
    statuses = [proxy_status(ADDRESSES[0])]

    overall = ServerStatus(
      players_online=max(map(lambda p: p.players_online, statuses)),
      players_max=max(map(lambda p: p.players_max, statuses)),
      latencies={addr: p.latency_ms for addr, p in zip(ADDRESSES, statuses)},
    )

    PLAYERS_ONLINE.set(overall.players_online)
    PLAYERS_MAX.set(overall.players_max)

    for addr, latency in overall.latencies.items():
      if latency > 0:
        LATENCY.labels(proxy=addr).set(latency)
        AVAILABLE.labels(proxy=addr).set(1)
      else:
        LATENCY.labels(proxy=addr).set(0)
        AVAILABLE.labels(proxy=addr).set(0)
  except Exception as e:
    import traceback

    traceback.print_exc()
