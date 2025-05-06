#!/bin/bash

RED="\033[31m"
GREEN="\033[32m"
BLUE="\033[34m"
RESET="\033[0m"

logger() {
  local timestamp
  timestamp=$(date '+%Y-%m-%d %H:%M:%S')

  if [[ $1 = "INFO" ]]; then
    echo -e "${timestamp} - ${BLUE}[INFO] - ${2}${RESET}"
  elif [[ $1 = "SUCCEEDED" ]]; then
    echo -e "${timestamp} - ${GREEN}[SUCCEEDED] - ${2}${RESET}"
  elif [[ $1 = "ERROR" ]]; then
    echo -e "${timestamp} - ${RED}[ERROR] - ${2}${RESET}" >&2
  elif [[ $1 = "FAILED" ]]; then
    echo -e "${timestamp} - ${RED}[FAILED] - ${2}${RESET}" >&2
  fi
}

send_request() {
  local status_code=$1
  local url="https://httpstat.us/$status_code"

  local response
  response=$(curl -s -w "%{http_code}" "$url" -o /tmp/response_body 2>/dev/null --connect-timeout 3 --max-time 5)
  local curl_status=$?

  if [ $curl_status -ne 0 ]; then
      logger "ERROR" "Failed to reach $url: curl error"
      return 1
  fi

  local status=$response
  local body
  body=$(cat /tmp/response_body)

  if [[ $status =~ ^[123][0-9][0-9]$ ]]; then
      logger "SUCCEEDED" "Status Code: $status, Response Body: $body"
  else
      logger "ERROR" "Status Code: $status, Response Body: $body"
      return 1
  fi

  return 0
}

status_codes=(100 200 300 400 500)

for status in "${status_codes[@]}"; do
    logger "INFO" "Sending Status Code: $status"
    if ! send_request "$status"; then
        logger "FAILED" "Status Code: $status, Exception: Request failed"
    fi
done

