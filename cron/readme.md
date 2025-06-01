## Crontab Scripts

1. Add camera blinker and main process to startup of raspberry pi

```bash
crontab -e
```
scripts:
```
@reboot cd /home/INSERT_YOUR_USERNAME/automatic-turret-gun && ./cron/startup.bash
```
