---
title: "FT8: A Beginner's Guide"
date: 2025-08-12
lastmod: 
draft: false
tags:
  - Radio
  - RTL-SDR
---
# Introduction
FT8 is a digital mode for amatuer radio that i've always wanted to try (which isn't that long, since my license is still just 2 months old at the time of writing). It's a very power efficient mode that allows for DX possibilities even with lower powered radios. It's pretty common for people to take some 5W QRP (low power) HF Radios to State Parks for Parks on The Air (POTA). In this post, I'll be learning how to do FT8 and detailing some of the options and practices that i've found to be helpful or necessary for success.
# How FT8 Works
- FT8 is a semi-automatic digital mode in amateur radio. 
	- FT8 is made up of multiple 50Hz signals within a 2.8KHz SSB space, with transmissions being about 15 seconds long.
		- ![[Pasted image 20250804113318.png]]
		- FT8 Operates on 15 Second intervals, so a Synchronized Clock is important. The clock on you computer must be within 1 second accuracy to UTC.
		- FT8 Transmissions use 8 Frequency Shift Keying, 8 tones spaced 6.25 Hz apart.
			- Each tone represents 3 bits, and results in a baud rate of about 6 bits/sec.
			- FT8 Transmissions also contain Forward Error Correction, so minor corruptions can be resolved.
	- It's very popular and can be used to determine how far out your setup can reach.
		- Also note, however, that WSPR is specifically designed for propagation testing and may provide more accurate/better results. (I say this having no experience with WSPR... Yet...)
	- The FCC Prohibits automatic operation of radios, or rather autonomous operation. So, the software used for FT8 is Semi-Automatic. 
	- You need to initiate/choose the station you want to make contact with, and for the most part, WSJTX will handle the actual conversation.
- FT8 is a more formalized mode, in that messages and conversations follow a generated format:
	- Here is an example QSO on FT8, and most contacts follow this format:
		1. `CQ AAAA EE11`: Station `AAAA` calls CQ with grid square `EE11`
		2. `AAAA BBBB DD22`: Station `BBBB` Responds to the CQ with their grid square, `DD22`
		3. `BBBB AAAA -5`: Station `AAAA` Responds to `BBBB` with a signal report of `-5` db.
		4. `AAAA BBBB R-10`: Station `BBBB` Acknowledges the signal report from earlier and sends their own signal report for `AAAA`
		5. `BBBB AAAA RR73`: Station `AAAA` says Roger Roger, thank you / best regards
		6. `AAAA BBBB 73`: Station `BBBB` says thank you / best regards
	- You *can* write custom messages, but from what I have heard these are typically used to call out bad operators (They overdrive their signal, the transmit on top of someone, etc.)
- There is another mode called JS8Call, which is based on the idea of FT8.
	- JS8Call is more free form communication, like an open chat room. Anybody on the frequency can see and send messages.
# Rig Control
- Probably going to be the hardest part of the setup process, since it is largely going to be device specific.
	- However, all setups require two things:
		- Audio in & out from the radio
		- Some way to control the radio (CAT Control, VOX, etc.)
- For some rigs with CAT control built in, you can just hook 'em up to your PC and WSJTX Might have settings for it.
	- Examples include Kenwoods, ICOMs, etc.
- For other radios, you will need to use something like flrig or similar to hook your radio up.
	- flrig is a "Man in the middle" type application that allows for a broader range of radio to work with WSJTX.
	- If you radio did not come with any kind of cables to do digital with, you can buy something like a Digirig to hook everything up. Or homebrew something.
- Largely though, you will need to look up rig specifics to figure out what you need to do. 
	- If you can decode FT8 on WSJTX, you can likely transmit.
- For me, since I use a Xiegu G90, I use the CE-19 digital expansion card that I got "for free". It was part of a bundle that was less than the cost of just the radio, so of course I get the bundle.
	- The CE-19 works, and that's about all I can say. If I could do it all again I would use a digirig. You have to build a cable for this to get the audio out, which isn't all bad on its own.
		- It's basically a culmination of issues, My setup uses 2 usb ports instead of one, it's specific to my radio, the CE-19 is a little bit tough to figure out the first time, etc. etc.
# Setting up WSJTX
### Downloading WSJTX
- Download WSJTX and run it. It might complain about no connection the first time, just close the complaint and open "File->Settings..."
### Configuring WSJTX
- First, let's hop over to General tab in settings. There are 2 settings you need to populate before trying out FT8:
	- Enter your Callsign under "My Call:" in the "Station Details" section.
	- Enter your Grid Square under "My Grid:" in the "Station Details" section.
		- You could enter the full grid square (such as EM63oj) but I'm pretty sure many people just use the large grid square (EM63 in this case)
		- Sorry if i'm not using the proper vocabulary, but I think you get what I mean. 
- Next, lets go to the Radio tab. Whatever method you used to setup your radio for control, enter that here.
	- In my case that means I use the FLRig option.
	- The sure fire way to test if WSJTX can control your radio properly is to use the "Test CAT" and "Test PTT" button. If both of these do what is expected (The "Test CAT" button should turn green and the "Test PTT" button should make your radio transmit)
	- Again, you will likely need to look up how to get your radio to talk to WSJTX.
