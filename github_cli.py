import argparse
from github_api import get_github_user_events

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
        if events:
            print(f"Recent activity for GitHub user: {args.username}")
            for event in events:
                print(f"Event: {event['type']}, Date: {event['created_at']}")
        else:
            print(f"No events found for user {args.username}.")
    else:
        print(f"Could not retrieve events for user [args.username].")
if __name__== "__main__":
    main()
