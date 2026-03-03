# Static Site Hosting with GitHub Pages and Pelican

This is a general purpose walk through of how to start hosting a static site generated using Pelican and hosted on GitHub pages, suitable for anyone with a beginner level understanding of command line interfaces and GitHub.

## Requirements:
- Python 3.9 or greater
- A GitHub Account
- A basic understanding of command line
- An understanding of the Markdown language
- An Internet Connection (If you're reading this congratulations! You likely have this)

### Some Assumptions
I run Linux (Specifically Ubuntu), I assume you are running this as well, a different OS may use different commands  
[A guide for Windows](https://docs.pelicanplatform.org/install/windows)  
[A guide for MacOS](https://docs.pelicanplatform.org/install/macos)  
## Instructions:
### Setup:
1. Set up and activate a python virtual environment:  
```
python -m venv venv
source venv/bin/activate
```
2. Install Pelican and Markdown:
```
python -m pip install "pelican[markdown]"
```
