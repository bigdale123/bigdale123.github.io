---
title: Getting Started with Neovim
date: 2025-03-05
lastmod: 2025-03-05
draft: false
tags:
  - Software
  - Linux
  - Vim
  - Neovim
---
![Pasted image 20250223112239.png](/attachments/Pasted%20image%2020250223112239.png)

Finally, I can do the part of the original post I planned on! If you're unaware, [I made a post before this one about vim keybinds](https://blog.coeus.icu/posts/a-mostly-exhaustive-list-of-keybinds-and-commands-for-vim/). This post was originally intended to be a complete article detailing what key binds I was going to learn *and* getting neovim setup with some plugins and settings to help out anybody else that got intimidated by the learning curve. And as you can see, the key binds and commands became a really long list. This post will be about configuring Neovim and setting it up with plugins.

My hope is that mainly, I can document my setup so that I can understand it later when I forget what things do.

# Neovim Settings
***
By default, Neovim looks like this:
![Pasted image 20250225124857.png](/attachments/Pasted%20image%2020250225124857.png)
It might change a little for you, but this is pretty much how it looks out of the box. And if you open up a file...
![Pasted image 20250225124940.png](/attachments/Pasted%20image%2020250225124940.png)
This is what it should look like. You'll notice it's missing some features that we might have in other editors like VSCode, like line numbers, syntax highlighting, etc. And this isn't because it can't do those things, it's just that they are not enabled by default. Vim and other vim-like editors (Neovim) are built to be incredibly lightweight while still being a powerful editor. Things that might cause the editor to take longer to draw get disabled, in favor for faster draw times which make the editor feel and behave faster. Another reason for this is it makes the editor *much* faster to launch. You may notice when you open VSCode, it takes a couple of seconds to load *everything*. It takes about a second to load enough to the point where you can start using it, opening files and editing them. With vim editors, it's near instant. It loads up, file open, ready to edit in almost no time at all.

