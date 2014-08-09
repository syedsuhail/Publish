publish
=======

Publish is a program to broadcast an announcement on multiple social media channels (like twitter, facebook, email, etc)

This particular program comes really handy.
With the help of this program you'll be able to post messages on multiple channels with ease.


To setup the application :

$ virtualenv publish

$ . publish/bin/activate

pip install tweepy

And to sent out messages : 

python publish.py --twitter --facebook -m "Hello World"

or

python publish.py -t -fb -m "Hello World"