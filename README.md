# StaticVideoContentGenerator
![Logo](/assets/images/logo.png)

## Description:
StaticVideoContentGenerator is a Python-based tool designed to dynamically create an HTML page that displays video content alongside a structured table of contents. This project simplifies the process of integrating educational or instructional videos with their corresponding sections or topics, making it easier for viewers to navigate through different parts of the video. The generator utilizes a simple text file (content.txt) that contains the video file name on the first line and then lists each topic with its corresponding timestamp.

## How It Works:
The Python script reads the content.txt file, where the first line is expected to be the name (or path) of the video file, and subsequent lines are structured as "Topic Time". For example, a line might read "Introduction 0:03" to indicate that an introduction starts at 3 seconds into the video. The script generates an HTML file that embeds the video and creates a clickable table of contents. Each entry in the table allows the user to jump to the specific time in the video where the topic begins.

## Features:
Generates an HTML page with an embedded video player.
Creates a table of contents based on topics and their timestamps, allowing easy navigation to specific video sections.
Supports local video files and could be adapted for hosted video URLs.
Utilizes Bootstrap for styling to ensure a responsive and modern design.

## How to Use:
### 1. Prepare the content.txt File:
- First line: Name or path of your video file (e.g., "myvideo.mp4").</li>
- Subsequent lines: List each topic and its start time in the video, formatted as "Topic Time" (e.g., "Introduction 0:03").
### 2. Run the Script:

- Ensure you have Python installed on your system.
- Place the generate_html.py script in the same directory as your content.txt.
- Open a terminal or command prompt, navigate to the directory containing the script, and run:
```python
py .\genHTML.py 
```

- The script reads content.txt, processes the contents, and generates an inhalte.html file in the same directory.

## View the Result:

Open the generated inhalte.html file in a web browser to view the embedded video and the interactive table of contents.

## Customization:
The HTML and CSS within the script can be customized to match specific styling requirements or to add additional functionality, such as integrating with different video hosting platforms or adding analytics tracking to table of contents clicks.

## Requirements:
- Python 3.x
- An internet connection (for loading Bootstrap and Font Awesome from CDN)
- A modern web browser to view the generated HTML file

This project is ideal for educators, content creators, and anyone looking to enhance the presentation of video content with an easy-to-navigate structure.