So now that we know why these features are turned off, lets turn them back on. Unless you are running Neovim on a potato, enabling these really shouldn't affect the speed of the editor at all, only marginally. The real speed killer will be plugins, but there's something we'll cover later to help remedy that in the plugins section. I will be using [This Site's start config](https://builtin.com/software-engineering-perspectives/neovim-configuration) to start my vim config (which for Neovim is located at `~/.config/nvim/init.vim):
```vimscript
" Basic Settings
" **************
set nocompatible            " disable compatibility to old-time vi


" Selection Behavior
" ******************
set showmatch               " highlights matching brackets (),[],{}
set ignorecase              " makes search patterns case insensitive
set hlsearch                " highlight all search matches
set incsearch               " show matches as search pattern is typed


" Mouse and Cursor Behavior
" *************************
set mouse=a                 " enable mouse support
set cursorline              " highlights the line where the cursor is


" Tab and Indentation Settings
" ****************************
set tabstop=4               " number of columns occupied by a tab 
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed


" UI Enhancements
" ***************
set number                  " adds line numbers
set wildmode=longest,list   " adds command line autocomplete
							"     longest = longest unambiguous match
							"     list = displays all possible matches
set cc=80                   " set an 80 column border for recommended line length
set ttyfast                 " Scrolls as fast as the terminal supports


" File Type and Syntax Highlighting
" *********************************
filetype plugin on          " turn on file-type-specific plugins
filetype plugin indent on   " allow auto-indenting depending on file type
syntax on                   " syntax highlighting


" Clipboard
" *********
set clipboard=unnamedplus    " use system clipboard for copy/paste
" set backupdir=~/.cache/vim " Directory to store backup files.
```
This is already a pretty good start! I tried out the `set cc=80`, thinking it would just be a line and not highlight the whole column. It wasn't so I disabled it, but maybe I will revisit later if I can find a solution that's not too invasive. Here's what Neovim looks like now:
![Pasted image 20250225195802.png](/attachments/Pasted%20image%2020250225195802.png)
It's already a lot nicer to work with, being able to use the mouse (even though I should be using the keyboard) is a nice addition. The mouse is still pretty limited on it's own, which I think will wean me off of using the mouse. It's mainly just nice to be able to move the cursor with the mouse.

# Appearance
***
Right now I think I am happy with the way it looks, but I also want to go ahead and lay out some groundwork for myself in the future. I am also going to setup background transparency, I just like being able to see stuff behind my terminal.

#### Transparency
I've done this in the past, but after not realizing that I didn't back up my dotfiles correctly I lost that configuration 😭. I remember that I did it without a plugin, so it *should* be possible to write it in vimscript. I'm just at a loss trying to find it in other storage, so I guess i'll have to find in on *The Internet*. Thankfully, you can throw a rock and hit vim/neovim configs. [Here's a site](https://blog.chaitanyashahare.com/posts/how-to-make-nvim-backround-transparent/) that had a "vanilla" (plugin independent) method to get transparency working. Just add the following to your config:
```vimscript
highlight Normal guibg=none
highlight NonText guibg=none
highlight Normal ctermbg=none
highlight NonText ctermbg=none
```
And you're good to go:
![Pasted image 20250225204310.png](/attachments/Pasted%20image%2020250225204310.png)
Can you tell I've been watching Severance? 

### Color Schemes
Even though I don't intend on installing a color scheme right now, I would like to already have all the groundwork laid out so that in the future all I have to do is swap out one theme for another. Vim and Neovim actually already come with some preinstalled color schemes, accessible through the `:colorscheme` command. Some color schemes require 24 bit color, though, and this wont make it a persistent change. Here's what i've added to my config:
```
set termguicolors
colorscheme default
```
And that should be about it. If I install a colorscheme in the future, it'll be as a plugin, and still be accessible through `:colorscheme`. 

# Plugins
***
It's time. The moment that *i've* been looking forward to. **Plugins**. 

This is where the cool stuff happens, and (can) add a *ton* of functionality to vim. They can add syntax highlighting, autocompletion, Git integration, and more. You can find most of all the plugins available at [vim-awesome](https://vimawesome.com). But, these can make vim load slower, so let me introduce you to what will be the most important plugin for me: [Lazy.nvim](https://github.com/folke/lazy.nvim). This plugin manager *Lazily* loads plugins, meaning that plugins get loaded when they try to get used. This keeps it fast, while still being able to handle a lot of plugins. It's kind of like a library: when you want to read a book you don't have to pull every book off the shelf first, you just grab the book you want. In fact, [LazyVim](https://www.lazyvim.org/) is a neovim setup that is powered by lazy.nvim. It comes with a bunch of plugins installed and pre configured. I've also used this in the past, and while it's nice, I think it is a little overkill for me. So, i'll be selecting my plugins myself.

There's one more order of business before we start installing plugins, and that's because i'm using lazy.nvim. The documentation specifies you need to setup lazy in `init.lua`, and not `init.vim` like i'm using now. So, I need to translate my `init.vim` to an equivalent `init.lua` 😞
```lua
-- Appearance
-------------
vim.opt.termguicolors = true
vim.cmd([[colorscheme default]])
vim.cmd([[highlight Normal guibg=none]])
vim.cmd([[highlight NonText guibg=none]])
vim.cmd([[highlight Normal ctermbg=none]])
vim.cmd([[highlight NonText ctermbg=none]])

-- Basic Settings
-----------------
vim.opt.compatible = false  -- Disable compatibility to old-time vi

-- Selection Behavior
---------------------
vim.opt.showmatch = true    -- Highlight matching brackets
vim.opt.ignorecase = true   -- Case-insensitive searching
vim.opt.hlsearch = true     -- Highlight all search matches
vim.opt.incsearch = true    -- Show matches as search pattern is typed

-- Mouse and Cursor Behavior
----------------------------
vim.opt.mouse = "a"         -- Enable mouse support
vim.opt.cursorline = true   -- Highlight the current line

-- Tab and Indentation Settings
-------------------------------
vim.opt.tabstop = 4         -- Number of columns occupied by a tab
vim.opt.softtabstop = 4     -- See multiple spaces as tabstops
vim.opt.expandtab = true    -- Convert tabs to spaces
vim.opt.shiftwidth = 4      -- Width for auto-indents
vim.opt.autoindent = true   -- Maintain indent of current line

-- UI Enhancements
------------------
vim.opt.number = true       -- Show line numbers
vim.opt.wildmode = { "longest", "list" } -- Command-line autocomplete
-- vim.opt.colorcolumn = "80" -- Set an 80 column border for recommended line length
vim.opt.ttyfast = true      -- Enable fast terminal scrolling

-- File Type and Syntax Highlighting
------------------------------------
vim.cmd([[filetype plugin on]])
vim.cmd([[filetype plugin indent on]])
vim.cmd([[syntax on]])

-- Clipboard
------------
vim.opt.clipboard = "unnamedplus" -- Use system clipboard for copy/paste
-- vim.opt.backupdir = os.getenv("HOME") .. "/.cache/vim" -- Directory for backup files
```
On the plus side, now that it's lua the code block highlights the syntax. That's nice.
### Lazy.nvim
If you're following along, please read the [Official lazy.nvim documentation](https://lazy.folke.io/) to install it since it might change overtime. At the time of install, following the structured setup, all you need to do is add a requirement to `init.lua` and the definition of that requirement., `lua/config/lazy.lua`. The `lazy.lua` file is what bootstraps lazy.nvim and sets it up.

Here's the file structure for lazy.nvim:
```
~/.config/nvim
├── lua
│   ├── config
│   │   └── lazy.lua
│   └── plugins
│       ├── spec1.lua
│       ├── **
│       └── spec2.lua
└── init.lua
```
And `lazy.lua`:
```lua
-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  local lazyrepo = "https://github.com/folke/lazy.nvim.git"
  local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
  if vim.v.shell_error ~= 0 then
    vim.api.nvim_echo({
      { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
      { out, "WarningMsg" },
      { "\nPress any key to exit..." },
    }, true, {})
    vim.fn.getchar()
    os.exit(1)
  end
end
vim.opt.rtp:prepend(lazypath)

-- Make sure to setup `mapleader` and `maplocalleader` before
-- loading lazy.nvim so that mappings are correct.
-- This is also a good place to setup other settings (vim.opt)
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

-- Setup lazy.nvim
require("lazy").setup({
  defaults = {
    lazy = true,
  },
  spec = {
    -- import your plugins
    { import = "plugins" },
  },
  -- Configure any other settings here. See the documentation for more details.
  -- colorscheme that will be used when installing plugins.
  install = { colorscheme = { "default" } },
  -- automatically check for plugin updates
  checker = { enabled = true },
})
```
Now let's install some plugins!

### vim-airline
Let's start off simple, since I don't actually trust that I installed lazy.nvim correctly. [vim-airline](https://github.com/vim-airline/vim-airline) is a "lean & mean" status line that sits just above the command area and below the window. I just think it looks better than the standard status line, and it should be a simple introduction to Plugin Specs.

lazy.nvim uses something called a "spec" to define plugins for lazy.nvim. This defines where to download a plugin, the config of that plugin, what it's priority is, whether to load the plugin lazily, etc. I gotta be honest, having used VimPlug (another vim plugin manager) in the past I kind of miss being able to just declare a plugin and running with it. Specs can be a little more involved, and i'm also a little disappointed that vim-awesome does not show lazy specs for plugins listed on their site. Then again, I haven't actually written the spec yet. Maybe it's easier than it looks.
```lua
return {
	{
		"vim-airline/vim-airline",
		lazy = false, -- needs to be available at start, no lazy
	}
}
```
And hey! Looks like that's all you need! We can see that the status line has changed to vim-airline in this screenshot:
![Pasted image 20250226122249.png](/attachments/Pasted%20image%2020250226122249.png)
That window that opened is the Lazy manager window, whenever you need to manage plugins on the fly you use this window. By default, this opens every time you install a new plugin. If you need to access this while in neovim, you simply run `:Lazy`. 
### vim-gitgutter
Damn! I way underestimated how hard it would be to pick out plugins, because they're all so good. I'm trying not to overload myself to start, and to keep the number of plugins as small as possible (since more plugins $\approx slower editor). Let's play it safe with gitgutter, which will show changes in the gutter of neovim (far left side of the window).
Here's the spec:
```lua
return {
	{
		"airblade/vim-gitgutter",
		lazy = false, -- needs to be available at start, no lazy
	}
}
```
![Pasted image 20250227205103.png](/attachments/Pasted%20image%2020250227205103.png)
See those `+`'s on the left side of the screen? That's gitgutter! It just marks lines that are different from the previous commit.

### NERDTree
Now this one's pretty neat, and it's going to be the first plugin that will be lazy loaded. NERDTree is a file explorer that runs inside neovim. I'll also be installing some plugins for NERDTree, mainly nerdtree-git-plugin & vim-devicons.
![Pasted image 20250305210629.png](/attachments/Pasted%20image%2020250305210629.png)
Here's the spec for NERDTree:
```lua
return {
    {
        "preservim/nerdtree",
        cmd = { "NERDTreeToggle", "NERDTreeFind" },
        keys = {
          { "<leader>n", ":NERDTreeToggle<CR>", desc = "Toggle NERDTree" },
          { "<leader>f", ":NERDTreeFind<CR>", desc = "Find file in NERDTree" },
        },
        dependencies = {
          "Xuyuanp/nerdtree-git-plugin", 
        },
        config = function()
          vim.g.NERDTreeShowHidden = 1 -- Show hidden files
          vim.g.NERDTreeMinimalUI = 1  -- Simplify UI
          vim.g.NERDTreeDirArrows = 1  -- Enable arrows for directories
        end,
    }
}
```
And the spec for vim-devicons:
```lua
return {
	{
		"ryanoasis/vim-devicons"
	}
}
```

### NERD Commenter
***
The NERD Tools are really good, you kinda can't go wrong with one. This tool makes commenting almost as easy as it would be in VSCode (with Ctrl+/). Simply select test in visual mode, or leave your cursor on a line to be commented, then run any of these commands:
- `[count]<leader>cc` **|NERDCommenterComment|**
	- Comment out the current line or text selected in visual mode.
- `[count]<leader>cn` **|NERDCommenterNested|**
	- Same as cc but forces nesting.
- `[count]<leader>c<space>` **|NERDCommenterToggle|**
	- Toggles the comment state of the selected line(s). If the topmost selected line is commented, all selected lines are uncommented and vice versa.
- `[count]<leader>cm` **|NERDCommenterMinimal|**
	- Comments the given lines using only one set of multipart delimiters.
- `[count]<leader>ci` **|NERDCommenterInvert|**
	- Toggles the comment state of the selected line(s) individually.
- `[count]<leader>cs` **|NERDCommenterSexy|**
	- Comments out the selected lines with a pretty block formatted layout.
- `[count]<leader>cy` **|NERDCommenterYank|**
	- Same as cc except that the commented line(s) are yanked first.
- `<leader>c$` **|NERDCommenterToEOL|**
	- Comments the current line from the cursor to the end of line.
- `<leader>cA` **|NERDCommenterAppend|**
	- Adds comment delimiters to the end of line and goes into insert mode between them.
- `<leader>ca` **|NERDCommenterAltDelims|**
	- Switches to the alternative set of delimiters.
- `[count]<leader>cl` **|NERDCommenterAlignLeft** `[count]<leader>cb` **|NERDCommenterAlignBoth**
	- Same as **|NERDCommenterComment|** except that the delimiters are aligned down the left side (`<leader>cl`) or both sides (`<leader>cb`).
- `[count]<leader>cu` **|NERDCommenterUncomment|**
	- Uncomments the selected line(s).
Here's the spec:
```lua
return {
	{"scrooloose/nerdcommenter"}
}
```

### Syntastic
***
Syntastic is a syntax checking plugin for vim. Here's the spec:
```lua
return {
  "vim-syntastic/syntastic",
  lazy = false, -- Ensure it loads on startup
  config = function()
    -- Example configuration
    vim.g.syntastic_always_populate_loc_list = 1
    vim.g.syntastic_auto_loc_list = 1
    vim.g.syntastic_check_on_open = 1
    vim.g.syntastic_check_on_wq = 0
  end,
}
```
Syntastic comes with *almost* every checker you might need, but for the ones that aren't you'll need to install the checker yourself. Check the syntastic page for information.

I Purposefully broke this spec to see if it detected bad syntax. And it does!
![Pasted image 20250305211905.png](/attachments/Pasted%20image%2020250305211905.png)
But only when you save the file. You can always run `:SyntasticCheck`, but why not save the file? It might reinforce some good behavior.

### Conclusion
***
Okay, I have **GOT** to stop with it. I kept looking at every plugin and vexing over whether it would actually get used or not, or if I was going to end up adding too many plugins. This is a pretty good start point, though, and I can always change stuff later. Because of how Lazy handles plugins modularly, it's easy to just edit the spec of any plugin I want since they are all separated.