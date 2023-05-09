# Billboard-to-Spotify-Playlist-Converter

This Python script converts Billboard Top 100 chart to a Spotify playlist using Spotipy API. It creates a playlist, searches for the songs on Spotify and adds them to the playlist. User can provide date and playlist name.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Code](#running-the-code)
  - [Tkinter GUI](#tkinter-gui)
- [Video Demos](#video-demos)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The Billboard to Spotify project is a tool that allows users to easily convert their favorite Billboard charts into Spotify playlists. The project utilizes Python and several APIs, including the Billboard API and Spotify API, to retrieve data on the top tracks and artists from Billboard and then create a Spotify playlist based on that data. The user can specify the chart type and date range for the data retrieval and can also choose to exclude certain artists or tracks from the playlist. The tool also features a user-friendly GUI built using the Tkinter library, which makes it easy to navigate and customize the playlist. Overall, the project provides a convenient way for music lovers to discover and listen to the latest and greatest hits from the Billboard charts on their favorite streaming platform, Spotify.

## Installation

1. Clone the repository:

```
git clone [https://github.com/OmkarPathak1/billboard-to-spotify-playlist.git.]
```

2. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

### Running the Code

To use the script, follow these steps:

1. Navigate to the project directory:

```
cd [insert project directory name]
```

2. Run the code:

```
python main.py
```

### Tkinter GUI

1.Create a Spotify developer account and create a new app to obtain your Client ID and Client Secret.
2. Enter the date in the format YYYY-MM-DD for which you want to create a Spotify playlist.
3. Click the Create Playlist button to authenticate with Spotify and create the playlist.
4. The script will scrape the Billboard Hot 100 chart for the specified date, search for the songs on Spotify, and add them to a new private playlist in your Spotify account.


## Video Demos



### Running the Code

```<iframe width="560" height="315" src="https://www.youtube.com/embed/4YIcug77s9E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>```

### Tkinter GUI

```<iframe width="560" height="315" src="https://www.youtube.com/embed/aeERxNbrunk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>```

## Contributing

If you want to contribute to this project, feel free to submit a pull request with your changes or open an issue to report a bug or suggest an improvement.

## License

This project is licensed under the MIT License.
