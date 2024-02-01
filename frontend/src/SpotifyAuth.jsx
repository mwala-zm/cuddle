import React, { useEffect } from "react";
// import { useHistory } from "react-router-dom";
import SpotifyWebApi from "spotify-web-api-js";

const spotifyApi = new SpotifyWebApi();

const SpotifyAuth = ({ onTokenReceived }) => {
  // const history = useHistory();
  const client_id = import.meta.env.VITE_SPOTIFY_CLIENT_ID;
  const redirect_uri = import.meta.env.VITE_SPOTIFY_REDIRECT_URI;
  const client_secret = import.meta.env.VITE_SPOTIFY_CLIENT_SECRET;
  const exchange_token = "http://localhost:8000/cuddle/exchange_token/";

  useEffect(() => {
    const handleAuth = async () => {
      const params = new URLSearchParams(window.location.search);
      const code = params.get("code");
      console.log("Code: ", code);

      if (code) {
        try {
          const response = await fetch(exchange_token, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ code }),
          });

          const data = await response.json();
          console.log("ACCESS TOKEN: ", data.access_token);

          // Set the access token in the Spotify API client
          spotifyApi.setAccessToken(data.access_token);

          // Callback to parent component with the access token
          onTokenReceived(data.access_token);
        } catch (error) {
          console.error("Error exchanging code for access token:", error);
        }
      } else {
        // Redirect to Spotify for authentication
        const redirectUri = redirect_uri;
        const clientId = client_id;
        const scopes = ["user-read-private", "user-read-email"]; // Add more scopes as needed
        const authUrl = `https://accounts.spotify.com/authorize?client_id=${client_id}&redirect_uri=${redirect_uri}&scope=${scopes.join("%20")}&response_type=code`;

        window.location.href = authUrl;
      }
    };

    handleAuth();
  }, [onTokenReceived]);

  return <div>Logging in...</div>;
};

export default SpotifyAuth;
