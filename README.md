python-logging-twitter
======================

#Description
Python-logging-twitter is a handler that helps you to post your logging messages in Twitter. It can be used through the Python logging library.

It makes use of the python-twitter library:

> https://github.com/bear/python-twitter


#Features
- Compatible with Python logging system.
- Compatible with Django.
- Post log messages as private direct messages to a Twitter specified user.
- Post log messages into the timeline.
- Add geolocation to your posts (only available in timeline posts). 
- Add media files to your posts (only available in timeline posts).
- Tested succesfully with unicode messages.


#Authors
- Marcos Villares


#License
Open source licensed under the GPLv3 license (see LICENSE file for details).


#Installation
To install this handler, just execute:
> pip install python-logging-twitter

To use this handler you will need to create your own Twitter app before in the next web page: 
>  https://apps.twitter.com/

You need to get the consumer key, consumer secret, access token key and access token secret values from this page. 


#Usage
###Using it in Python
    #!/usr/bin/env python
    import logging
    from logging_twitter.handler import TwitterHandler

    # Set required twitter parameters
    # Get them in your Twitter developer page
    CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxx'
    CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'
    ACCESS_TOKEN_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
    ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxx'

    # User variable: Direct message to the user if 
    # it is defined. Set to None if you with to publish  
    # to your timeline
    USER = None
    #USER = 'twitterscreenname'

    # Create logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("logging_twitter")

    # Add Twitter logging handler
    handler = TwitterHandler(consumer_key=CONSUMER_KEY,
               consumer_secret=CONSUMER_SECRET,
               access_token_key=ACCESS_TOKEN_KEY,
               access_token_secret=ACCESS_TOKEN_SECRET,
               direct_message_user=USER)
    logger.addHandler(handler)

    # Log a message
    dextra = {
        'latitude': '1',
        'longitude': '3',
        'media': '/tmp/opensource.jpg'
    }
    logger.info('Testing message', extra=dextra)


###Using it in Django
Add to your settings.py the handle:

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'twitter': {
                'level': 'INFO',
                'class': 'logging_twitter.TwitterHandler',
                'consumer_key': 'xxxxxxxxxxxxxxxxxx',
                'consumer_secret': 'xxxxxxxxxxxxxxxxxx',
                'access_token_key': 'xxxx-xxxxxxxxxxxx',
                'access_token_secret': 'xxxxxxxxxxxxxxx',
                'direct_message_user': 'screenname',
            },
        },
        'loggers': {
            'twitter': {
                'handlers': ['twitter'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

Finally, use it in your views:

    from django.http import HttpResponse
    import logging

    logger = logging.getLogger('twitter')

    def index(request):
        logger.info('Posting message...')
        return HttpResponse("Success")
