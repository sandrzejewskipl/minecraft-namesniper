# Minecraft NameSniper

Based on [cardbooard/Minecraft-NameSniper-Blocker](https://github.com/cardbooard/Minecraft-NameSniper-Blocker), but most of the code was reworked for the new API. I also removed unnecessary code.

# Dependencies
- Python3
- requests module in python (pip install requests)

# Usage

After running program type in a few data from below.

### Target

Targeted username.

### Bearer key

Login into to your account on minecraft.net, than click CTRL+SHIFT+I, go to Application tab, click on Cookies, find "bearer_token" - click on it and you will see a long value at the bottom - that's the bearer key!

#### Time of Availability

Use namemc.com to figure when a name will drop (example 18:19:06).

#### Run Before Release Time
Here you can enter when the program is to start before the nickname's availability time. (for example ping to api.minecraftservices.com, if your ping is 30 then type 0.030).
