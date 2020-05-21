# ButtonLED

## Install

From inside this directory, run the following commands to install this as a
service that automatically starts at boot time:

```bash
sudo ln -s `pwd`/ButtonLED.service /lib/systemd/system/ButtonLED.service
sudo systemctl daemon-reload
sudo systemctl enable ButtonLED.service
```

At this point the program should start after you reboot the raspberry pi, or
you can start it immediately with

```bash
sudo systemctl start ButtonLED
```

Then veryify that it's running with:

```bash
sudo systemctl status ButtonLED
```