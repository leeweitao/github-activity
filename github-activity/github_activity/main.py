import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]

    print(f"Fetching activity for: {username}")

    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data.")
        sys.exit(1)

    events = response.json()

    if not events:
        print("No recent activity.")
        sys.exit(0)

    for event in events[:10]:
        etype = event["type"]
        repo = event["repo"]["name"]

        if etype == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            print(f"Pushed {len(commits)} commits to {repo}")
        elif etype == "IssuesEvent":
            action = event.get("payload", {}).get("action", "updated")
            print(f"{action} an issue in {repo}")
        elif etype == "WatchEvent":
            print(f"Starred {repo}")
        else:
            print(f"{etype} in {repo}")

if __name__ == "__main__":
    main()