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


## How to use this project

```
# Clone this repository
git clone https://www.github.com/FrankSteps/github-beats

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


## License

This project is licensed under the [MIT licence](LICENSE)
