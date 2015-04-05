#!/usr/bin/env python
import logging
from datetime import datetime
from logging_twitter.handler import TwitterHandler


# Set required twitter parameters
# Get them in your Twitter developer page
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_KEY = 'xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# User variable: Direct message to the user if it is defined.
# Set to None if you with to publish to your timeline
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
dtnow = datetime.now().strftime('%Y-%m-%d %H:%M%S')
dextra = {'latitude': '1', 'longitude': '3', 'media': '/tmp/opensource.jpg'}
logger.info('[%s] Testing django-logging-twitter' % (dtnow), extra=dextra)
