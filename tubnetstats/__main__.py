from tubnetstats import server_status
from multiprocessing import Pool
from prometheus_client import start_http_server
from schedule import every, run_pending
from time import sleep

PROMETHEUS_PORT = 3688


def main():
  start_http_server(PROMETHEUS_PORT)

  server_status()
  every(10).seconds.do(server_status)

  while True:
    run_pending()
    sleep(1)


if __name__ == "__main__":
  main()
