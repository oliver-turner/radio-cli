# radio-cli v1.0.0

A very simple terminal radio player for Windows and now Linux !

I wanted to have a variety of different radio stations available for me to tune into and listen while I do some work.

Please let me know what you think, and most importantly, where I can improve, as well as new features you would like !

Thank you for checking out my fun project

---

## Requirements

**All platforms**

- [Git](https://git-scm.com/)

**Windows**

- Windows 10 or 11
- Audio playback uses the Windows Runtime (WinRT) — no extra install needed

**Linux**

- `mpv`, for audio playback:

```bash
  sudo apt install mpv      # Debian/Ubuntu
  sudo dnf install mpv      # Fedora
  sudo pacman -S mpv        # Arch
```

---

## Installation

Open your terminal and run these three commands.

**Windows**

```powershell
git clone https://github.com/oliver-turner/radio-cli.git
cd radio-cli
.\setup.ps1
```

**Linux**

```bash
git clone https://github.com/oliver-turner/radio-cli.git
cd radio-cli
chmod +x setup.sh launch.sh
./setup.sh
```

`setup.ps1` / `setup.sh` will:

1. Install `uv` if it isn't already on your system
2. Create an isolated Python environment
3. Install all dependencies from the locked, hash-verified `uv.lock` file — if the lockfile doesn't match what's expected, setup stops and tells you rather than installing something unverified

---

## Running

**Windows**

```powershell
.\launch.ps1
```

**Linux**

```bash
./launch.sh
```

**Optional — add a global `radio` command**

If you want to type `radio` from anywhere in any terminal, add this to your profile. Open:

- `notepad $PROFILE` in PowerShell (Windows)
- `nano ~/.bashrc` in your terminal (Linux)

Windows (PowerShell):

```powershell
function radio {
    & "C:\path\to\radio-cli\launch.ps1"
}
```

Linux (bash/zsh):

```bash
radio() {
    ~/path/to/radio-cli/launch.sh
}
```

---

## Future Features

Currently it is a hardcoded list of stations I like. While I develop this project, I will try and add more features such as:

- An about section in the program [i will do this next :)]
- Adding and removing stations
- Updating the stations info
- Having the info shown in the windows media tray (windows key + a)
- Shazam song recognition (?)
- Spotify connection to automatically add songs you like to your liked songs
