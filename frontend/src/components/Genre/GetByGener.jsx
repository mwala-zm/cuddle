import React, { useEffect, useState } from "react";
import axios from "axios";
import GenreList from "./GenreList";
import { genreData } from "../../constants";

const GetByGener = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [genreName, setGenreName] = useState("");
  const [genreId, setGenreId] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!genreId) {
      return;
    }

    const fetchMovies = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios.get(
          `http://localhost:8000/cuddle/movies/${genreId}/`,
        );
        setMovies(response.data.movies);
      } catch (error) {
        setError("Failed to fetch movies");
      } finally {
        setLoading(false);
      }
    };

    fetchMovies();
  }, [genreId]);

  const handleInputChange = (event) => {
    const name = event.target.value;
    setGenreName(name);

    const genre = genreData.find(
      (g) => g.name.toLowerCase() === name.toLowerCase(),
    );
    if (genre) {
      setGenreId(genre.id);
    } else {
      setGenreId(null);
    }
  };

  return (
    <div>
      <div>
        <input
          type="text"
          placeholder="Enter genre"
          value={genreName}
          onChange={handleInputChange}
        />
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error}</p>
      ) : (
        <div>
          <GenreList movies={movies} />
        </div>
      )}
    </div>
  );
};

export default GetByGener;
