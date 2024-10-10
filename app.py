from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the songs dataset
songs_df = pd.read_csv('songs.csv')

def recommend_songs(song_title, artist_name=None, genre=None):
    # If both artist and genre are provided, use both to filter recommendations
    if artist_name and genre:
        filtered_songs = songs_df[
            (songs_df['artist'].str.lower() == artist_name.lower()) &
            (songs_df['genre'].str.lower() == genre.lower())
        ]
    # If only genre is provided, recommend based on genre
    elif genre:
        filtered_songs = songs_df[songs_df['genre'].str.lower() == genre.lower()]
    # If only artist is provided, recommend based on artist
    elif artist_name:
        filtered_songs = songs_df[songs_df['artist'].str.lower() == artist_name.lower()]
    # If neither is provided, fallback to recommendations based only on song title
    else:
        song_row = songs_df[songs_df['song_title'].str.lower() == song_title.lower()]
        if song_row.empty:
            return ["Song not found. Please enter a valid song title."]
        
        song_genre = song_row['genre'].values[0]
        filtered_songs = songs_df[songs_df['genre'].str.lower() == song_genre.lower()]

    # Exclude the original song if present
    filtered_songs = filtered_songs[filtered_songs['song_title'].str.lower() != song_title.lower()]

    # Get top 5 similar songs
    top_songs = filtered_songs['song_title'].head(5).tolist()
    if not top_songs:
        return ["No other songs found matching the criteria."]
    
    return top_songs

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    song_title = data.get('song_title')
    artist_name = data.get('artist_name')  # New field for artist
    genre = data.get('genre')  # New field for genre
    
    # Call the updated recommendation function with all fields
    recommendations = recommend_songs(song_title, artist_name, genre)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
