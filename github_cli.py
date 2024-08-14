import argparse
from github_api import get_github_user_events
from github_events import EVENT_TYPE_DESCRIPTIONS

def main():
    # set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Retrieve GitHub user activity.")

    # add an argument for the GitHub username
    parser.add_argument('username', type=str, help="GitHub username to retrieve activity for")

    # parse the arguments
    args = parser.parse_args()

    # get the github user events
    events = get_github_user_events(args.username)

    if events:
        print(f"Recent activity for GitHub user: {args.username}")
        for event in events:
            event_type = event['type']
            description = EVENT_TYPE_DESCRIPTIONS.get(event_type, event_type)
            repo_url = event.get('repo', {}).get('url', 'No repository URL')
            print(f"Event: {description}, Date: {event['created_at']}, Repository: {repo_url}")
    else:
        print(f"Could not retrieve events for user {args.username}.")
if __name__== "__main__":
    main()
