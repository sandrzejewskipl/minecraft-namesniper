# Minecraft NameSniper

Based on [cardbooard/Minecraft-NameSniper-Blocker](https://github.com/cardbooard/Minecraft-NameSniper-Blocker), but most of the code was reworked for the new API. I also removed unnecessary code.

# Dependencies
- Python3
- requests module in python (pip install requests)

# Usage

After running script type in a few data from below.

### Target

Targeted username.

### Bearer key

Login into to your account on minecraft.net, than click CTRL+SHIFT+I, go to Application tab, click on Cookies, find "bearer_token" - click on it and you will see a long value at the bottom - that's the bearer key!
Remember that bearer key resets every 2 hours. Additionally you need to answer security questions on minecraft.net.

#### Time of Availability

Use namemc.com to figure when a name will drop (example 18:19:06).

#### Delay after release time
Delay after release time (e.g. 0.005 = 0.005 second). For example, if u want to send request 0.7 seconds before release time, set release time to 1 second earlier and set delay to 0.3 seconds.

## IMPORTANT
If the begin button does not appear after pressing the Insert Info button, check the console. After clicking Begin check console for any output after the program tries to get a targeted nickname.
