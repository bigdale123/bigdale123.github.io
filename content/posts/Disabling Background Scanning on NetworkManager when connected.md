---
title: Disabling Background Scanning on NetworkManager when connected
date: 2025-02-27
lastmod: 
draft: false
tags:
  - Networking
  - Linux
  - Miscellaneous
---
Cheeky little blog post :)

I use Moonlight & Sunshine to do remote gaming, and it works fine on an Ethernet connection. However, when you switch to using Wifi there are lag spikes about every 2-3 minutes. I looked up if anybody else was having this issue on wifi, and most of the posts that I read said that it was related to background scanning of networks. I searched for a way to do this, couldn't find a clear answer, and last resort asked chatGPT. And what do you know, it was right for once! So, the below solution is courtesy of our AI overlords.
***
### 1. **Modify the NetworkManager Configuration**
Edit (or create) the configuration file:
```bash
sudo nano /etc/NetworkManager/conf.d/no-scanning.conf
```

Add the following lines:
```ini
[device]
wifi.scan-rand-mac-address=no

[wifi]
scan-generated-ssid=1
disable-connected-scans=true
```

### 2. **Restart NetworkManager**
Apply the changes by restarting NetworkManager:
```bash
sudo systemctl restart NetworkManager
```

### 3. **Verify the Setting**
Check if scanning is disabled while connected:
```bash
nmcli device wifi rescan
```
If scanning is disabled, the command should fail or not return new networks.

---
This configuration prevents NetworkManager from continuously scanning for new networks while you are already connected. If you experience any connectivity issues, you can revert these changes by removing or modifying the file.