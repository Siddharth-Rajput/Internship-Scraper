# Internship Scapper 
[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)]
[![MIT License](https://img.shields.io/github/license/Siddharth-Rajput/insternship-scraper)](https://github.com/Siddharth-Rajput/insternship-scraper/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/Siddharth-Rajput/insternship-scraper)](https://github.com/Siddharth-Rajput/insternship-scraper/issues)


As all of you know its the internship season and the most popular place to find it is internshala.com. One fin day an idea came into my mind that why should we visit the site again and again instead we can scape our preferred(favourite) intership with python and that day this tool was born. Enough of this story telling lets get into the details.

## What it basically does

This tool just sits on you desktop and when clicked fetches all you preffered internship from this page https://internshala.com/internships/matching-preferences. And displayes it in a plain terminal window with poppy text colors.
**It also highlights the keywords that you what in internship name.**

### Prerequisites

Python 2 any will do the work.

```
The Packages that we need are:
* Lxml
* Beautifullsoap
* Colorama
* Requests
```

### Installing

```
1. git clone https://github.com/Siddharth-Rajput/insternship-scraper
2. python -m pip install requirement.txt
3. Now configure the code according your use.
```

## Configuration

This is divided into two part setting up the cookies and the keywords in the script

### Setting the cookies:

1. Login into you internshala account and go to this page: https://internshala.com/internships/matching-preferences
2. Open the debugger menu of our browser and look for network tab.
3. Hit refresh to capture the request.
4. Look for the first request and copy the cookies header and paste in cookies.txt
(**this because we are skiping the login step so that the tool runs in its max speed😎**)
5. You can tweak the code according to you need its a simple one.

![alt text](https://github.com/Siddharth-Rajput/insternship-scraper/blob/master/assets/cookieheader.gif)

### Setting up the KeyWords.

This will help to see you favourite internships in red. Like '**IOS**' then the tool will search IOS in the internship name and highligt it in RED. To Set your keywords just type it in **keywords.txt** one word in one line.

![alt text](https://github.com/Siddharth-Rajput/insternship-scraper/blob/master/assets/keywords.jpg)

### How to run the tool
#### Just click on the main.py and sit back and enjoy all your favorite internship in terminal.
*Suggestion: Just create a desktop shortcut of main.py for instant use.*

![alt text](https://github.com/Siddharth-Rajput/insternship-scraper/blob/master/assets/demogif.gif)

## Authors

* **Siddharth Rajput** - (https://github.com/Siddharth-Rajput)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Inspiration
* etc
