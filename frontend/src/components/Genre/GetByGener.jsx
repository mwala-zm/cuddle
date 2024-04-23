import React, { useEffect, useState } from "react";
import axios from "axios";
import GenreList from "./GenreList";

const GetByGener = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [gener_id, setGener_id] = useState("")

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/cuddle/movies/${setGener_id}/`,
        );
        setMovies(response.data.movies);
      } catch (error) {
      } finally {
        setLoading(false);
      }
    };

    fetchMovies();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <div>
        <input type="text" placeholder="enter gener" />
      </div>
      <div>
        <GenreList movies={movies} />
      </div>
    </div>
  );
};

export default GetByGener;
