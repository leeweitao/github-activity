# github-activity
This project was made according to the instructions on roadmap.sh. Roadmap.sh has roadmaps for many different roles in the tech industry. This project is one of their recommended projects to showcase on your portfolio.

More project recommendations on the website: (https://roadmap.sh/projects/github-user-activity)

##  Installation

1. Go to the correct project root and activate a virtual environment:

   ```
   python -m venv .venv        # Step 1: Create a virtual environment
   .venv\Scripts\activate      # Step 2: Activate it (Windows)
   ```

2. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Open terminal in the correct folder
   ```bash
   cd D:\Programming\Documents\github-activity
   ```
4. Install your CLI tool

   ```bash
   pip install -e
   ```

<br>

## How to use it

To query the recent activity of a GitHub user, run the following command:

   ```bash

   github-activity <username>    # Example: github-activity leeweitao

   ```
You can choose to run specific commands to display the desired events: 
    
    - `push`: Commits pushed.
    - `watch`: Starred repositories.
    - `issue`: Issues created.
    
  Example: If you want to display only the commits pushed by the user, use: 
   ```
   github-activity leeweitao --type push
   ```
