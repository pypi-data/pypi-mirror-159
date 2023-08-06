# PiTouchScreen

Programmatically control the [Raspberry Pi Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)

## Features
<details><summary><strong>GPIO Control</strong></summary>

With a button connected to pin 17:
- Cycle brightness between 50, 100, 150
- Long-press button for 1 second to turn off the screen

```bash
pi-touch-screen pi-touch-screen --channel 17 -bl 50 -bl 100 -bl 150 --power-sec 1 
```
</details>

<details><summary><strong>Thread-safe</strong></summary>
- `BacklightManager` provides thread-safe attribute access and thread-safe sysfs read/writes
- Reading or setting values requires owning a lock
- Prevents race conditions from threaded callbacks
</details>

<details><summary><strong>Install as Service</strong></summary>

- Save `pi_touch_screen_service.service` to `$HOME/.config/systemd/user/pi_touch_screen_service.service`
- Run ```systemctl --user edit pi_touch_screen_service``` and modify `ExecStart` to use your desired parameters
- Run ```systemctl --user enable pi_touch_screen_service``` to run the service at startup
</details>
