from mccistats import server_status
from multiprocessing import Pool
from prometheus_client import start_http_server
from schedule import every, run_pending
from time import sleep

PROMETHEUS_PORT = 3622


def main():
  start_http_server(PROMETHEUS_PORT)

  pool = Pool(processes=3)
  server_status(pool)
  every(10).seconds.do(server_status, pool)

  while True:
    run_pending()
    sleep(1)


if __name__ == "__main__":
  main()
