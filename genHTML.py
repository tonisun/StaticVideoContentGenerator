import os

def generate_html(video_filename, content_lines, output_filename='content.html'):
    html_content = f'''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
    
    <style>
        .table-rounded {{
            border-radius: 10px;
            overflow: hidden;
        }}
    </style>
    <title>{video_filename}</title>
</head>
<body>
    <div class="container mt-5">
        <h1>{video_filename}</h1>
        <video id="myVideo" controls width="100%" class="table-rounded shadow">
            <source src="{video_filename}" type="video/mp4">
            Ihr Browser unterstützt das Video-Tag nicht.
        </video>
        <table class="table table-bordered table-rounded shadow mt-4">
            <thead class="thead-dark">
                <tr>
                    <th>Time</th>
                    <th>Topic</th>
                </tr>
            </thead>
            <tbody>
    '''

    for line in content_lines:
        if line.strip():  # Ensure the line is not empty. (Stelle sicher, dass die Zeile nicht leer ist)
            try:
                topic, time  = line.rsplit(' ', 1)  # Correctly splits each line at the last space. (Korrekt: Teilt jede Zeile beim letzen Leerzeichen)
                html_content += f'<tr><td><a href="#" onClick="startVideo(timeInSeconds(\'{time}\'))">{time}</a></td><td>{topic}</td></tr>\n'
            except ValueError as e:
                print(f"Error processing line (Fehler beim Verarbeiten der Zeile): {line}. Error (Fehler): {e}")

    html_content += '''
            </tbody>
        </table>
    </div>
    <script>
        function startVideo(time) {
            var video = document.getElementById('myVideo');
            video.currentTime = time;
            video.play();
        }

        function timeInSeconds(timeString) {
            // Splits the time string into its components
            const parts = timeString.split(':').reverse();
            let seconds = 0;

            // Iterates through the parts and converts them accordingly
            // parts[0] = Seconds, parts[1] = Minutes, parts[2] = Hours
            if (parts[0]) seconds += parseInt(parts[0]); // Adds seconds
            if (parts[1]) seconds += parseInt(parts[1]) * 60; // Adds minutes as seconds
            if (parts[2]) seconds += parseInt(parts[2]) * 3600; // Adds hours as seconds

            return seconds;
        }
    </script>
</body>
</html>
    '''

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"{output_filename} has been successfully created.")

    output_filename = os.path.join(os.getcwd(), 'content.html')
    #print(content_lines)

def main():
    input_filename = 'content.txt'
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    video_filename = lines[0].strip()  # The first entry is the video filename. (Der erste Eintrag ist der Videodateiname)
    content_lines = [line.strip() for line in lines[1:]]  # The rest are the contents. (Der Rest sind die Inhalte)
    
    generate_html(video_filename, content_lines)

if __name__ == '__main__':
    main()
