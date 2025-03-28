---
title: Taking Pictures of Space
date: 2025-03-28
lastmod: 2025-03-28
draft: false
tags:
  - Photography
  - Miscellaneous
---
I am no photographer. I take pictures, but they're not impressive. I pretty much only use my phone camera, a 64MP *Android* phone camera, so I lack the cool post processing that iOS devices do to make their photos better than the typical android based phone. Still, if possible i'd like to try taking cool space pictures with just my phone. So this post is going to be me documenting my experiments and methods to aid anyone in the future (and myself) who wants to try this.

Like all the other posts I have made, this ended up being a dumping ground for any information I ran into while trying to get (what I call) a good star picture.

# Background
***
Let's talk about how you're *supposed* to do astro-photography. According to [Space.com](https://www.space.com/astrophotography-for-beginners-guide#section-camera-bodies-and-lenses), the best kind of setup is a camera that has a full-frame sensor. These pick up the most light, and make them an ideal choice for taking really dark photographs.

They are referred to as full-frame because the sensor size is the same size as a frame of 35mm film. Other cameras use what's called a crop sensor, which are smaller than a frame of 35mm film but have their image blown up to fit that frame. These are cheaper to manufacture than full-frame sensors, which means that a full-frame sensor is going to be expensive. You can see in the below picture that the sensor on the right is the full frame sensor, and will capture *much* more data than the sensor on the left.
![Pasted image 20250307140948.png](/attachments/Pasted%20image%2020250307140948.png)
As I stated before though, i'm trying to do this on the cheap, so we're just going to use our phone and whatever sensor it has on it. Sorry if I got any details wrong in the section before, like I said i'm no photographer.

Now, since we're not using a full-frame camera, we'll need to increase our exposure time to capture a similar amount of data to the full frame sensor. The exposure time is how long the shutter remains open and the camera receives and stores data. With short exposure times you can take good pictures without blurring, but a downside is that the image sensor takes in less data and the image becomes darker as a result. This gets corrected by the ISO and white balance settings (again, not a photographer, might be wrong, that's the gist tho). The longer the exposure time, the more data you can log but the more prone the image is to blurring. Think about it this way: If the camera remains perfectly still, any new data that hits the sensor gets added to the existing pixels of the image. If the camera gets bumped or something walks in front of it while it's taking its picture, that data gets added to the pre existing pixels also. This is what causes blurring, data getting added on top of pre existing data.

We can fix these issues with two pieces of low cost equipment: A tripod and a shutter remote. The tripod *is necessary*, but the shutter remote isn't. It's just a convenience, we can take the picture without touching the camera which won't cause it to shake. If you don't want to buy a shutter remote (they are pretty inexpensive), you can simply make a shutter timer and set it to a small amount of time. This way the camera waits X amount of seconds to actually open the shutter, allowing the camera to get still again after touching it before it actually takes the picture. The Tripod will elevate your camera and keep it still.

# I have no idea what i'm doing
***
I tried this while I was at the beach. I had hoped to get a really cool photo of the beach, ocean, horizon, and the stars above all at once. Think like a sunset on the beach picture, but instead of a sunset you can see the milky way. Cool idea, right? So I went out and bought a cheap tripod, waited until night, put my phone camera in pro mode and...
![Pasted image 20250307142415.png](/attachments/Pasted%20image%2020250307142415.png)
![Pasted image 20250307142432.png](/attachments/Pasted%20image%2020250307142432.png)
![Pasted image 20250307142536.png](/attachments/Pasted%20image%2020250307142536.png)

I mean, not bad for a first attempt and little to no research, but woof. They're grainy, inconsistent, and they still blew me away the first time I tried. I couldn't see 75% of the stars that were out with my eyes, so this was still really cool and totally worth the $10 i spent on a tripod. This was back in September of 2024, and now that it's starting to get warm again i'm looking to try to improve my results. Here's what my settings were when I tried these photos, i'm approximating however because I didn't write down what I was doing. Something that I sorely regret now.

| Setting                  | Value      |
| ------------------------ | ---------- |
| Exposure                 | 32 seconds |
| ISO                      | ?          |
| White Balance            | ?          |
| Focus                    | Infinite?  |
| Exposure Correction      | Auto       |
| F Stop (uncontrollable?) | 1.8        |
The only thing I really remember is just cranking the exposure time up. Glad we're revisiting this so I can make it scientific (or, at least adjacent to scientific).

# Research
***
Sticking with the space.com article, let's talk about what the ideal camera settings should be. The Aperture (F-Stop) should be wide open, as open as it can go. Turns out my phone has an aperture size of 1.7, which is pretty good!. In order to capture as much data as possible, we should be saving images raw, no jpg or png or any processing at all.
Now, for exposure times...
### The 500 Rule
If our exposure time is too long, the stars will trail (desired if you're trying to shoot star trails). If it's too short, you won't capture enough data. There is a sure-fire way to find out how long our exposure time should be, and all we do is divide 500 by the focal length of our camera lens. The result of this is the exposure Time.
$$\frac{500}{Focal\ Length\ in\ mm} = Exposure\ Time\ in \ Seconds$$
So, for my camera, $\frac{500}{4.71\ mm}=106.1571\ seconds$, which is longer than my camera can do...
But the equation doesn't take into account crop factor. If we factor in crop factor (found [here](https://astrobackyard.com/the-500-rule/)), the equation looks like this: $$\frac{500}{Focal\ Length \times Crop\ Factor}=Exposure\ Time\ in\ Seconds$$
Multiplying the crop factor with the focal length is like saying "This is what the focal length would be if this were an equivalent full frame camera lens". So, $\frac{500}{4.71\ mm \times 5.35}=19.8424\ seconds$, much more achievable for my camera. *If* this ends up not being enough data, we can either take our picture in a less light polluted zone or use an intervalometer. Intervalometers allow for longer exposure times by busting up the exposure time into smaller chunks, the only difference is we need to tell the intervalometer the rotation of the sky so it can "track" the stars and not cause blurring.

### ISO Sensitivity
This will largely be the result of experimentation. ISO amplifies the light signal captured by the camera, but this also means that if the ISO is too high it will introduce noise into the image. Our ISO will need to be high since we are photographing a sky with no bright light source.

### Focus
This should be dead simple. Set your focus to manual focus, zoom into the brightest star in the frame, then adjust the focus until the star is as sharp as possible.

### White Balance
Again, something that should be the result of experimentation. This isn't something that will affect the *quality* of the image though, so it's alright to not have a hard rule and we could even leave it on auto. Generally though, slightly cooler white balances are preferred for astro shots. If light pollution ends up being an issue, we can get a light pollution filter to help remove it.

### Ryan Borden (goat)
I found [this](https://www.youtube.com/watch?v=4XWFeeSl-Gc) video while researching camera settings, and it's a great resource. It talks about what camera settings do, best practices for taking night shots, when to take them, etc. 
- The moon is bright, and could ruin our shot. The closer to a new moon you try to take your shot, the more light we get from stars.
- If you're shooting the milky way, time of year matters. If you're in the northern hemisphere, it's best to try shooting in your spring to fall season. 
- Get to a dark spot, and face south if you're shooting the milky way. Use a dark spots map to find which areas are darkest.
- Put your camera in manual mode.
- Have your aperture as open as possible, maybe get a wide angle lens to get a lot in your frame
- [500 rule](#the-500-rule)
- Shoot in RAW. 
- Get your [focus dialed in](#focus)
- Adjust white balance to cancel out any artifacted colors (4000K)
- ISO, 2000-4000 is the ideal range.
	- If you lower your ISO, increase your expsoure length.
	- If you raise your ISO, lower your exposure length.
He even includes a slide containing all the best practices he talks about during the video at the end of the video,
![Pasted image 20250307173915.png](/attachments/Pasted%20image%2020250307173915.png)
### Cody Mitchell (goat)
A video that *really* helped me understand camera settings was Cody Mitchell's [9 Years of Camera Setting Knowledge in 29 Minutes](https://www.youtube.com/watch?v=vu5ohljtB-A). It really helps to understand the *relationship* between settings, and how to take correct exposures. Please go watch the video, it explains it in such good detail with examples. Cody also provides a cheat sheet with diagrams that explain most of what he talks about in his video, which I will be borrowing from to back up my own explanation. I still encourage you to get your own copy of the cheat sheet, since it is well put together and a valuable resource.

The main concept in his video is the idea of the "Exposure Triangle". The three core settings you will use on your camera (that have the most impact on the exposure) are:
- Aperture
- Shutter
- ISO
In his video, he shows that to achieve the same exposure after changing one setting, you must adjust another setting accordingly. The idea is a Triangle, if you change one side of the triangle the other two sides must compensate to achieve the same exposure.
![Pasted image 20250313114006.png](/attachments/Pasted%20image%2020250313114006.png)
Another key thing that I knew (but hadn't realised) is that higher ISO = more grain. I knew it does, but it had never set in, yknow? So really, you should shoot at the lowest *reasonable* ISO. I understand that in some situations, you have to raise it in order to make your picture bright enough, but ideally you should try changing aperture and shutter speed first before raising it. Because as mentioned before, Higher ISO leads to a grainier image.

Another key thing I learned was that the amount you have to adjust another setting is directly affected by how many stops you changed another setting by. Increase the F Stop by 3 stops? shutter speed needs to change by 3 stops. Increase the ISO 3 stops? The aperture needs to be changed 3 stops. Those are examples, but the idea is simple. 

That's all i'm going to talk about from his video and cheat sheet, I *really* recommend looking at his resources for yourself and making your own realizations.
# Experimenting
***
## Experiment 1: Exposure Time
We've established what the exposure time *should* be, but I want to see what it *can* be before we mess with the ISO and WB. This will be done with the stock camera app in "Pro" mode, the exposure lengths will be the selectable exposure lengths. So, the steps between will be unequal. ISO will be set to 3000, and WB to 4000K to start. We will experiment with those next, after we have found our "ideal" exposure time (the one I think looks best).
Here are the results:

| Exposure Length | Picture                              |
| --------------- | ------------------------------------ |
| 0.5"            | ![Pasted image 20250310213745.png](/attachments/Pasted%20image%2020250310213745.png) |
| 1"              | ![Pasted image 20250310213751.png](/attachments/Pasted%20image%2020250310213751.png) |
| 1.3"            | ![Pasted image 20250310213757.png](/attachments/Pasted%20image%2020250310213757.png) |
| 1.6"            | ![Pasted image 20250310213802.png](/attachments/Pasted%20image%2020250310213802.png) |
| 2"              | ![Pasted image 20250310213808.png](/attachments/Pasted%20image%2020250310213808.png) |
| 2.5"            | ![Pasted image 20250310213813.png](/attachments/Pasted%20image%2020250310213813.png) |
| 3.2"            | ![Pasted image 20250310213819.png](/attachments/Pasted%20image%2020250310213819.png) |
| 4"              | ![Pasted image 20250310213824.png](/attachments/Pasted%20image%2020250310213824.png) |
| 5"              | ![Pasted image 20250310213831.png](/attachments/Pasted%20image%2020250310213831.png) |
| 6"              | ![Pasted image 20250310213836.png](/attachments/Pasted%20image%2020250310213836.png) |
| 8"              | ![Pasted image 20250310213841.png](/attachments/Pasted%20image%2020250310213841.png) |
| 10"             | ![Pasted image 20250310213846.png](/attachments/Pasted%20image%2020250310213846.png) |
| 13"             | ![Pasted image 20250310213851.png](/attachments/Pasted%20image%2020250310213851.png) |
| 16"             | ![Pasted image 20250310213857.png](/attachments/Pasted%20image%2020250310213857.png) |
| 21"             | ![Pasted image 20250310213903.png](/attachments/Pasted%20image%2020250310213903.png) |
| 27"             | ![Pasted image 20250310213908.png](/attachments/Pasted%20image%2020250310213908.png) |
| 32"             | ![Pasted image 20250310213913.png](/attachments/Pasted%20image%2020250310213913.png) |
## Experiment 2: ISO vs. WB
For this experiment, I picked an exposure based on the results of the [500 rule](#the-500-rule). For me, this resulted in a exposure length of 21 seconds (well, actually 19.84 something, but i picked the nearest setting I had on my phone's camera app). And here are the results of that:

| WB/ISO   | 2000K                                | 3000K                                | 4000K                                | 5000K                                | 6000K                                | 7000K                                | 8000K                                |
| -------- | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ISO 100  | ![Pasted image 20250310213935.png](/attachments/Pasted%20image%2020250310213935.png) | ![Pasted image 20250310213939.png](/attachments/Pasted%20image%2020250310213939.png) | ![Pasted image 20250310213945.png](/attachments/Pasted%20image%2020250310213945.png) | ![Pasted image 20250310213950.png](/attachments/Pasted%20image%2020250310213950.png) | ![Pasted image 20250310213954.png](/attachments/Pasted%20image%2020250310213954.png) | ![Pasted image 20250310213959.png](/attachments/Pasted%20image%2020250310213959.png) | ![Pasted image 20250310214005.png](/attachments/Pasted%20image%2020250310214005.png) |
| ISO 500  | ![Pasted image 20250310214011.png](/attachments/Pasted%20image%2020250310214011.png) | ![Pasted image 20250310214016.png](/attachments/Pasted%20image%2020250310214016.png) | ![Pasted image 20250310214021.png](/attachments/Pasted%20image%2020250310214021.png) | ![Pasted image 20250310214025.png](/attachments/Pasted%20image%2020250310214025.png) | ![Pasted image 20250310214030.png](/attachments/Pasted%20image%2020250310214030.png) | ![Pasted image 20250310214034.png](/attachments/Pasted%20image%2020250310214034.png) | ![Pasted image 20250310214038.png](/attachments/Pasted%20image%2020250310214038.png) |
| ISO 1000 | ![Pasted image 20250310214044.png](/attachments/Pasted%20image%2020250310214044.png) | ![Pasted image 20250310214048.png](/attachments/Pasted%20image%2020250310214048.png) | ![Pasted image 20250310214053.png](/attachments/Pasted%20image%2020250310214053.png) | ![Pasted image 20250310214057.png](/attachments/Pasted%20image%2020250310214057.png) | ![Pasted image 20250310214102.png](/attachments/Pasted%20image%2020250310214102.png) | ![Pasted image 20250310214106.png](/attachments/Pasted%20image%2020250310214106.png) | ![Pasted image 20250310214120.png](/attachments/Pasted%20image%2020250310214120.png) |
| ISO 2000 | ![Pasted image 20250310214132.png](/attachments/Pasted%20image%2020250310214132.png) | ![Pasted image 20250310214138.png](/attachments/Pasted%20image%2020250310214138.png) | ![Pasted image 20250310214144.png](/attachments/Pasted%20image%2020250310214144.png) | ![Pasted image 20250310214149.png](/attachments/Pasted%20image%2020250310214149.png) | ![Pasted image 20250310214154.png](/attachments/Pasted%20image%2020250310214154.png) | ![Pasted image 20250310214159.png](/attachments/Pasted%20image%2020250310214159.png) | ![Pasted image 20250310214203.png](/attachments/Pasted%20image%2020250310214203.png) |
| ISO 3000 | ![Pasted image 20250310214217.png](/attachments/Pasted%20image%2020250310214217.png) | ![Pasted image 20250310214223.png](/attachments/Pasted%20image%2020250310214223.png) | ![Pasted image 20250310214228.png](/attachments/Pasted%20image%2020250310214228.png) | ![Pasted image 20250310214233.png](/attachments/Pasted%20image%2020250310214233.png) | ![Pasted image 20250310214238.png](/attachments/Pasted%20image%2020250310214238.png) | ![Pasted image 20250310214242.png](/attachments/Pasted%20image%2020250310214242.png) | ![Pasted image 20250310214247.png](/attachments/Pasted%20image%2020250310214247.png) |
| ISO 4000 | ![Pasted image 20250310214253.png](/attachments/Pasted%20image%2020250310214253.png) | ![Pasted image 20250310214257.png](/attachments/Pasted%20image%2020250310214257.png) | ![Pasted image 20250310214302.png](/attachments/Pasted%20image%2020250310214302.png) | ![Pasted image 20250310214307.png](/attachments/Pasted%20image%2020250310214307.png) | ![Pasted image 20250310214312.png](/attachments/Pasted%20image%2020250310214312.png) | ![Pasted image 20250310214317.png](/attachments/Pasted%20image%2020250310214317.png) | ![Pasted image 20250310214322.png](/attachments/Pasted%20image%2020250310214322.png) |
| ISO 5000 | ![Pasted image 20250310214328.png](/attachments/Pasted%20image%2020250310214328.png) | ![Pasted image 20250310214335.png](/attachments/Pasted%20image%2020250310214335.png) | ![Pasted image 20250310214341.png](/attachments/Pasted%20image%2020250310214341.png) | ![Pasted image 20250310214346.png](/attachments/Pasted%20image%2020250310214346.png) | ![Pasted image 20250310214351.png](/attachments/Pasted%20image%2020250310214351.png) | ![Pasted image 20250310214357.png](/attachments/Pasted%20image%2020250310214357.png) | ![Pasted image 20250310214403.png](/attachments/Pasted%20image%2020250310214403.png) |
| ISO 6000 | ![Pasted image 20250310214410.png](/attachments/Pasted%20image%2020250310214410.png) | ![Pasted image 20250310214419.png](/attachments/Pasted%20image%2020250310214419.png) | ![Pasted image 20250310214426.png](/attachments/Pasted%20image%2020250310214426.png) | ![Pasted image 20250310214430.png](/attachments/Pasted%20image%2020250310214430.png) | ![Pasted image 20250310214437.png](/attachments/Pasted%20image%2020250310214437.png) | ![Pasted image 20250310214443.png](/attachments/Pasted%20image%2020250310214443.png) | ![Pasted image 20250310214450.png](/attachments/Pasted%20image%2020250310214450.png) |
| ISO 6400 | ![Pasted image 20250310214522.png](/attachments/Pasted%20image%2020250310214522.png) | ![Pasted image 20250310214528.png](/attachments/Pasted%20image%2020250310214528.png) | ![Pasted image 20250310214533.png](/attachments/Pasted%20image%2020250310214533.png) | ![Pasted image 20250310214538.png](/attachments/Pasted%20image%2020250310214538.png) | ![Pasted image 20250310214543.png](/attachments/Pasted%20image%2020250310214543.png) | ![Pasted image 20250310214548.png](/attachments/Pasted%20image%2020250310214548.png) | ![Pasted image 20250310214553.png](/attachments/Pasted%20image%2020250310214553.png) |

Based on the results, I like 5000K, but would probably end up doing something between 4000K and 5000K. And in terms of ISO, something between 1000 and 500 seems ideal. Something I don't understand yet is why the images all have the center brighter than the rest of the image, but maybe that is due to sideways light pollution? I took these in the backyard, there was light from porch lights, the moon, windows, etc. It might also be beneficial to bump my exposure time to the nearest setting *below* the 500 rule, as 21" is a little bright and stars look like they're just starting to trail.

Upon further research, the reason for this is vignetting. It's caused by the aperture being open too wide, so now I need to find a way to make it smaller (If that is even possible on this phone). 

Something cool you might notice, this ends up being a timelapse of the sky moving. If you look at the brightest star in all the pictures, you can see that it moves towards the bottom right of the frame. Here's a gif, pretty cool (seizure warning, the changes in WB can be a little rapid).
![9mxvtz.gif](/attachments/9mxvtz.gif)

# Getting Serious
***
After doing research, I started to get some videos showing up in my youtube feed. And holy shit, it may be the best thing for this project. This guy on youtube, [Nebula Photos](https://www.youtube.com/@NebulaPhotos) has extremely detailed and informational videos describing *exactly* how to take *any* space picture with any camera, using an intervalometer and a program called [DeepSkyStacker](http://deepskystacker.free.fr/english/index.html) to calibrate our images. Following his steps should result in a higher quality picture going forward, so before we continue doing experiments lets break down some of the key information he talks about in [this](https://youtu.be/iuMZG-SyDCU?si=slRR-4r9ejgeQuyh) video:

## Gear and Prep
A lot of this section is info we've already covered in the [research](#research) section of this article, so i won't talk about much. Basically,
- Shoot in Raw
- If you can afford/have it, an actual camera suited for the shot you want
- Check light pollution on the map and try to find a suitable dark sky spot to take your photo
- Turn off *all* the auto modes on your camera; auto denoise, auto wb, auto focus, etc.
I'm skimming here, if you want a more in depth discussion please watch the gear and prep sections of his video. But that was not what made me think his video is [fantastic](https://media1.tenor.com/m/56CE99HqWyQAAAAd/fant4stic-say-that-again.gif), it was the next section about calibrating your image.

## Calibration
When I first started this project (which I didn't think could be classified as a project, but here we are after a lot of work) I did not understand the purpose of flat frames and bias frames, nor how to use them with a stacking software or anything. This video is what made it click for me, since he explains the purpose of each frame and how to make those frames so clearly. Another good resource for understanding how these frames are taken and what they do is [Galactic Hunter's calibration frames post](https://www.galactic-hunter.com/post/calibration-frames).
- **Bias Frames**
	- These frames are used to subtract the noise that the image sensor of your camera makes on its own, from the image we take. 
		- If you have a removable lens, this is done with the lens off.
	- You can take one set of bias frames and reuse them over and over, assuming you don't change cameras or ISO. The bias frames will be unique to your camera and the ISO you shoot it at.
	- To make a bias frame,
		- Set the ISO to the ISO you want to shoot your photos at
		- Set the shutter speed to the shortest it can be (Approaching zero, so something like $\frac{1}{1000}"$ or smaller)
		- Take the bias frame picture in *complete darkness*. Put the lens cap on, cover the camera up, anything to take a completely black picture.
	- You should take at least 30, but the more the better. 50 seems to be the preferred number.
- **Dark Frames**
	- These frames are similar to bias frames, in that they are shot in complete darkness. Except, these frames match the exposure time and ISO of our light frames (the "actual" pictures).
		- If you have a removable lens, this is done with the lens off.
	- Your dark frames should have the exact same settings as your light frames (actual pictures), just taken in complete darkness (hence the name, "Dark Frames").
	- Unlike bias frames, these will need to be retaken whenever a setting is changed, it is not just dependent on ISO. 
	- Again, take at least 30, but the more the better. 50 seems to be the preferred number.
- **Flat Frames**
	- These are responsible for helping take care of vignetting in your images. 
		- vignetting is common when using lenses with wide apertures.
	- To take a flat frame (these can be tricky),
		- Take a picture of a flat white light source. This can be a T-shirt over the camera, a light panel, etc. You just need to take a picture that is a well-lit all white image.
		- Set the exposure of your flats to the setting that makes your histogram peak be in the middle of the graph.
			- It doesn't need to be dead center, but it should be in the middle third of the histogram at least.
	- Again, take at least 30 flat frames, 50 preferred.

That should be it, although if you have a modded camera or something you will need to replace some frame types with different frame types (Example: if you have a cooled sensor camera, instead of biases you will take Dark Flat Frames instead). If you need different calibration frame types, please see [Galactic Hunter's calibration frames post](https://www.galactic-hunter.com/post/calibration-frames).

It should also be noted that you don't have to take these calibration frames before you go take your light frames. You can do this after, all though you will need to know what settings you shot your lights at to make effective calibration frames. Write them down if you plan to make your calibration frames later.

## Capturing
Once you get to your shooting location, block out any light sources you can from hitting your camera. In the video, Nebula Photos blocks some street lights from getting into his shot by propping up a sterilite container. I actually 3D printed a lens hood for my phone camera, that attaches using a hair tie. I went for a cheap option, there were some options to buy a lens hood for my phone but it was $20. My 3D print is less than a dollar, cost of 3D printer not included (because if it was it'd be like a $300 lens hood :)).

Now, find the thing you want to photograph. Get your camera situated before moving on. In the video, he's taking a picture of the Orion nebula, so he finds the Orion nebula before proceeding.

Next, we focus our camera. In the video he uses a Bahtinov mask to focus, but you can also focus without a Bahtinov mask.
- Zoom in your camera to the brightest star in the picture.
	- If using a Bahtinov mask,
		- Place your Bahtinov mask on your lens and look at the star. There should be a line coming off of the star if it is not in focus.
		- Adjust the focus until the star makes a 6 pointed diffraction pattern (like a six pointed star).
		- See [AstroBackyard's post](https://astrobackyard.com/bahtinov-mask/) for some examples.
	- If not using a Bahtinov mask,
		- Adjust your focus until that star is the most in focus it can be. The star should get smaller the more in focus it is, so when the star is smallest that *should* be the focus you need to be at.
		- To test, you can take a picture (with shorter exposure and different settings, since we are zoomed in) and zoom in as much as you can. 
			- If the stars look crisp, they're in focus. 
			- If they look blurry, they're not.
		- Basically, just fiddle with the focus point until the stars are the most in focus to you.
- Zoom back out to the zoom level you want

Get your intervalometer setup if you are using one. You'll want to take more pictures if the thing you are trying to photograph is farther out in space. If you use an intervalometer, you'll want to use the NPF method to determine exposure time per shot, instead of the 500 rule.

Once you've got your shots, pack up and head home to stack and post process.

## Pre-processing
The stacker being used is [DeepSkyStacker](http://deepskystacker.free.fr/english/index.html), which will calibrate your lights using calibration frames taken earlier. Overall, it will make our image cleaner and make more stars appear.

1. In DSS (DeepSkyStacker), click "open picture files" and load in your light frames.
	1. Now click "dark files..." to load in your dark frames.
	2. Click "flat files..." to load in your flats
	3. Click "bias files..." or "dark flats..." (depending on your setup) to load those in.
2. Click "Register Checked Pictures" to register all the pictures we just loaded.
	1. Check to make sure every type of frame was loaded
	2. Check that "Automatic Detection of Hot pixels" is enabled in the Actions tab
	3. Go to the Advanced tab and click "Compute the number of detected stars", let it do its thing.
		1. If you don't get a lot of stars back, you can lower or raise the star detection threshold to adjust how it detects stars. 
	4. Click "Recommended settings" in the Action tab to view recommended settings
	5. Click "Stacking Parameters" in the Action tab to view stacking parameters
	6. Click "OK" to start calibrating.
3. Sort your imported photos by score, pick the highest scoring picture as your reference frame (right click, "use as reference frame")
4. On the left, click "Stack checked pictures" and review the settings. I would probably roll with the defaults the first time around, experiment later.
5. Go do something else while it stacks, it might take a while. Once done, it should output a `Autosave.tiff` in your lights folder.

## Post-processing
You might be dissapointed at what comes out of DSS (might be pretty dark), but don't worry. The image will look better after post-processing in Photoshop or a similar program like gimp. The following instructions are pretty much step-by-step from the Nebula Photos video, so they're photoshop oriented. GIMP users, you're on your own. Maybe in the future I can figure out a GIMP workflow, if so I will write a new article (this one's hella long!)

Also, photos to come later, once I get a chance to try this. Just copying it down so I can start learning some of it.
1. Open that `Autosave.tiff` in your photo editor.
	1. It should open it as a 32 bit image, don't change this yet.
2. Duplicate the initial layer, and call it "First Stretch"
	1. This is the step where we flatten the image.
	2. Open the levels menu (histogram) and you should see a large spike on the left of the histogram.
		1. Move the middle slider towards the spike a little bit and press OK. This should bring the spike closer to the center and spread it out a bit. 
			1. It's OK if the image becomes light, we'll fix this later.
		2. Reset the black point to just before the beginning of all the data and press ok.
		3. Repeat this process until that spike has been stretched out enough that we get some details in our picture. Don't over do it though, we don't want to clip any data out, we're essentially re-ranging the existing data in the stacked image.
3. Now we can switch the image to "16 bits per channel mode".
	1. If it asks if you want to merge, say "don't merge".
4. Duplicate the stretch layer and call it "background removal".
	1. Select everything (Ctrl-A) and then copy the layer (Ctrl-C). Now, open a new image. It should copy the size of the image from the clipboard.
	2. Name this new image "bg".
	3. Delete the (should be blank) background layer.
5. In the "bg" project, Open your "Filter dust, noise, and scratches" menu in your editor.
	1. Set your radius to something on the lower end, in the video it was 60.
	2. For the halos that are left, use spot healing to fix and remove those halos.
		1. The goal is to have an image that is just the light pollution gradient. The gradient should be as smooth as possible, we're removing the hot spots that stars introduce.
	3. Once the image looks clean enough, save both projects (The original we opened in step one and this "bg" file we created)
6. In the original project file (step 1 file) deselect everything and pick the "background removal" layer.
	1. We are going to "Apply image"
	2. In the menu that opens, select the source as the "bg" file we created.
		1. Pick the layer that contains the gradient in the "layer section"
		2. Set the blending method to "Subtract"
			1. Looking at the picture behind the menu window, change the offset (starting at 10, increasing by 10) until you get to a point where the image is fairly gray, but flat.
				1. The key thing we are looking for is detail, we don't want to lose any stars subtracting the gradient.
			2. Once it looks good, hit "OK".
7. duplicate the layer, name it "second stretch".
	1. Open the levels menu again, and stretch the histogram out like before. 
		1. This time, the goal is to add *contrast* to the image and bring out more data from our tiff file.
	2. Now open the Curves menu, and apply an aggressive S curve. Bring the mid levels up and take the shadows down.
8. Duplicate the layer, name it "saturation"
	1. We're going to raise the saturation on our image.
	2. Open the hue/saturation menu, and adjust the saturation to make the colors pop, but don't add so much that you get color noise (color appearing out of nowhere).
		1. Worth noting that if there is a feature you want to saturate without affecting the rest of the image, mask off the feature in a new layer (or layer mask) and adjust the saturation of the feature.
			1. Gotta be honest, the way he described it doesn't make sense to me *yet*, but it shouldn't be too hard. 
9. You will likely have some artifacting on the edges, just crop those out. 
10. color correction. 
	1. Necessary if some stars have a halo that distracts you from the subject of the image, if you have a subject
	2. Make a new layer from visible, name it "halo correction"
	3. open the "Select by Color Range" menu
		1. This is easy to overdo, if you do, start over
		2. set the fuziness to 40 (or keep it at default)
		3. set the selection criteria to "sampled colors"
		4. select a bunch of colors that you want to mute/correct
			1. check the selection preview to see if it is good enough selection
			2. play around with settings to get desired selection
		5. press OK
	4. If there are selections where you dont want them, do the following:
		1. press Q to bring up the selection mask overlay (?)
		2. with the brush tool, paint in black the spots you *don't* want color corrected.
		3. Press Q again to exit
		4. using the selection, create a layer mask (adjustment layer?) to change the hue/saturation of the selection
			1. Open the hue/saturation properties for the layer mask
			2. play around with the values to fix the stars.
			3. Hit OK when done.
11. Final whole image color correction, to make the blacks truly black
	1. Your black of the void of space might not be completely black, you can adjust the whole image to make it look right.
	2. Open a selective color adjustment layer (sorry gimp folks, idk what this is yet)
		1. Set the colors options to "blacks"
		2. adjust the color options until the image looks as desired.
12. Done! Export the image as desired.

# Trying out with new info
***
Now that I have watched the whole video, I want to try to take a good picture. One you'd hang up on the wall.

Using the [new NPF rule](https://sahavre.fr/wp/regle-npf-rule/) that is mentioned, my exposure times need to be about 10.3 seconds (i'll round down to 10s). In a single picture, this will be darker but we're taking dozens if not hundreds of light frames, so that should make up for it in post processing.
![Pasted image 20250318160941.png](/attachments/Pasted%20image%2020250318160941.png)

My intervalometer will be DeepSkyCamera, an android app that handles it all via software. I plan on taking 360 light frames, which equates to about an hour of exposure time. Here are the settings for each exposure:
- Exposure Time: 12s
- ISO: 200
- WB: 5900K (Daylight-ish)

And here's the results from that:
![Much_Better_Success.png](/attachments/Much_Better_Success.png)
Not bad! It's noisier than I anticipated, but there's more stars than before. That big bright one in the center is Mars, which happened to be directly above. Something I failed to realize was that because it was straight up, it rotated the fastest. I took about 135 light frames, but only ended up stacking about 30 of those because of how much the constellation had moved. In the future, maybe I should take a smaller group of photos and then recenter the subject of my photograph before taking another "bank". This could all be avoided if you use a star tracker, but those are expensive. Some DIY Options exist, but I don't think im that invested yet. 

Thanks for reading! I know it was a long one, but it ended up being a larger rabbit hole than I thought it would be.