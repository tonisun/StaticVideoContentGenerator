import os

def generate_html(video_filename, content_lines, output_filename='inhalte.html'):
    html_content = f'''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
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
                    <th>Zeit</th>
                    <th>Thema</th>
                </tr>
            </thead>
            <tbody>
    '''

    for line in content_lines:
        if line.strip():  # Stelle sicher, dass die Zeile nicht leer ist
            try:
                topic, time  = line.rsplit(' ', 1)  # Korrekt: Teilt jede Zeile beim ersten Leerzeichen
                html_content += f'<tr><td><a href="#" onClick="startVideo(zeitInSekunden(\'{time}\'))">{time}</a></td><td>{topic}</td></tr>\n'
            except ValueError as e:
                print(f"Fehler beim Verarbeiten der Zeile: {line}. Fehler: {e}")

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

        function zeitInSekunden(zeitString) {
            // Teilt den Zeitstring in seine Komponenten
            const teile = zeitString.split(':').reverse();
            let sekunden = 0;

            // Geht die Teile durch und rechnet sie entsprechend um
            // teile[0] = Sekunden, teile[1] = Minuten, teile[2] = Stunden
            if (teile[0]) sekunden += parseInt(teile[0]); // Addiert Sekunden
            if (teile[1]) sekunden += parseInt(teile[1]) * 60; // Addiert Minuten in Sekunden
            if (teile[2]) sekunden += parseInt(teile[2]) * 3600; // Addiert Stunden in Sekunden

            return sekunden;
        }
    </script>
</body>
</html>
    '''

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"{output_filename} wurde erfolgreich erstellt.")

    output_filename = os.path.join(os.getcwd(), 'inhalte.html')
    #print(content_lines)

def main():
    input_filename = 'inhalte.txt'
    
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    video_filename = lines[0].strip()  # Der erste Eintrag ist der Videodateiname
    content_lines = [line.strip() for line in lines[1:]]  # Der Rest sind die Inhalte
    
    generate_html(video_filename, content_lines)

if __name__ == '__main__':
    main()
