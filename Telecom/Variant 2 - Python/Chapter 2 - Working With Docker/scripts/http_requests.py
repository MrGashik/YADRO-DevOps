#!/usr/bin/env python3

import requests
import logging

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

logging.basicConfig(
  level=logging.INFO,
  format=f'%(asctime)s - %(message)s'
)
logger = logging.getLogger(__name__)


def format_msg(level, message):
  if level == "INFO":
    msg = "{}[INFO] - {}".format(BLUE, message)
  elif level == "SUCCEEDED":
    msg = "{}[SUCCEEDED] - {}".format(GREEN, message)
  elif level == "ERROR":
    msg = "{}[ERROR] - {}".format(RED, message)
  elif level == "FAILED":
    msg = "{}[FAILED] - {}".format(RED, message)

  msg += f"{RESET}"

  return msg

def send_request(status_code):
  url = f"https://httpstat.us/{status_code}"

  try:
    response = requests.get(url, timeout=5)
    status = response.status_code

    if 100 <= status < 400:
      msg = format_msg("SUCCEEDED", f"Status Code: {status}, Response Body: {response.text.strip()}")
      logger.info(msg)
    else:
      msg = f"Status Code: {status}, Response Body: {response.text.strip()}"
      raise requests.exceptions.HTTPError(msg)
  except requests.exceptions.HTTPError as http_err:
    msg = format_msg("ERROR", f"{http_err}")
    logger.error(msg)
    raise
  except requests.exceptions.RequestException as req_err:
    msg = format_msg("ERROR", f"{req_err}")
    logger.error(msg)
    raise


if __name__ == "__main__":
  status_codes = [100, 200, 300, 400, 500]

  for status in status_codes:
    try:
      msg = format_msg("INFO", f"Sending Status Code: {status}")
      logger.info(msg)
      send_request(status)
    except Exception as e:
      msg = format_msg("FAILED", f"Status Code: {status}, Exeption: Request failed")
      logger.error(msg)
