---
title: Building a BBS in 2026
date: 2026-07-13
lastmod:
draft: false
tags:
  - Software
  - Homelab
  - Self-Hosting
  - VintageComputing
  - BBS
  - Synchronet
  - C64U
---
# I Got a New Toy

So I recently was able to purchase a Commodore 64 Ultimate, which is a bucket list level achievement for me. I have always wanted to own a Commodore 64, they are very cool machines. I would still like to own an original someday, but for now this suits me just fine.

![Pasted image 20260714092937.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714092937.png)

One of the things I wanted to try doing with the C64U right after it arrived was getting it connected to the internet. I had heard that the C64U has a modem emulator built straight into it. To test this out, I figured I would start a self-hosted bulletin board system (BBS) that I could connect to from any emulator I wanted, so I built "The Daily Byte."

![Pasted image 20260714093046.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714093046.png)

The Daily Byte is a Synchronet bulletin board system running on a Docker container, and this blog post will be about setting up and customizing my Synchronet BBS.

## Installing Synchronet

[Synchronet](https://www.synchro.net/) is a free, modern bulletin board system software that runs on pretty much any platform you can think of. It's built mostly on an older syntax of JavaScript and supports translation to a lot of older terminal styles. In practice, this means you can write all your user menus in one language, and Synchronet will adapt it on the fly for whatever system is currently connected. It has terminal detection built in to make that translation process as easy as possible.

I installed Synchronet using a [Docker container](https://github.com/bbs-io/synchronet-docker). Setting up the Docker container is very easy, all you have to do is follow the instructions on the GitHub page, and it will automatically create all the directories it needs and boot up almost instantly. That's really all there is to it. Here's my docker-compose.yml, the commented out section are optional additional services you can run alongside the server. My compose file is likely not perfect, but has a lot of the "unnecessary" ports turned off. 

```yaml
version: "3.8"
services:
  sbbs:
    container_name: sbbs

    # -- LOCAL BUILD ----------------------------
    # build:
    #  context: ./docker
    # image: bbsio/synchronet:local
    # -------------------------------------------

    # -- LATEST RELEASE -------------------------
    image: bbsio/synchronet:nightly
    # -------------------------------------------

    # -- NIGHTLY --------------------------------
    # Nightly images are tagged with
    #
    # Latest Nightly - sometimes may be broken
    # image: bbsio/synchronet:nightly
    #
    # Specific year-month-day as follows.
    # image: bbsio/synchronet:nightly-YYYYMMDD
    # image: bbsio/synchronet:nightly-20210225
    # -------------------------------------------

    deploy:
      restart_policy:
        condition: any
    volumes:
      - /home/dylan/sbbs-data:/sbbs-data
    networks:
      - sbbs
    environment:
      - TZ=America/Chicago
    ports:
      #- 80:80 #http
      #- 443:443 #https
      #- 1123:1123 #ws-term
      #- 11235:11235 #wss-term
      - "8021:21" #ftp
      - "8022:22" #ssh
      - "8023:23" #telnet
      - "8513:513" #rlogin
      - "6400:64" #petscii 40-column
      - "1280:128" #petscii 128-column
      #- "25:25" #smtp-mail
      #- 587:587 #smtp-submit
      #- 465:465 #smtp-submit+tls
      #- 110:110 #pop3
      #- 995:995 #pop3+tls
      #- 119:119 #nntp
      #- 563:563 #nntps
      #- "18:18" #message send prot
      #- "11:11" #active user svc
      #- "17:17" #qotd
      #- 79:79 #finger
      #- 6667:6667 #irc
      # - 5500:5500 #hotline
      # - 5501:5501 #hotline-trans
      # - 24554:24554 #binkp
      # - 24553:24553 #binkps
      # - 143:143 #imap
      # - 993:993 #imap+tls
  # sbbs_irc:
  #   container_name: sbbs_irc
  #   build:
  #     context: .
  #   deploy:
  #     restart_policy:
  #       condition: any
  #       delay: 3s
  #   volumes:
  #     - $PWD:/sbbs-data
  #   command: sbbs-run jsexec /sbbs/exec/ircd.js
  #   ports:
  #     - 6667:6667

  #
  # # Door Party Connector
  # #
  # # Save: ~/sbbs/mods/doorparty.js
  # #       https://raw.githubusercontent.com/bbs-io/doorparty-connector-docker/master/synchronet/doorparty.js
  # #
  # # Add the following to modopts.ini (optional)
  # #
  # #   [doorparty]
  # #   tunnel_host=doorparty
  # #   tunnel_port=9999
  # #
  # doorparty_connector:
  #   hostname: doorparty
  #   container_name: doorparty_connector
  #   image: bbsio/doorparty
  #   environment:
  #     - SSH_USERNAME=TODO
  #     - SSH_PASSWORD=TODO
  #     - SYSTEM_TAG=[TODO]
  #     - LOCAL_INTERFACE=0.0.0.0
  #     - LOCAL_PORT=9999
  #     - SSH_HOST=dp.throwbackbbs.com
  #     - SSH_PORT=2022
  #     - RLOGIN_HOST=dp.throwbackbbs.com
  #     - RLOGIN_PORT=513
  #   deploy:
  #     restart_policy:
  #       condition: any
  #   networks:
  #     - sbbs

networks:
  sbbs:
    name: sbbs
```

There is one extra step you have to take to get PETSCII terminals working with Synchronet. PETSCII refers to the unique graphical character set found on most Commodore machines. To enable it, you'll need to edit `sbbs.ini`, found in the Synchronet `ctrl` folder. Scroll down to the BBS section of the config file and edit the `TelnetInterface` variable to equal:

```
[BBS]   Terminal (Telnet, SSH, RLogin, Raw-TCP) Server
	...
	TelnetInterface = 0.0.0.0, 0.0.0.0:64, 0.0.0.0:128
	...
```

This tells Synchronet which ports on the Docker container to use for PETSCII support. When you try to connect to your BBS from a Commodore system, make sure to point your Commodore terminal to the correct port: the IP address of your BBS, with port 64 for a Commodore 64 or port 128 for a Commodore 128.

Once you've done all that, you should have a fully functioning bulletin board system running on your own network. But we're not done yet, we still need to go into the Synchronet config menu and change some settings so we can create our first user.

Take some time to get familiar with the Synchronet Config menu, often called SCFG, because you'll be using it quite a lot. SCFG is where most of Synchronet's options are configured, so it's worth learning your way around its menus.

![Pasted image 20260714095007.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095007.png)

To create our first user, we'll need to set the System Operator (sysop) password. Open the System menu, then Security Options, then change the system password under System Password. I'd recommend making it fairly long, since this server runs primarily on Telnet connections and is likely to be compromised if you ever make it public.

![Pasted image 20260714095036.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095036.png)

Once you've configured your sysop password, you can connect to the BBS through a program like [SyncTERM](https://syncterm.bbsdev.net/). Configure your BBS connection in SyncTERM, generally you can use the standard Telnet port, port 23. Once you log in, you should see a login page like this:

![Pasted image 20260714095240.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095240.png)

From the login page, type `new` to create a new user and follow the account prompts. This will be the system operator account for the BBS you're creating, so make sure to configure it correctly the first time and use a password you'll remember.
![Pasted image 20260714095422.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095422.png)

Once you've created your account, log in and follow the on-screen prompts until you reach the main menu. If you make it there, congratulations, you're running your own bulletin board system.

## Customizing Synchronet

Now let's talk about customizing Synchronet. The main thing you'll probably be customizing are what Synchronet calls "messages." Here are some example message files that come with Syncrhonet by default:
![Pasted image 20260714095746.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095746.png)
![Pasted image 20260714095756.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095756.png)
![Pasted image 20260714095835.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714095835.png)
Messages are static text files typed using Ctrl-A codes that can contain ASCII or CP437 characters, as well as @ Codes that let you include special variables within a msg file. They're written this way so it's easy to translate the message files into other character sets for different terminals. The best way to edit a message file is with [PabloDraw](https://github.com/cwensley/pablodraw), an editor that lets you create message files much like a modern paint program.

One of the first things you can customize, and one of the easiest, is the banner that displays on the login page. Open the `banner.msg` file in PabloDraw and make your changes. Just keep in mind that you should try to match the original size if you want to preserve the shape of the login screen.

Keep in mind that editing message files and menu files only changes the _look_ of a menu, not the actual availability of commands. I don't recommend making changes to the menu files themselves, because in Synchronet, most features are pretty closely tied together. If you want to remove a menu item, you can remove it from the menu and then, on the page you would have reached, add a note saying that feature isn't currently supported, just so anyone who ends up there anyway knows.

If you do decide to change the actual behavior of a menu, don't edit the original JavaScript file in the `exec` folder. Instead, copy it into the `mods` folder and make your changes there. Any JavaScript file in the `mods` folder with the same name as one in the `exec` folder will be loaded in its place, so you keep a clean copy of the stock file in `exec` alongside your modified version in `mods`.

The last thing I'll cover, because so far it's the only other thing I've tried customizing, is doors. Doors are external programs you install onto your BBS so users can access them. One example: if you go to the External Programs menu, under Games, Minesweeper comes installed by default. That's a door.
![Pasted image 20260714100417.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714100417.png)

Doors are just programs stored in the external program section. Synchronet actually comes with quite a few doors already in the `exec` folder's external directory, they just aren't pre-installed. You can install them using their `install-xtrn.ini` files, which automate the process. If a door doesn't come with an ini file, you can still install it manually by telling Synchronet where the door needs to launch from and how to launch it. For the specifics, refer to the Synchronet documentation at wiki.synchro.net, since there are several ways to do this depending on what files are available.

To demonstrate how to install a door using an `install-xtrn.ini` file, I'll show you how I installed my own door, called Synchro-Wordle, a Wordle clone written for Synchronet bulletin board systems. I'll be putting out another blog post detailing how the game works under the hood.

To start, clone my Wordle GitHub repo into the `xtrn` folder under a `wordle` subfolder. Once it's cloned, run the install command from the README in my GitHub repo. Running the `install-extern.ini` file should step you through all the decisions needed to install the door. Once it's installed, you should see it appear in the External Programs menu.
![Pasted image 20260714100444.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714100444.png)
From there, you should be able to launch the door by selecting it from the menu.

![Pasted image 20260714100500.png](/attachments/Self%20Hosting/Building%20a%20BBS%20in%202026/Pasted%20image%2020260714100500.png)
## Conclusion

So far I've had a lot of fun configuring, customizing, and building my bulletin board system. It's not currently publicly available, mainly because of the security concerns around opening up a bunch of Telnet ports to the internet. If I figure out how to safely host The Daily Byte publicly, I will. For now, I don't have any plans beyond running it on my LAN, or maybe a free instance somewhere down the line.

If you're still reading, it's worth mentioning that there are hardening instructions on the Synchronet wiki for making your BBS more secure. If I ever decide to make my BBS public, I will likely make a blog post detailing the steps I took to make it more secure than it is now.