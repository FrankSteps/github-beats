# Github Beats 

This project updates your **GitHub status** with the title of the **YouTube** video you are watching or listening. **If you listen to music on YouTube, this project is for you!**


## Tree

```
. 
├── extension           # Browser extension files
│   ├── content.js      # Script running on webpages
│   └── manifest.json   # Extension settings
├── logs                # Server log files
│   └── server.log
├── server              # Python server files
│   ├── server.py
│   └── start.sh
├── LICENSE      
└── README.md       

``` 


## Dependences
- Python3
- Flask             – Python web server
- Flask-CORS        – Allows the browser extension to communicate with the server
- requests          – For sending HTTP requests to the GitHub API
- python-dotenv     – Loads environment variables from .env



## Features

- Identify YouTube video tittle
- Updates your GitHub status with the title or YouTube video


## How to use this project

```
# Clone this repository
git clone https://www.github.com/FrankSteps/github-beats


# install the dependences
pip install flask requests python-dotenv flask-cors


# Go to the project folder
cd github-beats


# Create a .env file and add your GitHub token
touch .env 
echo "GITHUB_TOKEN=ghp_..." >> .env


# Start the server
./server/start.sh


# Load the "manifest.json" file in your browser as an extension

# Notes:
# 1. This project uses port 8080: Ensure that no other program is using the same port
# 2. Press Ctrl + Z to stop the server
```


## Notes
```
# In my Ubuntu machine, i uses this project with virtual machine.
# If this project not load in your PC, apply this code: 

cd github-beats

python3 -m venv myVenv
source myVenv/bin/activate

./server/start.sh

```


## License

This project is licensed under the [MIT licence](LICENSE)
