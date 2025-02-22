---
title: Getting Started with Neovim
date: 2025-02-20
lastmod: 
draft: true
tags:
  - Software
  - Linux
  - Vim
  - Neovim
categories:
  - Linux
---
I've been a VSCode user for basically all the time I've been writing code, I've tried Neovim and Vim before and couldn't get used to the keyboard shortcuts. Now that my preferred Desktop environment is i3wm, keyboard shortcuts have become more common. Basically what i'm saying is, it's time to at least branch out and try vim based editing for real. I do plan on using some plugins, which I will cover after I learn basic navigation and such.

Lastly, before I jump into this, you don't have to use vim or neovim to take advantage of the vim style keybindings. There exists many plugins for many editors that replicate this functionality.
# Basic Controls
***
A great resource is [Vim Cheat Sheet](https://vim.rtorr.com/), which has most of the common key binds detailed. I will be picking and chosing from this list for this article, mainly so that I can cut out features that I do not use currently. It should make the transition process easier, and I can still learn the other functionality at a later date if I need to. Basically, i'm using this as my own documentation on how to use vim.
## Cursor Movement
- Arrow Keys will move the cursor around, but the "vim" way is to use `h,j,k,l`. Use either.
	- `h` moves the cursor left
	- `j` moves the cursor down
	- `k` moves the cursor up
	- `l` moves the cursor right
- `<line number>gg` or `<line number>G` will jump the cursor to the line number typed.
	- `gg` on its own will jump the cursor to the first line in the document
	- `G` on its own will jump the cursor to the last line in the document
- Jumping within the screen
	- `H` will jump the cursor to the top of the screen
	- `M` will jump the cursor to the middle of the screen
	- `L` will jump the cursor to the bottom of the screen
- Jumping to a paragraph/function/block
	- `}` jumps to the next paragraph (next empty line)
	- `{` jumps to the previous paragraph (next empty line)
- Scrolling the Screen
	- `zz` will scroll the screen until the current line is in the center of the screen
	- `zt` will scroll the screen until the current line is at the top of the screen
	- `zb` will scroll the screen until the current line is at the bottom of the screen
	- `Ctrl + e` will move the screen down one line (without moving cursor)
	- `Ctrl + y` will move the screen up one line (without moving cursor)
	- `Ctrl + b` will move the screen up one page (cursor to last line)
	- `Ctrl + f` will move the screen down one page (cursor to first line)
	- `Ctrl + d` will move the cursor and screen down 1/2 page
	- `Ctrl + u` will move the cursor and screen up 1/2 page
## Insert Mode
This is the mode you will be in to actually write text. Any of these commands will place you in Insert mode (Except for the commands that take you out of insert mode 🙂):
- `i` will insert text before the cursor
- `I` will insert text at the beginning of the line
- `a` will insert text (append) after the cursor
- `A` will insert text (append) at the end of the line
- `o` will append text (open) a new line below the current line
- `O` will append text (open) a new line above the current line