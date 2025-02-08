# GitHub Activity CLI

A simple command-line tool written in Python to fetch and display a GitHub user's recent activity using the GitHub API.

## Features

- Fetches recent activity for a specified GitHub user.
- Displays activity in a human-readable format in the terminal.
- Handles errors gracefully (e.g., invalid usernames or API failures).
- Uses only Python's built-in modules (no external libraries required).

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/jupelaz/github-activity
   cd github-activity
   ```

2. **Make the script executable**:
   ```bash
   chmod +x github_activity.py
   ```

3. **Run the script**:
   ```bash
   ./github_activity.py <username>
   ```

## Usage

Run the script from the command line by providing a GitHub username as an argument:

```bash
./github_activity.py <username>
```

### Example

```bash
./github_activity.py kamranahmedse
```

### Output

The script will display the user's recent activity in the terminal. For example:

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## How It Works

1. The script uses the GitHub API endpoint `https://api.github.com/users/<username>/events` to fetch the user's recent activity.
2. It parses the JSON response and extracts relevant information based on event types (e.g., `PushEvent`, `IssuesEvent`, `WatchEvent`).
3. The activity is displayed in a readable format in the terminal.

## Error Handling

- If the provided username is invalid or the API request fails, the script will display an error message and exit gracefully.

## Dependencies

This script uses only Python's built-in modules:
- `sys` for command-line arguments.
- `urllib.request` for making HTTP requests.
- `json` for parsing the API response.

No external libraries are required.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to contribute, report issues, or suggest improvements!
