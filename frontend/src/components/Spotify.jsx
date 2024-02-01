import React, { useState } from "react";
import SpotifyAuth from "../SpotifyAuth";

const Spotify = () => {
  const [spotifyToken, setSpotifyToken] = useState(null);
  const handleTokenReceived = (token) => {
    setSpotifyToken(token);
  };

  return (
    <div>
      {spotifyToken ? (
        <h2>Success!</h2>
      ) : (
        <SpotifyAuth onTokenReceived={handleTokenReceived} />
      )}
    </div>
  );
};

export default Spotify;
