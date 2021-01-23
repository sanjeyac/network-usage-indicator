# Network Usage  Indicator

A network app indicator, based on GTK3 Appindicator3, which is mainly a wrapper for vnstat on linux.

![Demo Image](docs/demo.png)

# Usage
These dependencies are needed to proceed:
- python3
- python3/GTK3 dependencies
- vnstat

Step 1)
Install vnstat on your linux distro, usually vnstat is already available on the package manager

(Ubuntu: ```sudo apt install python3 python3-gi vnstat``` )

Step 2)
Download this repository somewhere which could be accessible for launcing it at login

(```git clone https://github.com/sanjeyac/network-usage-indicator.git``` or download it as zip from the browser)

Step 3)
Add this command to the list of startup applications  
```python3 <path to folder>/network-usage-indicator.py```

( Ubuntu: type "startup" on the menu > click on add button > add the above command as "Command" and logout and login to see if it works.)

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
