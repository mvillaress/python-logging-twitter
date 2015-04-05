#!/usr/bin/env python
"""
Copyright (C) 2015  Marcos Villares

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from twitter import Api


class TwitterHandler(logging.Handler):

    """ Twitter logging handler """

    def __init__(self, consumer_key=None, consumer_secret=None,
                 access_token_key=None, access_token_secret=None,
                 direct_message_user=None):
        """ Constructor of the handler. It defines a twitter connection
            Parameters:
                consumer_key: Obtainable from Twitter developer page
                consumer_secret: Obtainable from Twitter developer page
                access_token_key: Obtainable from Twitter developer page
                access_token_secret: Obtainable from Twitter developer page
                direct_message_user: Receiver username. If None the message
                    will be published in the timeline
        """
        logging.Handler.__init__(self)
        if (consumer_key and consumer_secret and
                access_token_key and access_token_secret):
            self.twitter_api = Api(consumer_key=consumer_key,
                                   consumer_secret=consumer_secret,
                                   access_token_key=access_token_key,
                                   access_token_secret=access_token_secret)
        else:
            self.twitter_api = None
        self.direct_message_user = direct_message_user

    def emit(self, record):
        """ Post log message to Twitter """
        try:
            if self.twitter_api:
                # Prepare message
                message = self.format(record)

                # Get coordinates if they are specified
                try:
                    latitude = record.latitude
                    longitude = record.longitude
                    display_coordinates = True
                except:
                    latitude = None
                    longitude = None
                    display_coordinates = False

                # Get media parameter
                try:
                    media = record.media
                except:
                    media = None
                print latitude, longitude, media
                # Send direct message to the user if it is specified
                # Otherwise post a message to the twitter timeline
                if message:
                    if self.direct_message_user:
                        status = self.twitter_api.PostDirectMessage(
                            message, screen_name=self.direct_message_user)
                    elif media:
                        status = self.twitter_api.PostMedia(
                            message, media=media, latitude=latitude,
                            longitude=longitude)
                    else:
                        status = self.twitter_api.PostUpdate(
                            message, latitude=latitude, longitude=longitude)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
