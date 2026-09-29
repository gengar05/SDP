#!/bin/bash

# Secure Network Check
# Purpose: Check basic network information on my Linux VM.
# Security: Only checks my own system, localhost and example.com.
# No external port scanning.

DOMAIN="example.com"
TEST_HOST="127.0.0.1"
TEST_PORT="8080"

LOG_DIR="$HOME/secure-network-check/evidence"
LOG_FILE="$LOG_DIR/network_check_$(date +%Y%m%d_%H%M%S).log"

PASSED=0
FAILED=0
log_status() {
    echo "[$1] $2"
    echo "$(date) [$1] $2" >> "$LOG_FILE"
}
environment_check() {
    log_status "INFO" "Checking network."

    hostname -I >> "$LOG_FILE"
    ip route | grep "default" >> "$LOG_FILE"

    log_status "OK" "Network checked."
    ((PASSED++))
}
dns_check() {
    if [ -z "$DOMAIN" ]; then
        log_status "FAIL" "Domain is empty."
        ((FAILED++))
    elif getent hosts "$DOMAIN" > /dev/null; then
        log_status "OK" "DNS works."
        ((PASSED++))
    else
        log_status "FAIL" "DNS does not work."
        ((FAILED++))
    fi
}
service_check() {
    if curl -s "http://$TEST_HOST:$TEST_PORT" > /dev/null; then
        log_status "OK" "Local service works."
        ((PASSED++))
    else
        log_status "FAIL" "Local service does not work."
        ((FAILED++))
    fi
}
port_check() {
    log_status "INFO" "Checking open ports."

    ss -tuln >> "$LOG_FILE"

    log_status "OK" "Port check completed."
    ((PASSED++))
}
cleanup() {
    if [ -n "$SERVER_PID" ]; then
        kill "$SERVER_PID" 2>/dev/null
        log_status "INFO" "Test server stopped."
    fi
}
start_server() {
    python3 -m http.server "$TEST_PORT" --bind "$TEST_HOST" > /dev/null 2>&1 &
    SERVER_PID=$!
    sleep 1
}
summary() {
    echo ""
    echo "Checks passed: $PASSED"
    echo "Checks failed: $FAILED"
    echo "Log file: $LOG_FILE"
}
tool_check() {
    TOOLS=("ip" "getent" "ss" "curl")

    for tool in "${TOOLS[@]}"; do
        log_status "INFO" "Checking $tool."
    done
}
mkdir -p "$LOG_DIR"

tool_check
environment_check
dns_check

start_server
service_check
port_check
cleanup

summary
if [ "$FAILED" -gt 0 ]; then
    exit 1
else
    exit 0
fi
