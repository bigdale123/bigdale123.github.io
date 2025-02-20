---
title: First Post! Learning how to use Hugo to host Obsidian files
date: 2025-02-19
draft: false
tags:
  - Hugo
  - Obsidian
  - Homelab
categories:
  - Homelab
  - Obsidian
---
# Introduction
***
Recently, I had a really tough bug that was following me around on any linux distro I tried. System would work fine for a while, then freeze out of nowhere. I had a school project (that I massively procrastinated on) due, so I switched to windows just to get it done. Then I came back to it, realized what was causing the crashes (some issue introduced in mesa driver 24.3.0) and downgraded to an older version. It's been a week with no crashes!
Anyway, while I was troubleshooting I griped about it to some friends and I ran my mouth so much someone said I should start a blog. Not a bad idea, and it'd help me procrastinate studying for my midterm. I use Obsidian to take notes. Any kind of notes: Lecture Notes, Recipes, Shopping lists, you name it. If it is text based, I use Obsidian. Why not make obsidian files be the blog?

I watched NetworkChuck's Video to get started, but I knew that it would get a little different for me. For one, i'd like to host the static site on github pages. I've already got a domain registered that points to the github pages, and I *had* a pretty shitty svelte site running on it that I used to learn how to use svelte. If you're reading this, then that means I moved the svelte project out of this repo into another repo, and am running this blog on bigdale123.github.io. I'm sure when github eventually removes the free github pages for users, i'll scramble to get it hosted on my proxmox cluster. But for now, i'll host somewhere that won't be affected by a brown out.

# The plan
***
Shrimple.
1. Figure out how to get hugo to build static files from obsidian
2. Fix any kind of missing content errors (like missing photos and stuff)
3. Figure out how I want to "workflow" the building process, if necessary.
	1. Basically, decide if I want to automate any of this process
4. Push to github and see if the static site works
5. (Optional and If supported) Style the blog site
	1. Hugo site has themes
6. (Optional and If supported) Maybe hugo can do categorical blog posts?
	1. Haven't done any research before attempting, hence optional

# Step 1: Learning how to use Hugo
***
I'm planning on using Congo for my Hugo theme. Looks nice, can support search, tags, archives, etc. Setup has been a little difficult, because I got confused on which config directory to use. Once I figured that out, I could finally see my changes. Behold, the first thing I have seen other than a blank page!
![Pasted image 20250219224139.png](/attachments/Pasted%20image%2020250219224139.png)
We love a good RoboCop quote. If only I could figure out how to get my damn Obsidian files to show up.
(Some time later)
![Pasted image 20250219225631.png](/attachments/Pasted%20image%2020250219225631.png)
Yeah, I forgot. Whoops. 
New problem to tackle, the way Obsidian handles photos in text (following the form of `![[some_image.png]]`) is not the same as the way that Hugo handles images (following the form of `![Example Image](/path/to/some_image.png)`). Not a problem with Hugo, but we will need to follow the same route NetworkChuck used by writing a script to port over images and replace any image paths. Also not a huge deal, since the way I want to have hugo build the site will require *copying* the markdown files from my Obsidian vault to Hugo. This way I can keep my blog posts in my vault, and the script should just copy them over.

