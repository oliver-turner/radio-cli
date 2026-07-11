#!/usr/bin/env bash
set -euo pipefail

echo ""
echo -e "\033[36mSetting up radio-cli...\033[0m"

if ! command -v uv >/dev/null 2>&1; then
    echo ""
    echo -e "\033[33muv not found. Installing from official Astral source...\033[0m"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

if ! command -v mpv >/dev/null 2>&1; then
    echo ""
    echo -e "\033[33mmpv not found — required for audio playback on this platform.\033[0m"
    echo "Install it with your package manager, then re-run this script:"
    echo "  Debian/Ubuntu: sudo apt install mpv"
    echo "  Fedora:        sudo dnf install mpv"
    echo "  Arch:          sudo pacman -S mpv"
    echo "  macOS:         brew install mpv"
    exit 1
fi

echo ""
echo -e "\033[33mSyncing dependencies from uv.lock (hash-verified)...\033[0m"
if ! uv sync --frozen; then
    echo ""
    echo -e "\033[31mERROR: uv sync failed. Lockfile may be out of date or tampered with.\033[0m"
    echo -e "\033[33mIf you intentionally changed pyproject.toml, run: uv lock\033[0m"
    exit 1
fi

echo ""
echo -e "\033[32mDone! All dependencies installed from verified hashes.\033[0m"
echo -e "\033[32mTo run the app, use:\033[0m"
echo "  ./launch.sh"
echo ""
