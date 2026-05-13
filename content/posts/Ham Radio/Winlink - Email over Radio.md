---
title: Getting Started with Winlink - Email over Radio
date: 2025-10-04
lastmod: 2025-10-04
draft: true
tags:
  - Radio
  - Software
---
# Introduction
***
This is one of those things that I thought you could just slip into, but it's only slightly more complicated than that. The main thing I had trouble with was finding good, detailed walkthroughs that didn't apply to a specific radio. So this is my attempt to resolve that, but mainly to write it down for myself in the future. So without more ragchewing, let's get started.

# Winlink over the Internet
***
Alright, you might be wondering, "Huh? Why are we doing Winlink over the Internet if the article is about Email over Radio?" Well, there are two reasons: 
1. Winlink accounts are actually registered *through the winlink app*. 
	- You can not make an account on the Winlink website, but you can manage some of your account details through there *after it's created*.
2. Doing your first email through the internet (telnet) is a good way to get familiar with the application before having to tear your hair out getting your radio working with it.

So, let's get started:
1. You need to download Winlink Express from the [Downloads Tab](https://downloads.winlink.org/) on [winlink.org](https://winlink.org/) and Install it.
2. Once you open Winlink Express, Click "Settings" then "Winlink Express Setup" in the Dropdown Menu
	1. ![Winlink_Setup.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Winlink_Setup.png)
3. This will open a new window:
	1. ![Winlink_Setup_Menu.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Winlink_Setup_Menu.png)
	2. Fill out the Following Fields:
		1. "My Callsign" - Enter your callsign
		2. "My Password" - Come up with a 6-12 letter password for Winlink
		3. "Password recovery e-mail" - Enter an email you can recover a lost password from
		4. Every field in the "Registration Contact Information" section that is not marked optional
		5. "My Grid Square" to the Grid Square you're in
		6. If you have a winlink registration key, enter it. It's not required to use winlink, however, but it'd be super cool if you would support the project if you enjoy it.
		7. Lastly, make sure your Service Codes are set to "PUBLIC".
	3. Once Done, press the "Update" button to complete your registration.
		1. If you missed a step, the form will tell you once you click the "Update" Button.


You now have a Winlink account! Your address is `callsign@winlink.org`. Now that we have an account, let's try sending an email over telnet, just to get familiar with the interface.
1. Back on the Home Page, Click the "Message" Button on the top row.
	1. ![Open_Message.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Open_Message.png)
2. This should open a window that looks like this:
	1. ![Message_Window.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Message_Window.png)
	2. It's a regular email form! Fill it out with whatever you need, then click the "Post to Outbox" button at the top. Just keep in mind that messages have a size limit of 120Kb. 
3. Now that we have a message in the outbox, let's send it over telnet! Click the Dropdown Menu next to "Open Session:" in the Top Right and select "Telnet Winlink"
	1. ![Session.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Session.png)
4. Now click "Open Session:"
	1. ![Open_Session.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Open_Session.png)
5. This will open a "Session Window". Anytime you send or receive Winlink messages it will be done through a Session Window, even when sending and receiving over radio.
	1. ![Pasted image 20251004215806.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Pasted%20image%2020251004215806.png)
6. Since this is just telnet, we don't need to alter any settings usually. Go ahead and click the "Start" button.
	1. ![Start_Session.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Start_Session.png)
7. Let the window do its thing until you see it disconnect. You should see something like this:
	1. ![Session_Actual.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Session_Actual.png)
8. If you see that you sent one message, congrats! You have sent a Winlink email! Check that other email address if you can to check if it got received.
9. To receive messages, start another session. Each time you start a session, Winlink Express will send any messages that you have waiting in your outbox, and check to see if you have any messages waiting and download them.
   
   
Now that we know how to send Emails through Winlink over the internet, let's try to do it on our radio...

# Winlink over Radio
***
![Pasted image 20251007114916.png](/attachments/Ham Radio/Winlink%20-%20Email%20over%20Radio/Pasted%20image%2020251007114916.png)