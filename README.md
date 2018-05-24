# :grinning: Welcome to tweeLights!

Each year, in living rooms and home-goods stores across the country the same battle unfolds: White or multi-colored lights? The battles are contentious with husbands and wives, neighbors and colleagues pitted against each other and searching for compromise.

In addition, this issue becomes bigger when major stores like Amazon, want to attract their customers during holidays. The choice of light colors may affect the customer's decision to visit or not to visit the store!

In order to solve this issue, and to have some fun, we decided to implement a system that controls the holiday lights' color by analyzing the social feeds and posts on twitter. Scroll down to learn how this project works!

## Installation

### :wrench: What will you need?
- Raspberry pi 3 or 2
- Bread Board
- Jumper Cables
- 3 LED of different colors (Yellow, Green, and Red)
- Computer to code 😸 



### :dizzy_face: How to configure it?
First, before we continue, you should have Raspberry Pi 3 Model B/B+ or a Raspberry Pi 2.

1. Get a micro SD card of at least 8GB.
1. Download the Raspbian image from the raspberry pi’s website and copy its content to the SD card.
1. Insert the SD card within the raspberry pi 3.
1. Connect the HDMI cable of your raspberry pi 3 to any suitable screen.
1. Power the raspberry pi by plugging in the USB cable.
1. Follow the steps to install the Raspbian system.
1. Once the installation is done, connect to the internet through wifi or ethernet.
1. Download the tweeLights.py python script on your raspberry pi 3.
1. Insert the credentials of your twitter account through a txt file and name it “config.txt” and place within the same directory of tweeLights.py 

```Python
consumer_key: [your key]
consumer_secret: [your secret]
access_token: [your access token]
access_token_secret: [your access token secret]
```

1. Install tweepy by `pip install tweepy`
1. Run the Python script `python tweeLights.py` after having the LEDs connected as mentioned the section below.
1. The system will be working now

### 🚀Raspberry Pi and LED connections

![](https://github.com/yasserkabbout/tweeLights/blob/master/images/gpio-numbers-pi2.png?raw=true)

The pins used in this project are the Ground pin, GPIO 14, GPIO 15, and GPIO 18.

- GPIO 14 → Yellow LED
- GPIO 15 → Green LED
- GPIO 18 → Red LED
- The anode part of the LED will be connected to the ground pin.


## :mortar_board: Read More!

:question: **[1. Project Description](https://github.com/yasserkabbout/tweeLights/wiki/1.-Project-Description)**

:bar_chart: **[2. Project Requirements](https://github.com/yasserkabbout/tweeLights/wiki/2.-Project-Requirements-RSD)**

:art: **[3. System Design](https://github.com/yasserkabbout/tweeLights/wiki/3.-System-Design-Sketches)**

:dart: **[4. Project Plan](https://github.com/yasserkabbout/tweeLights/wiki/4.-Project-Plan)**

:moneybag: **[5. Project Market Analysis](https://github.com/yasserkabbout/tweeLights/wiki/5.-Project-Market-Analysis)**

:rocket: **[6. Project Complexity Analysis](https://github.com/yasserkabbout/tweeLights/wiki/6.-Project-Complexity-Analysis)**

:surfer: **[7. Team SWOT Analysis](https://github.com/yasserkabbout/tweeLights/wiki/7.-Project's-Team-SWOT-Analysis)**

:computer: **[We are live! Click here](http://tweelights.yasserkabbout.com/)**

 📑 **[ 8. Git Cheat Sheet](https://github.com/yasserkabbout/tweeLights/blob/master/images/github-git-cheat-sheet.pdf)**


## :ok_hand: Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## :hearts: Credits

Credit goes to Yasser El Kabbout & Professor Dr. Suzan Üsküdarlı from Bogaziçi University.

## :innocent: License

Nah! Don't worry about this :D feel free to use and edit the software.
