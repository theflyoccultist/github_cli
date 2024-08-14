import http.client
import json

def get_github_user_events(username):
    try:
        # Establish a connection to the github API
        conn = http.client.HTTPSConnection("api.github.com")

        # user agent header required by GitHub
        headers = {
            'User-Agent': 'Python CLI',
        }

        #GET request to the user events endpoint
        conn.request("GET", f"/users/{username}/events", headers=headers)

        # get the response
        response = conn.getresponse()

        if response.status == 200:
            # read and decode the response
            data = response.read().decode('utf-8')

            # parse the json data
            events = json.loads(data)

            # return the parsed events
            return events
        elif response.status == 404:
            print(f"Error: User '{username}' not found.")
            return None
        elif response.status == 403:
            print(f"Error: Rate limit exceeded. Please try again later.")
            return None
        else:
            print(f"Error: Recieved status code {response.status}")
            return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None