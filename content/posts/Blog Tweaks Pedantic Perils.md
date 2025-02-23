---
title: "Blog Tweaks: Pedantic Perils"
date: 2025-02-23
lastmod: 2025-02-23
draft: false
tags:
  - Hugo
  - Obsidian
---
I'm really digging my Hugo blog since I put it together in [This Post](https://blog.coeus.icu/posts/first-post-learning-how-to-use-hugo-to-host-obsidian-files/), but I wanted to make some tweaks to match some of the appearance in Obsidian, as well as some little tweaks like enabling theme switching. 

# Removing back-ticks from inline code
***
When inline code got rendered using the congo theme, initially they got rendered with the backticks as part of the inline code. 
![Pasted image 20250223143626.png](/attachments/Pasted%20image%2020250223143626.png)
I found that in Hugo, you can add a `custom.css` under `assets/css`. And then I also found a site where somebody else running a Hugo blog/site that also uses Congo had some CSS rules that would remove the backticks from inline code. That site is [here](https://applegamer22.github.io/posts/hugo/), and the CSS rules are:
```css
.prose :where(code):not(:where([class~="not-prose"] *))::before {
	content: unset !important;
}
.prose :where(code):not(:where([class~="not-prose"] *))::after {
	content: unset !important;
}
```
These remove the wrapper symbols (im guessing?) from before and after anything with the `code` style associated. I'm sad to say that I am not as educated as I should be on CSS, while I *can* figure out what CSS does, I can't just look at it and understand what a snippet does. That was part of the reason I wanted to try building the blog in the first place.
So now inline code has no backticks:
![Pasted image 20250223144744.png](/attachments/Pasted%20image%2020250223144744.png)
# Adding a background to inline code
***
Let's go! A little dopamine hit goes a long way, now I want to make the inline code have a background, like how this codeblock does.![Pasted image 20250223144907.png](/attachments/Pasted%20image%2020250223144907.png)
Basically, I want the Hugo site to mimic the style that Obsidian uses, while following the color pattern of the Congo theme.
This took a little doing, since I didn't understand how tailwind works. Tailwind CSS, for those that don't know, is essentially a set of predefined styles that you can use to define some complex CSS styles. This means that your css files need to be *post-processed* in order for the tailwind rules to be applied. I had forgotten this, so my first attempt was to simply copy the `.chroma` rule into the code rule in my custom CSS from the Congo `main.css`:
```css
code {
  word-wrap: break-word; /* All browsers since IE 5.5+ */
  @apply break-words;
  @apply rounded-md bg-neutral-50 py-3 text-neutral-700 dark:bg-neutral-700 dark:text-neutral-200;
}
```
This probably *would* have worked, if the custom css was pre processed. But it's not, and I didn't realize this for half a day. Just clicking rocks together the whole time.
![smooth_brain.gif](/attachments/smooth_brain.gif)
This probably would have been so much faster to implement if I had a clue what I was doing. Anyways, I did have a good thought: tailwind css is just css. So, ask chatgpt to rewrite the tailwind rule I wrote, and...
```css
.prose :where(code):not(:where([class~="not-prose"], [class~="not-prose"] *)) {
    background-color: #f0f0f0 !important; /* Force light mode */
    word-wrap: break-word;
    overflow-wrap: break-word;
    border-radius: 0.200rem;
	padding-inline: 0.25rem;
}

.dark .prose :where(code):not(:where([class~="not-prose"], [class~="not-prose"] *)) {
    background-color: #404040 !important; /* Force dark mode */
}
```
I did take some stuff out, so that it's just the rules you need to get the background. If you are implementing this for yourself, you might want to tweak the background colors for the respective appearance modes. This is what I think works for me. And now...
![Pasted image 20250223153340.png](/attachments/Pasted%20image%2020250223153340.png)
Looking good!
# Adding Appearance Toggle
***
We've reached the portion of the post where i'm just tackling small stuff.
I ended up putting an appearance toggle in the footer, and the menu.
```toml
# params.toml
[footer]
  # showCopyright = true
  showThemeAttribution = true
  showAppearanceSwitcher = true
  showScrollToTop = true
```
```toml
# menus.en.toml
[[main]]
  identifier = "appearance"
  weight = 95
  [main.params]
    action = "appearance"
```
That's about it. See ya.

