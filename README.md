Getting Tweet API with Tweepy: Twitter for Python!
======

[![Build Status](http://img.shields.io/travis/tweepy/tweepy/master.svg?style=flat)](https://travis-ci.org/tweepy/tweepy)
[![Documentation Status](http://img.shields.io/badge/docs-v3.6.0-brightgreen.svg?style=flat)](http://docs.tweepy.org)
[![Version](http://img.shields.io/pypi/v/tweepy.svg?style=flat)](https://crate.io/packages/tweepy)

Feature
------------
- When you implement this source code, you can get a CSV file that well organized by type.
![Csv](/assets/User_csv.png?raw=true "Optional Title")
- If you run more this code, new file will be added to CSV.
- You can input 'Username', 'HashTag' on cmd to find the info.
- You can see the result at the cmd also.

Installation
------------
The easiest way to install the latest version
is by using pip/install to pull it from PyPI:

    pip install tweepy

TestCode

    pip install -U pytest

Running
------------

if you want to get the Tweet searched by Hashtags,

    cd GetHash
    python3 "Hash".py

elif : you want to get the Tweet searched by Username,  

    cd GetUser
    python3 "User".py

![Cmd](/assets/User_cmd.png?raw=true "Optional Title")

elif : you want to test,

    cd test
    pytest.Tweet_test.py

![Error_Connection Screen Shot](/assets/Test.png?raw=true "Optional Title")

Something that was difficult
---------
- Connection Refused Problem : 

![Error_Connection Screen Shot](/assets/ConnectionError.png?raw=true "Optional Title")

When I started this project, I just noticed that my labtop couldn't connect [Twitter](https://twitter.com/).
Because I didn't use Twitter before, I didn't know what the problem was.
From the beginning, I should have met difficulty, Connection error.(Ex.ScreenShot)

I tried a lot of times to implement the code, but it showed same errors.
Although I searched all related info on the stackoverflow, google and github, no solution was found out at all. 

Fortunately, I happened to know how to access to Twitter from one of my Korean Friend(not a developer). 
He said, "Use the [VPN](https://kor.windscribe.com/). Router machine in Vietnam is preventing people from accessing to certain URLs.".
Thanks to his opinion, finally I could solve this problem.

- Getting the Reply_Count : 

Tweepy API doesn't have Reply_Count Object. so, I imported Twitter Api. But it still showed that this object was only available with the Premium and Enterprise tier products.

- Getting the HashTag : 

I tried to get the hashtags in entities object(Ex: entities.get('hashtags', entities.gethashtags[0][1][1] or entities.hashtags.text etc....), but It didn't access the hashtags:{"text"}.

Impressive things(During Project)
------------
Firstly, I really appreciate AnyMind Group for giving me the opportunity and interesting project.

I made it by Python, so I could review all from the basic of Python.
In addition, it's my first time using the CSV file.

Through this project, I've learnded new things more.
At the first problem(Connection Refuse), it tooks quite a long time to fix,
but it didn't work, that made me so sad.

After solving the problem out, I leared listening to other people's opinions 
even who is not a developer.

Sometimes, I couldn't call the some certain object which is API of tweepy,
I read the all of Docs and I could deeply understand about other properties of that API.

Lastly, I'd like to say again :

" Thank you very much for giving me this Awesome Project and 
it will be very glad if we work together!"

From. Sean.Kim;


Reference
---------
- [Tweepy Object](https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2)
- [Twitter Object](https://dev.twitter.com/overview/api/tweets?lang=en)
- [pytest](https://docs.pytest.org/en/latest/)
- [CSV](https://docs.python.org/3/library/csv.html)