# Sine
![GitHub Repo stars](https://img.shields.io/github/stars/srcworks-software/Sine?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/srcworks-software/Sine?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/srcworks-software/Sine?style=for-the-badge)

A complex calculator app with graphing and scientific features.

# Setup
The installation process for Sine.
## Step 1: Install package
In your terminal, run
```
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip python3-gi python3-dev libgirepository1.0-dev libcairo2-dev gir1.2-gtk-3.0 build-essential pkg-config git
pip install sine-calc --break-system-packages
```
This will install the base package. From here, you can run
```
sine-calc
```
However, you will need to proceed with the following steps in order to launch Sine from your desktop environment.
## Step 2:
In your terminal, run
```
git clone https://github.com/srcworks-software/Sine
cd Sine/src
chmod +x setup.sh
sudo ./setup.sh
```
This will install the necessary `.desktop` file to run Sine from your desktop environment.