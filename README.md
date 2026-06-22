# radio-cli

A very simple terminal radio player for Windows.

I wanted to have a variety of different radio stations available for me to tune into and listen while I do some work. 

Please let me know what you think, and most importantly, where I can improve, as well as new features you would like !

Thank you for checking out my fun project

> **Windows only** — the audio backend uses the Windows Runtime (WinRT) and won't run on Mac or Linux.

---

## Requirements

- Windows 10 or 11
- [Git](https://git-scm.com/)

---

## Installation

Open PowerShell and run these three commands

```powershell
git clone https://github.com/oliver-turner/radio-cli.git
cd radio-cli
.\setup.ps1
```

`setup.ps1` will install uv, create a isolated Python environment and install all dependencies from the locked, hash-verified uv.lock file

---

## Running

```powershell
.\launch.ps1
```

**Optional — add a global `radio` command**

If you want to type `radio` from anywhere in any terminal, add this to your PowerShell profile:

```powershell
function radio {
    & "C:\path\to\radio-cli\launch.ps1"
}
```

Replace `C:\path\to\radio-cli` with wherever you cloned the repo. To open your profile for editing, run `notepad $PROFILE` in PowerShell.

---

## Usage

Once the app starts you'll see a menu:

```
~
Menu
Now playing: No station is playing
1. Play
2. View Saved Stations
~
Enter q to exit or enter kobe
```

| Input | Action |
|-------|--------|
| `1` | Choose and play a station |
| `2` | List all saved stations |
| `q` | Quit |
| `kobe` | 👀 |

---

## Future Features
Currently it is a hardcoded list of stations I like. While I develop this project, I will try and add more features such as:
- An about section in the program [i will do this next :)]
- Adding and removing stations
- Updating the stations info
- Having the info shown in the windows media tray (windows key + a)
- Shazam song recognition (?)
- Spotify connection to automatically add songs you like to your liked songs
