---
title: Listening to the Police Scanner with SDR Trunk
date: 2025-02-20
lastmod: 2025-02-20
draft: true
tags:
  - RTL-SDR
  - Software
  - Miscellaneous
categories:
  - RTL-SDR
  - Miscellaneous
---
Now that I have a blog, I wanted to document how to do this because it's a niche-r hobby. I had, not a difficult time, but *a* time getting this working properly, and finding out how to setup playlists. All told though, it's fun to get setup.
# What is trunking?
***
In a nutshell, Trunking is when multiple users need to share a pool of radio frequencies. There is a control channel that manages which frequencies are in use and who are using them, and who is requesting to use a channel. Talkgroups are roles within the system assigned to users, and allow for group based permissions. When a user initiates a transmission, the control channel will tell the user what channel it can use. When a transmission is made on that channel, all the members of the same talkgroup will receive the transmission. Are you getting it now?

SDR Trunk is specifically made to work with the following trunking (and some non trunking) protocols:
- **AM** - AM demodulator
- **APCO-25 Phase 1 (C4FM/Simulcast)** - P25 message decoder and automatic trunked channel following.
- **APCO-25 Phase 2** - Phase 1 control channels with automatic Phase 2 trunked channel following.
- **DCS** - Digital Coded Squelch (DCS) decoder for NBFM channels
- **Fleetsync II** - FM demodulator and decoder for ANI, Acknowledge, Status, Paging and GPS bursts
- **FM/NBFM** - narrow-band FM demodulator with squelch control.
- **LJ1200** - FM demodulator and decoder for LoJack data bursts on 173.075 MHz in US.
- **LTR-Net** - FM demodulator and LTR-Net trunked radio signaling decoder
- **LTR-Standard** - FM demodulator and Logic Trunked Radio (LTR) trunked radio signaling decoder
- **MDC-1200** - FM demodulator and decoder for MDC-1200 ANI bursts.
- **MPT-1327** - FM demodulator and MPT-1327 trunked radio signaling decoder and automatic trunked channel following.
- **Passport** - FM demodulator and Passport trunked radio signaling decoder.
- **Tait 1200** - FM demodulator and decoder for Tait CCDI protocol GPS location bursts.

# Getting RTL-SDR drivers installed
***
This is gonna be platform specific, but we need drivers to use RTL-SDR devices. *Please* follow the official quick start guide @ [airspy.com](https://www.rtl-sdr.com/tag/install-guide/) and make sure your dongle is plugged in before continuing (how will we know the dongle works if it's not plugged in?)

On *most* linux systems, just install the `rtl-sdr` package for your system and you're rolling. Run `rtl_test` to see if your device is detected. If not, a common reason that it isn't getting picked up is because it is stuck in dvb-t mode. You can fix this by blacklisting the dvb-t module from being loaded, like so:
```shell
$ cd /etc/modprobe.d
$ sudo nano dvb_blacklist.conf
[in the config file, add this line]
blacklist dvb_usb_rtl28xxu
```

On windows systems, it's a little more involved. Download the SDR# package, run `install-rtlsdr.bat`, then run the `zadig.exe` it downloaded. Go to the options tab, and select "List all devices". Sometimes you need to uncheck "Ignore hubs or composite patterns". Then, select "Bulk-In, Interface (Interface 0)", make sure the driver box says "WinUSB ...", then click Replace Driver.

Mac seems like you don't need to do anything? weird. But I don't care. Moving on!

# Install & Setup SDR Trunk
***
Pretty easy, download from the [Releases Page](https://github.com/DSheirer/sdrtrunk/releases/latest) or install through your package manager (I used the AUR). Once done, you should see an interface like this:
![Pasted image 20250220165945.png](/attachments/Pasted%20image%2020250220165945.png)
You will likely get prompted to perform CPU calibrations if it's the first time running the program, go ahead and accept. Let it do it's thing.
While that's going, we can actually do one more thing. We need to install the JMBE library, responsible for audio decoding. Click the "Create Library" button, and install the jar file. You should see something like this in the settings menu once it's setup properly:
![Pasted image 20250220170416.png](/attachments/Pasted%20image%2020250220170416.png)
By now, the JMBE library and the CPU calibration should both be done. The blue, red, orange thing is called a "waterfall". Basically a spectrum analyzer, and it's purpose is to show signals and their strength in the range of frequencies being viewed. If it is killing your resource usage, you can disable it by right clicking on it and disabling it.

# Building our Playlist
***
Alright, here's the true hard part of getting SDR Trunk working. SDR Trunk uses a playlist to manage all the information needed for listening to trunked systems. This includes:
- Channels (Frequencies, Protocols, Names, etc.)
- Aliases (Talkgroups, Aliases, & identifiers)
If you bare bones it, it's not hard, but you will be missing some useful data like correct talkgroups and aliases and stuff. 

I ***Highly*** encourage you to pay for a [Radio Reference](https://www.radioreference.com/), just one time. They're not expensive, and it's worth the time you can save. Because...
![Pasted image 20250220172550.png](/attachments/Pasted%20image%2020250220172550.png)
You can import all the data for your area straight from Radio Reference if you have a subscription!
![yippee-happy.gif](/attachments/yippee-happy.gif)
Just make an account, buy a subscription, and then import a system. If you really want to make the most out of your subscription, Backup your playlists of imported data before your subscription runs out. Then in the future, just update any relevant data when a channel quits working.

I will not go over how to build a playlist manually, if you want to do that (masochist) go read the [SDRTrunk Wiki](https://github.com/DSheirer/sdrtrunk/wiki) and figure it out yourself.

# Tuning into a site
***
So easy it doesn't really deserve a section.
- Go to the playlist editor
- select your playlist
- go to the channels section
- Find the site you want to listen to
- click on it, then press the play button
![Pasted image 20250220173132.png](/attachments/Pasted%20image%2020250220173132.png)
You can see in my playlist that I picked the "Jefferson County Simulcast" site, and the big play button. 
![Pasted image 20250220173227.png](/attachments/Pasted%20image%2020250220173227.png)
You should have success! If you see a "CONTROL" channel, you've tuned into the trunked system correctly. If aliases are set up properly, those will show up in the Alias column. 
Any sub channels that are pink and say "ENCRYPTED" can't be played, but any blue channels that say "CALL" can. SDRTrunk can play 2 calls at the same time, one on the left audio channel and another on the right audio channel. It can get chaotic, and I haven't learned how to enforce a single call to play at a time.

You can setup recording each snippet that comes in for any given alias, just go to the alias and set it to record audio. Whenever a call occurs with the alias being part of that call, the audio segment will get saved to disk.

That's about all I know, SDRTrunk is a neat program to run every once in a while. I'll put a link to my playlist [here]() once I get it uploaded in the blog repo.

Speaking of blog, This post is the first post to contain a gif! Which I thought was previously not going to work, but I forgot I already implemented that when I wrote my import script.
![think-smart-meme-945257677 1.gif](/attachments/think-smart-meme-945257677%201.gif)