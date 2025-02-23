---
title: Getting Started with Neovim
date: 2025-02-22
lastmod: 2025-02-23
draft: true
tags:
  - Software
  - Linux
  - Vim
  - Neovim
---
![Pasted image 20250223112239.png](/attachments/Pasted%20image%2020250223112239.png)
I've been a VSCode user for basically all the time I've been writing code, I've tried Neovim and Vim before and couldn't get used to the keyboard shortcuts. Now that my preferred Desktop environment is i3wm, keyboard shortcuts have become more common. Basically what i'm saying is, it's time to at least branch out and try vim based editing for real. I do plan on using some plugins, which I will cover after I learn basic navigation and such.

Lastly, before I jump into this, you don't have to use vim or neovim to take advantage of the vim style keybindings. There exists many plugins for many editors that replicate this functionality.

# Vim Modes
***
![Pasted image 20250223112457.png](/attachments/Pasted%20image%2020250223112457.png)
Yes, yes, back to back memes. Gotta have fun with it, y'know?

Vim has different modes for accomplishing different tasks. They are:
- Normal Mode
	- The default mode, used for navigation and executing commands.
	- To get back to Normal mode from any other mode, hit `Esc` or type `Ctrl + [`.
- Insert Mode
	- Used for inserting and editing text.
	- Entered by typing any [Insert Mode](#insert-mode) keybinds.
- Visual Mode
	- Used for selecting text
	- Entered by typing:
		- `v` to do character wise selection
		- `V` to do line wise selection
		- `Ctrl + v` to do Block Selection
- Command-Line Mode
	- Used for executing vim [commands](#commands)
	- Entered by typing `:` (usually most commands are document as something like `:q`)
- Replace Mode
	- Similar to Insert mode, but replaces existing characters instead of inserting new ones.
	- Entered by typing `R`
- Select Mode
	- Similar to Visual mode but behaves similar to selection in other editors
		- Typing replaces the selection
	- Entered by typing `gh`, `gH`, or `g<C-h>`
The next section will be all the "most practical" (more common) keybinds you might need to know. It is not an exhaustive list, and is also what *I* personally think would be necessary or convenient to *me*. If you have the time, I would recommend you scroll through the cheat sheet mentioned next and see if there is anything you would like to be able to use.
# All the most practical commands I will learn
***
A great resource is [Vim Cheat Sheet](https://vim.rtorr.com/), which has most of the common key binds detailed. I will be picking and chosing from this list for this article, mainly so that I can cut out features that I do not use currently. It should make the transition process easier, and I can still learn the other functionality at a later date if I need to. Basically, i'm using this as my own documentation on how to use vim.

As a side note, if you don't understand *what* a keybind does, ChatGPT gives some really good explanations with examples.
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
## Editing in Normal Mode
- `u` will undo a change
- `Ctrl + r` will redo a change
- `.` will repeat a change
- `ciw` will replace an entire word
	- Place the cursor anywhere on/in a word, run `ciw<replacement word>`, and the word you had selected will be replaced with the replacement.
- `cw` will perform a change until the end of a word
	- `ce` will also do this but only works in the middle of a word. `cw` is more versatile since it works at the beginning and in the middle of a word.
- `cc` will change an entire line, and is generally (but not always) faster than deleting and retyping the line.
	- `c$` or `C` is similar to `cc` but is intended to replace *part* of a line instead of the whole line.
- `xp` swaps two letters, intended to be used to fix typos.
	- `x` deletes the highlighted letter
	- `p` pastes the previously deleted letter
## Visual Mode Commands
Visual Mode is entered by typing `v`. You select a block of text with your cursor.
- `>` shifts text to the right
- `<` shifts text to the left
- `y` yanks (copies) the selected text
- `d` deletes the selected text
- `~` switches the case of the selected text
	- e.g. `false` becomes `FALSE`.
- `u` changes the selected text to lowercase
- `U` changes the selected text to uppercase
## Cutting, Copying, and Pasting
- `yy` yanks (copies) a line
- `<number>yy` yanks (copies) `<number>` numbers of lines
- `yw` yanks from where the cursor is to the beginning of the next word
- `yiw` yanks the word under the cursor
- `y$` yanks from cursor to the end of the line
- `p` puts (pastes) the clipboard after the cursor
- `P` puts (pastes) the clipboard before the cursor
- `dd` deletes (cuts) a line
- `<number>dd` deletes (cuts) `<number>` number of lines
- `dw` deletes (cuts) from the cursor to the start of the next word
- `diw` deletes (cuts) the word under the cursor
- `d$` or `D` deletes (cuts) from cursor to the end of the line
- `x` deletes (cuts) a character
## Indenting
- `>>` indents a line one shiftwidth
- `<<` de-indents a line one shiftwidth
- `gg=G` re indents the entire buffer (Visual Mode)
- `=%` re indents the entire block inside a `()` or `{}` (Cursor must be on one of the braces)
- `]p` puts (pastes) with adjusted indentation
- `<number>==` re indents `<number>` number of lines
# Special vim-like stuff
***
This is gonna be the section for stuff that aren't commands, but are sorta specific to vim editors.
## Registers
- `:reg[isters]` shows all registers content
- `"xy` yanks whatever is selected into register x
- `"xp` pastes whatever is in register x where the cursor is
- `"+y` yanks whatever is selected into the system clipboard
- `"+p` pastes from the system clipboard where the cursor is
- Special Registers:
	- `0` holds the last yank
	- `"` is an unnamed register, holds the last delete or yank
	- `%` holds the current file name
	- `#` holds an alternate file name
	- `+` holds the system clipboard
	- `/` holds the last search pattern
	- `:` holds the last command run
	- `.` holds the last inserted text
	- `-` holds the last small delete (less than a line)
	- `=` is the expression register
		- This register holds the result of an expression, handy for not having to use `:call`
	- `_` is the black hole register
		- Like `/dev/null` as a register, anything written to it disappears
		- Can be useful when you want to delete something but not affect any registers
## Macros
- `qa` records a macro and stores it as macro `a`
- `q` stops recording whatever macro is currently being recorded
- `@a` runs macro `a`
- `@@` runs the last run macro
# Commands
***
I'm separating this from the prior section because commands are started with colons. They are different, and are typically longer than the previous keybinds which make them different. It is too early to be writing like this.
## Exiting
- `:w` saves the current file, but does not exit.
	- `:wq` or `:x` or `ZZ` saves the current file and then quits
- `:q` quits out of vim (will not work if there are unsaved changes)
- `:q!` or `ZQ` quits out of vim and throws out unsaved changes (quit without saving)
- `:wqa` saves the file and quits on *every* tab.
## 