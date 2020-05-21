from gpiozero import LED, Button
import signal
import time

class Device:

    def __init__(self, led_bcm=17, button_bcm=18):
        self.led = LED(led_bcm)
        self.button = Button(button_bcm)
        self.button.when_pressed = self.on_button_press
        self.button.when_released = self.on_button_released

    def on_button_press(self):
        print("Button pressed, turning led on...")
        self.led.on()
        
    def on_button_released(self):
        print("Button released, turning led off...")
        self.led.off()

    def run(self):
        print("Device is starting...")
        for i in range(2):
            time.sleep(.25)
            self.led.on()
            time.sleep(.25)
            self.led.off()

        signal.pause()


if __name__ == '__main__':
    Device().run()
