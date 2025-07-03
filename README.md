# ST7735-Screen-Distance-Pi
Distance sensor display using HC-SR04 ultrasonic sensor on TFT ST7735 screen with raspberry Pi 3B+
Work to be done for porting to ESP-32 and arduino

## Screen
- GND = Pin 6 (Ground)
- VCC = Pin 1 (3v3 Power)
- SCL = Pin 23 (GPIO 11)
- SDA = Pin 19 (GPIO 10)
- RST = Pin 18 (GPIO 24)
- DC = Pin 22 (GPIO 25)
- CS = Pin 24 (GPIO 8)

## Distance sensor
- GND = Pin 9 (Ground)
- ECHO = 1k Resistor ->Splits-> Pin 13 (GPIO 27) & 2 Resistor -> Attached to same length as GND
- TRIG = Pin 11 (GPIO 17)
- VCC = Pin 4 (5V Power)

## Sites
- Pinout: https://pinout.xyz/
- Setup: https://learn.adafruit.com/1-8-tft-display/python-wiring-and-setup
- Usage: https://learn.adafruit.com/1-8-tft-display/python-usage
- Library to display images: https://pillow.readthedocs.io/en/stable/handbook/overview.html
- Distance sensor: https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
- GPIO Docs: https://gpiozero.readthedocs.io/en/latest/recipes.html
