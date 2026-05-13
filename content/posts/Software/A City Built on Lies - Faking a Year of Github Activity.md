---
title: A City Built on Lies - Faking a Year of Github Activity
date: 2026-05-12
lastmod: 2026-05-12
draft: false
tags:
  - Miscellaneous
  - Software
  - Engineering
  - PostOfShame
---
# This is a Post of Shame
---
I had meant to post this right after the end of the experiment, in January of 2026. But y'know, I forgot about all this and didn't feel like writing it up. Until now!



# The Github Skyline
---
Do you remember when Github introduced the skyline? It was a neat concept where it would take the activity graph you see on your Github profile and turn it into a 3d representation, and since it looked a lot like a city (if you had a lot of activity), they called it skyline. ![[Blog Content/posts/Software/attachments/Pasted image 20260512182504.png]]It originally started in 2021, and only ran as a web page until 2024. They would later turn it into a `gh-cli` extension that accomplishes the same goal. I have always wanted to print one of these skylines on my 3D printer, but I normally don't have much, if any, Github activity. Usually I do most of my development on my Seafile server, then every so often do a mass backup where I make sure there is a copy of all my work on Github. This does not make for a great activity graph.

That is when I had an idea. An awful idea. I had a wonderful, awful idea. I know just what to do! I'll write up a script that runs every day, and generates a random number of commits to a private repository every morning. That way after a year of continuous running, i'll have a nice populated skyline. And so I did just that!



# How the Script works
---
I made my script as a bash script, so that I could brush up on the syntax a bit. It's very simple. So simple, I can include the whole thing right here:
```sh
#!/bin/bash

# Set the repository directory path and Discord webhook URL
REPO_DIR="/home/dylan/gh-bot"
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."

# Navigate to the repository directory
cd "$REPO_DIR" || { echo "Failed to navigate to repository."; exit 1; }

# Generate a random number of commits (between 1 and 10)
NUM_COMMITS=$((RANDOM % 30 + 1))
echo "Creating $NUM_COMMITS commits..."

# Loop to create commits
for ((i = 1; i <= NUM_COMMITS; i++)); do
    # Generate a random number and compute its SHA256 hash
    RANDOM_NUMBER=$((RANDOM % 1000 + 1))
    HASH=$(echo -n "$RANDOM_NUMBER" | sha256sum | awk '{print $1}')

    # Overwrite the contents of hash.txt with the hash
    echo "$HASH" > hash.txt

    # Stage and commit the changes
    git add hash.txt
    git commit -m "$HASH"
done

# Push the commits to the remote repository
git push origin main || { echo "Failed to push changes."; exit 1; }

# Send a notification to Discord
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"content": "Pushed $NUM_COMMITS commits to the repository."}' \
     "$DISCORD_WEBHOOK_URL"

# Script complete
echo "Done!"
```
With some help from a handy LLM, anyway. I had this idea a week before the new year, I just wanted to get it running ASAP so I had a couple of trial runs. But you can see what it does, All it does is:
1. Decide how many commits it's going to make for today.
2. For each commit it should make, generate a hash and write that hash to a file called hash.txt.
	1. After writing to the file, commit the change. A `git add` is added for redundancy, in case the file disappeared somehow.
	2. Each commit's message is just the hash that it wrote.
3. After all the commits are made, push them all up to the repo and send out a discord notification.
The script is started via a cron job set to run every day. 



# Results
---
The script ran successfully, all 365 days of the year! That's better uptime than Github has been having, as of late. This resulted in a total commit count of 8,509 commits, averaging roughly 15-20 commits a day. Here's the activity chart for 2025:
![[Blog Content/posts/Software/attachments/Pasted image 20260512201120.png]]
And here's the skyline I printed!
![[Blog Content/posts/Software/attachments/IMG_20260512_201159780_HDR.jpg]]



# A Realization
---
This project helped me to realize commit activity is not a sole measure of proficiency or productivity, as it can be easily faked. Of course, if all the commit activity is occurring in public repositories there is a sort of "proof of work". But most people that work on personal projects likely use private repositories, especially since universities are starting to enforce the use of private repositories for homework. I have heard of several universities including this rule in their Academic Honor policies, and if somebody were to copy your work because your homework repo was public you'd get cited for a violation of this policy. I feel if you wanted to use this concept of padding your github activity to look more attractive to potential employers, "less is more". For example my activity chart is very dense, but that is because I faked my activity with the sole purpose of generating a nice skyline. If you were to sparsely pad your github activity with 1-4 commits on random days, it would probably be more believable. 


Well, that's it. Just a small little project to accomplish something I had always wanted to print. And I don't care that I cheated, I just like the way the skyline looks. 