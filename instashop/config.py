__author__ = 'dilaver'
from authomatic.providers import oauth2, oauth1

CONFIG = {

    'tw': {  # Your internal provider name

             # Provider class
             'class_': oauth1.Twitter,

             # Twitter is an AuthorizationProvider so we need to set several other properties too:
             'consumer_key': 'wyQdNPSjSRKBjesg1jeQ1AstO',
             'consumer_secret': 'IkHLekktm5qjwBTs5aJEKeSb4qKmdKqa7bseBv83CCTc0swbnJ',
             },

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '625600450873825',
        'consumer_secret': '5a5cea3b1c92e813514ce1a3aa432d45',

        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
}
