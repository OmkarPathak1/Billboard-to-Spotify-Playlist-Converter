import tkinter as tk
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create Tkinter window
window = tk.Tk()
window.title("Billboard to Spotify Playlist Converter")
window.geometry("610x570")
window.configure(bg="#1DB954")

# Set the theme to Spotify green and black
spotify_green = "#1DB954"
window.config(bg=spotify_green)

# Create a frame for the Spotify API inputs
api_frame = tk.LabelFrame(window, text="Spotify API Credentials")
api_frame.config(bg=spotify_green, foreground="white", font=("Arial", 12))
api_frame.grid(column=0, row=0, padx=10, pady=10)

# Create a label and entry for the Client ID
client_id_label = tk.Label(api_frame, text="Client ID:")
client_id_label.config(background=spotify_green, foreground="white", font=("Arial", 10))
client_id_label.grid(column=0, row=0, padx=5, pady=5)

client_id_entry = tk.Entry(api_frame, width=40)
client_id_entry.grid(column=1, row=0, padx=5, pady=5)

# Create a label and entry for the Client Secret
client_secret_label = tk.Label(api_frame, text="Client Secret:")
client_secret_label.config(background=spotify_green, foreground="white", font=("Arial", 10))
client_secret_label.grid(column=0, row=1, padx=5, pady=5)

client_secret_entry = tk.Entry(api_frame, width=40)
client_secret_entry.grid(column=1, row=1, padx=5, pady=5)

# Create a label and entry for the Redirect URI
redirect_uri_label = tk.Label(api_frame, text="Redirect URI:")
redirect_uri_label.config(background=spotify_green, foreground="white", font=("Arial", 10))
redirect_uri_label.grid(column=0, row=2, padx=5, pady=5)

redirect_uri_entry = tk.Entry(api_frame, width=40)
redirect_uri_entry.grid(column=1, row=2, padx=5, pady=5)

# Create a frame for the date input and button
date_frame = tk.LabelFrame(window, text="Date Input")
date_frame.config(bg=spotify_green, foreground="white", font=("Arial", 12))
date_frame.grid(column=0, row=1, padx=10, pady=10)

# Create a label and entry for the date
date_label = tk.Label(date_frame, text="Date (YYYY-MM-DD):")
date_label.config(background=spotify_green, foreground="white", font=("Arial", 10))
date_label.grid(column=0, row=0, padx=5, pady=5)

date_entry = tk.Entry(date_frame, width=40)
date_entry.grid(column=1, row=0, padx=5, pady=5)

# Create text widget to display output
output_text = tk.Text(window)
output_text.grid(row=1, column=0, padx=20, pady=20)


def create_playlist():
    # Get input values
    client_id = client_id_entry.get()
    client_secret = client_secret_entry.get()
    redirect_uri = redirect_uri_entry.get()
    date = date_entry.get()

    # Scraping Billboard 100
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    # Spotify Authentication
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    output_text.insert(tk.END, f"Authenticated as {user_id}\n")

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            output_text.insert(tk.END, f"Added {song} to playlist\n")
        else:
            output_text.insert(tk.END, f"{song} not found on Spotify\n")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    output_text.insert(tk.END, f"Created playlist {playlist['name']} on Spotify\n")

    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    output_text.insert(tk.END, "Added songs to playlist\n")


# Create a button to trigger the playlist creation process
create_button = tk.Button(window, text="Create Playlist", command=create_playlist)
create_button.config(bg=spotify_green, foreground="black", font=("Arial", 12))
create_button.grid(row=2, column=0, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()

window.wait_visibility()
