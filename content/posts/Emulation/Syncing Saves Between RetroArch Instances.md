---
title: Syncing Saves Between RetroArch Instances
date: 2026-05-31
lastmod: 2026-05-31
draft: false
tags:
  - Emulation
  - Software
  - Homelab
---
I have recently gotten back into emulation, and took the time to actually trim the library I have down to what I would actually want to play. Believe it or not, a curated collection is more enjoyable than a hodgepodge of random games!

But I have a unique problem. I like to use RetroArch on both my PC, and on my handheld (A Retroid Pocket 3+). The neat thing is, if I can play RetroArch on my TV, I can stream it to any smart TV with moonlight installed. This makes jumping between the systems tough, as my saves aren't transferred. I find myself playing more on one system than the other, which makes me want to play on the other system less. Good news is, RetroArch has a method in their documentation for how to sync saves and other data between instances (Even BIOS Files)! And even more good news, I can self host the server that handles the synchronization!

This might be common knowledge for many people, but it wasn't for me. So I decided to write this post to both make a note for myself, but to also let others know this is possible.

{{<alert "lightbulb">}}
You don't *have* to self host the sync backend. I am self hosting it because I don't want to be dependent on a third party solution. You could instead [read the documentation](https://docs.libretro.com/guides/retroarch-cloud-sync/) and see what other backends RetroArch supports. At the time of writing, Any WebDAV server (which is what I will be self hosting) is supported on all platforms, with iCloud & iCloud Drive being supported on various devices.
{{</alert>}}
# Setting up a WebDAV server
---
RetroArch documentation states that WebDAV is a supported syncing solution *on all platforms*. So, all we should have to do is host a WebDAV server and set it up in RetroArch on both devices. Our WebDAV server needs to have a username and password, and needs to be accessible by our RetroArch devices. There are a lot of ways you could approach that, but for now, I will just be using my internal VPN to access my LAN wherever I need to. Likely the safest option for something i'm kinda throwing together.

There are many WebDAV servers out there, but the one i'll be using is rclone. You are likely familiar with or have heard of rclone, a popular tool used to bring cloud files into the local file system. You could say it's like a bridge of sorts. The important part for our needs though is that rclone can be setup to serve a WebDAV server.

So to get started, i'll spin up an LXC container on my Proxmox cluster, and setup a docker container inside. Here is the `docker-compose.yml` i'll be using:
```yaml
services:
  rclone-webdav:
    image: rclone/rclone:latest
    container_name: rclone-webdav
    ports:
      - 8080:8080
    volumes:
      - /home/dylan/rclone.conf:/config/rclone/rclone.conf
      - /home/dylan/webdav-data:/data
    command: >
      serve webdav /data
        --addr :8080
        --user dylan
        --pass <your password>
    restart: unless-stopped
```
The password field (`--pass`) needs to be replaced with your password of choice. If security concerns you, you could place the password value in a .env file.

You will also need to create a minimal `rclone.conf`. Here's mine:
```conf
[remote]
type = local
```

If all was successful, you should see something like this after the WebDAV server starts properly:
```
rclone-webdav  | 2026/05/31 15:11:55 NOTICE: Local file system at /data/local/data: WebDav Server started on [http://[::]:8080/]
```

# Configuring RetroArch for Sync
---
So the "hard part" is done, now we need to configure our RetroArch clients with the WebDAV details and setup sync.

{{<alert "triangle-exclamation">}} Check your RetroArch version!!

Cloud Sync is a relatively new feature on some platforms. For instance, Android only got Cloud Sync support in 2025. If you try to find the Cloud Sync option on your RetroArch version and it's not there, you are likely running an old version!
{{</alert>}}

We need to setup an initial client, so let's start by going to **Settings → Saving → Cloud Sync** on RetroArch.
![Pasted image 20260531101652.png](/attachments/Emulation/Syncing%20Saves%20Between%20RetroArch%20Instances/Pasted%20image%2020260531101652.png)

Now that you're in the Cloud Sync menu, Enable it and select which files you want to sync. I picked everything except "Thumbnail Images" because I currently don't use custom thumbnails. "Configuration Files" won't sync the main RetroArch config, just core configurations & options, shader presets, and high scores.
![Pasted image 20260531102014.png](/attachments/Emulation/Syncing%20Saves%20Between%20RetroArch%20Instances/Pasted%20image%2020260531102014.png)
Next we'll setup the Cloud Sync Backend. Click on that and pick "webdav", then go back to the "Cloud Sync" menu and fill in your WebDAV details.
![Pasted image 20260531102335.png](/attachments/Emulation/Syncing%20Saves%20Between%20RetroArch%20Instances/Pasted%20image%2020260531102335.png)
Now you should restart RetroArch. On the next launch, the initial sync should start and you'll see it in the bottom.
![Pasted image 20260531111057.png](/attachments/Emulation/Syncing%20Saves%20Between%20RetroArch%20Instances/Pasted%20image%2020260531111057.png)

And that should be it! All the things you configured to sync should sync! If you run into errors, make sure to turn on logging and set the level to debug.

# Results
---
After some tweaking, and updating my android version of RetroArch, cloud sync works great! In current versions of RetroArch, sometimes cloud sync just fails. If you look in the logs, it's usually a `begin failed` error, which is a known issue in the GitHub repo right now. If it does fail, you can usually just run a manual sync (with the "sync now" option in the main menu) and it will get its mind right. If it continues to fail, there is likely a problem with your WebDAV server and you'll need to check the logs to see what the issue is. Happy Emulating!