- Lastly, We need to go to the Audio tab.
	- First, Go ahead and check both boxes in the "Remember power settings by band" section.
		- This is going to help later when we adjust our transmit audio level to prevent splattering.
	- Next, find your sound card that handles your radio. This one's going to be though to do by name alone, so if you don't know what sound card you should pick:
		- Open the sound devices menu on whatever device you are using
		- Take note of what interfaces exist
		- unplug the interface for your radio
		- Take note of which interfaces disappeared, those are your radio interfaces
	- Now you can just set the microphone and speakers accordingly.
- We're done with the settings section!
	- Back in the main window, in the lower left corner, pick your band and your mode (FT8 in this case).
	- You should be decoding FT8 Signals now! but we have a few more things to check before we attempt a QSO.
	- If your receive audio is too loud, this meter will be red. You need to adjust the level of the input device you picked in the Audio settings tab to bring the volume down until the slider is green all the time. 
		- The key test is that your audio signal should be about 30db in complete static.
	- Lastly, we need to adjust the power level for the band we are on. Look in the bottom right corner to see a power slider.
		- Tune your radio off the FT8 frequency, just for tuning the power level. It'd be inconsiderate to other operators if we splattered all over their signal while tuning.
		- If your audio output to your radio from WSJTX is too loud, your signal will splatter.
			- This basically means you will generate multiple signals, which is no good. Your splatter could broadcast over somebody elses signal.
		- Press the "Tune" button, this will output a steady consistent tone. 
			- Look at your radio and see if the ALC has been activated, or if your radio is equipped with a waterfall, if you are putting out multiple signals (there should be one "spike" on the spectrum graph, if you have like 2 or more you are splattering).
			- Adjust the power slider until the ALC turns off or you only put out one signal.
				- The key is to get the power output as high as possible without activating the ALC. 
			- Turn off the "Tune" button when done.
			- Because we enabled those "remember power settings by band" options earlier, the next time you fire up WSJTX the power setting is stored.
- Last thing, take a look at the waterfall in WSJTX. Find an empty space and move your Tx window there, then click "hold Tx Frequency". 
	- Later, if someone starts transmitting on top of your signal, just find a new empty slot and park it there.
	- Holding your Tx window makes the behavior for FT8 QSOs more consistent, i've heard. I haven't done this yet, but I will be doing this from now on. It helps keep the spectrum "organized".
- Congrats! Except for picking your Tx frequency, everything we've done is Set once and (mostly) forget. Let's talk about some optional settings you might want. 
	- I would say if this is your first time doing FT8, don't mess with these yet. But this is just text on a screen, I can't stop you if you do :)
	- A nice optional setting is in the Reporting tab, "Prompt me to log QSO". When doing a QSO in FT8, after you send a 73 back to the other person and finish the QSO, WSJTX will automatically populate a QSO log and prompt you to review the info and log the contact in WSJTX.
		- logs in WSJTX can be found by going to "File->Open Log Directory", then locating the .adi file.
	- Another optional setting I think I like is in the General tab, under the Behavior section.
		- You can click "Double-click on call sets Tx Enable" and should transmit on the next FT8 time slot.
		- "Disable Tx after sending 73" will disable Tx after you finish a QSO, totally up to personal preference.
# How to do FT8 QSOs
- Probably the easiest part of the whole thing.
	- Answering a CQ
		- Double click the person calling CQ you want to make a QSO with.
		- That's it, the software handles the conversation.
		- If you don't have "Prompt me to log QSO" turned on, when the QSO is complete click the "log" button on the main window and log the contact.
	- Calling CQ
		- You should probably enable Answering the First response to your CQ, there's a dropdown for this in the main window.
		- Just select the CQ message (usually message option 6) and enable transmit, you'll start calling CQ on the next window or the current window if there is enough time.
		- WSJTX will handle the whole conversation, pretty much. It will call CQ until someone answers, try to make the contact, then stop transmitting. Either from a completed QSO or the runaway Tx watchdog will keep your radio from transmitting constantly.
# Additional WSJTX Tools
- Grid Tracker - Hooks into WSJTX (or something like that) and displays received grid squares and active communications on a map. Really cool software.
	- https://gridtracker.org/
	- It will also spot somebody if they are doing POTA, if you answer someone calling "CQ POTA" gridtracker will automatically spot them on pota.app
# Conclusion
You'll find that FT8 is a pretty fun mode! I use a Xiegu G90 with an EFHW setup in a sloped configuration, and the first time I decided to run FT8 I made about 60 contacts in day, two of them overseas! All only on 15 watts!
![[Pasted image 20250812120756.png]]
I like to use FT8 to get a good idea of how far out I could realistically go. Of course, distance will depend on what mode you're in. SSB will shrink your effective distance due to it (sorry for the bad explanation) being a less power dense mode. Sure, I can broadcast 20 watts SSB but that power is divided over 2.8KHz of bandwidth. Where as in FT8, the 15 Watts I was using is distributed over 50Hz of bandwidth. 

FT8 is also one of those modes that you can do while you do something else. Get some laundry done, do the dishes, just pop back to your computer every once in a while to start another QSO or start calling CQ again.  