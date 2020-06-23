import facebook
import requests

class FacebookFeed:

    TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
    params = dict(self.client_id, self.client_secret, 
                  grant_type='client_credentials')

    def __init__(self, auth_key, client_secret):
        self.client_id = auth_key
        self.client_secret = client_secret

    def get_posts(self, user, count=1):
        try:
            token_response = requests.get(url=cls.token_url, params=cls.params)
            access_token = token_response.text.split('=')[1]
            graph = facebook.GraphAPI(access_token)
            profile = graph.get_object(user)
            query_string = 'posts?limit={0}'.format(count)
            posts = graph.get_connections(profile['id'], query_string)
            return posts
        except facebook.GraphAPIError:
            return None