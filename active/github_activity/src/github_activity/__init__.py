# I want to build a CLI app that can return the public events of a user on GitHub
# I will use the GitHub API to get the public events of a user
# I will use the requests library to make the API call
# I will use the json library to parse the response
# I will use the pprint library to print the response
# I will use the argparse library to parse the command line arguments
# I will use the sys library to exit the program if there is an error

# %%
import requests
import argparse
import sys


# %%
def get_public_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to get public events for {username}")
    else:
        event = response.json()
        latest_events = event
        print(f"Latest events for {username}:")
        for event in latest_events:
            # Covering only the most common events
            if event["type"] == "IssueCommentEvent":
                print(f"-  commented on issue {event['payload']['issue']['number']}")
            elif event["type"] == "PushEvent":
                print(f"-  pushed to {event['repo']['name']}")
            elif event["type"] == "IssuesEvent":
                print(f"-  created issue {event['payload']['issue']['number']}")
            elif event["type"] == "WatchEvent":
                print(f"-  starred {event['repo']['name']}")
            elif event["type"] == "PullRequestEvent":
                print(
                    f"-  created pull request {event['payload']['pull_request']['number']}"
                )
            elif event["type"] == "PullRequestReviewEvent":
                print(
                    f"-  reviewed pull request {event['payload']['pull_request']['number']}"
                )
            elif event["type"] == "PullRequestReviewCommentEvent":
                print(
                    f"-  commented on pull request {event['payload']['pull_request']['number']}"
                )
            elif event["type"] == "CreateEvent":
                print(
                    f"-  created {event['payload']['ref_type']} {event['payload']['ref']}"
                )
            else:
                print(f"-  {event['type']}")


# %%
def main():
    parser = argparse.ArgumentParser(
        description="Get the public events of a user on GitHub"
    )
    parser.add_argument(
        "username",
        type=str,
        help="The username of the user to get the public events of",
    )
    args = parser.parse_args()

    try:
        public_events = get_public_events(args.username)
        print(public_events)
    except Exception as e:
        print(e)
        sys.exit(1)


# %%
if __name__ == "__main__":
    main()

# %%
