import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [songTitle, setSongTitle] = useState('');
    const [artistName, setArtistName] = useState(''); // New input for artist name
    const [genre, setGenre] = useState(''); // New input for genre
    const [recommendations, setRecommendations] = useState([]);

    const getRecommendations = async () => {
        const response = await axios.post('http://127.0.0.1:5000/recommend', {
            song_title: songTitle,
            artist_name: artistName, // Send the artist name along with the song title
            genre: genre, // Send the genre along with the song title
        });
        setRecommendations(response.data);
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Song Recommendation System</h1>

            {/* Input for Song Title */}
            <input
                type="text"
                placeholder="Enter a song title"
                value={songTitle}
                onChange={(e) => setSongTitle(e.target.value)}
                style={{ marginBottom: '10px', padding: '10px', width: '300px' }}
            />
            <br />

            {/* Input for Artist Name */}
            <input
                type="text"
                placeholder="Enter artist name"
                value={artistName}
                onChange={(e) => setArtistName(e.target.value)}
                style={{ marginBottom: '10px', padding: '10px', width: '300px' }}
            />
            <br />

            {/* Input for Genre */}
            <input
                type="text"
                placeholder="Enter genre"
                value={genre}
                onChange={(e) => setGenre(e.target.value)}
                style={{ marginBottom: '20px', padding: '10px', width: '300px' }}
            />
            <br />

            <button onClick={getRecommendations} style={{ padding: '10px 20px' }}>Get Recommendations</button>

            <h2>Recommendations:</h2>
            <ul>
                {recommendations.map((song, index) => (
                    <li key={index}>{song}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