# Step 2: Fixing missing content
***
So, now for the real work. I need to write a script that will do the following (in order, ideally):
1. Copy the entire "Blog Content" folder from Obsidian to the "content" folder in the site repository.
2. For each markdown file, replace all instances of `![[some_image.png]]` with `![](/attachments/some_image.png)`
There will be more steps in the script, but for now this is all we need. I'm going to borrow from NetworkChuck's script heavily, since he has basically the same use case that I do (Source Code: https://blog.networkchuck.com/posts/my-insane-blog-pipeline/). The only thing i'll really change is probably the OS dependent versions, the OS library should include methods that will handle paths in a way that the same code can be cross platform. Here's what i'm going with, if you happen to find this (hello, you industrious little fellow) you might have to change how the attachments folder is found based on how your obsidian vault handles attachments. Mine uses an attachments subfolder in the parent directory of the markdown file.
```python
import os
import re
import shutil
import sys

def copy_vault_files(path_to_vault_folder):
    # Check that folder contains posts folder (validity check)
    if not os.path.isdir(path_to_vault_folder):
        raise IOError("Given path does not exist.")
    if not os.path.isdir(os.path.join(path_to_vault_folder, 'posts')):
        raise IOError("Given path does not contain a 'posts' folder.")

    # Recursively copy files over, maintaining the structure, including attachments
    shutil.copytree(path_to_vault_folder, os.path.join(os.getcwd(), "content"), dirs_exist_ok=True)

    # For every file that was copied over, replace obsidian formatted images with appropriate hugo image format
    for dirpath, _, filenames in os.walk("content"):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                # print(f"Markdown File: {file_path}")
                attachments_directory = os.path.join(dirpath, 'attachments')

                # Load file content and find all images matching format ![[]]
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                images = re.findall(r'\[\[([^]]+\.(?:png|jpg|jpeg|gif|bmp|svg|webp))\]\]', content)

                for image in images:
                    # Edge case: check that the image actually exists before replacing the markdown
                    # print(f"Found Image: {image}")
                    # check that attachments directory exists, only if file contains images
                    if not os.path.isdir(attachments_directory):
                        raise IOError(f"Attachments directory for file {file_path} does not exist")
                    image_path = os.path.join(attachments_directory, image)
                    if os.path.exists(image_path) and os.path.isfile(image_path):
                        # image exists, replace markdown and copy file to static/attachments
                        # copy file to static/attachments
                        new_image = os.path.join("static", "attachments", image)
                        os.makedirs(os.path.join("static", "attachments"), exist_ok=True)
                        shutil.copy2(image_path, new_image)
                        # replace markdown
                        new_markdown = f"![{image}](/attachments/{image.replace(' ', '%20')})"
                        # print(new_markdown)
                        content = content.replace(f"![[{image}]]", new_markdown)
                        print(f"Image Found in {file_path}:\n    Replacing ![[{image}]] with {new_markdown}")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
```
A tad ugly, but it gets the job done. And now we have images showing up in Hugo!
![Pasted image 20250220102903.png](/attachments/Pasted%20image%2020250220102903.png)

# Step 3: Workflowing the pipeline
***
A'ight, that's the real heavy work the python script should do. Now I need to write some other stuff that will build the static site and push it upto the github repo.

Actually, I think i'll keep this script separate from the whole publishing part. That way I can port over the obsidian files, test the server first to make sure everything renders OK, then do the publishing. Or at least a separate function, that way I can ask if somebody wants to build and push.

Just to make it easier on myself, I have set the publish dir in my `config.toml` to `docs`, since Github Pages natively supports using this directory as the build directory. Honestly, it's kinda dissapointing that GitHub won't let you pick any folder in your branch, you're stuck between /docs or /. Here's the config.toml section:
*EDIT:* I ended up undoing this for a custom github action, see next step.
```toml
# -- Site Configuration --
# Refer to the theme docs for more details about each of these parameters.
# https://jpanther.github.io/congo/docs/getting-started/

baseURL = "/"
defaultContentLanguage = "en"

publishDir = "docs"

...
```

And here's what I wrote for the publishing function, honestly I probably won't use it since it's just `hugo` then a push to the repo.
```python
def publish():
    os.system("hugo")
    commit_message = f"Automated Publish on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    os.system("git add *")
    os.system(f'git commit -am "{commit_message}"')
    os.system("git push")
```

# Step 4: See if the static site works
***
Well, if *you're* reading this you know it works. I had some trouble getting github pages to work with it. I got an error the first time I tried to have the pages action build the site, `Liquid Exception: Invalid Date: '"{{ .Date }}"' is not a valid datetime. in /_layouts/default.html`. To fix this, i added a .nojekyll file inside the docs directory, which should make pages serve the site as is. And...
It didn't work. I guess that just don't work no more 😮‍💨. I looked up what to do on the hugo docs, and they recommend a custom github action that will build the hugo site up on github.
Turns out I forgot to set `them = "congo"` in `config.toml`, but once I did that...
![Pasted image 20250220121602.png](/attachments/Pasted%20image%2020250220121602.png)
WOOP! Github Pages built and deployed the site using the action that I definitely did not copy word for word from the Hugo site 🙂. The important thing is, the site is up. We can polish all the other stuff later.

# Conclusion 🎉
***
Steps 5 and 6 are already done, since I picked my theme at the outset and that theme ended up already implementing categories. Call me lucky.
This might not have been harder than I thought it would be, but it definitely took me longer than I though it would. Maybe i'm getting slower? Whatever, the site is done. It's up. I can move on to the next thing. Maybe I should brush up on Github Actions?





