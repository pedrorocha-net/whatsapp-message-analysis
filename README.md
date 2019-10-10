# WhatsApp Message Analyzer

## What is it?

It's a script that analyzes all the messages in a given WhatsApp group chat and visualizes the most active users, the most used words and the dates and times with the most activity.

## Setup & Usage:

1. Download and install Python3.

2. Clone or download this repository and enter the root directory. 

3. Run `pip install -r requirements.txt`

4. Get a chat by going into a group -> Settings -> Email Chat -> No Media.

5. Place the downloaded .txt file containing the chats in the same folder as this script.

6. Run the script in the command line with the following format:
`analyze.py chat.txt` where chat.txt is the file containing the chats

7. The below images will be generated in an output folder along with an excel sheet containing the formatted data:

```
groupname-data.xlsx
```