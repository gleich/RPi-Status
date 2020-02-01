# RPi-Status

Show the status of your RPi's CPU using the Pimoroni Blinkt.

# Color Values

Updates all the lights to the corresponding colors as shown below every 5 seconds

![CPU<33 Percent = Green](https://badgen.net/badge/CPU%3C33%20Percent/%20%20%20%20%20%20%20%20%20%20%20%20%20/green)

![CPU<66 Percent = Yellow](https://badgen.net/badge/CPU%3C66%20Percent/%20%20%20%20%20%20%20%20%20%20%20%20%20/yellow)

![CPU<=100 Percent = Red](https://badgen.net/badge/CPU%3C=100%20Percent/%20%20%20%20%20%20%20%20%20%20%20%20%20/red)

## Setup

You can either run this program using python or in a docker container with docker-compose

### Python

1. Clone the repo
2. Run `pip3 install -r requirements.txt` in the repo
3. Run `python3 rpiStatus/main.py` in the repo

### Docker

1. Clone the repo
2. Run `docker-compose up -d` in the repo
