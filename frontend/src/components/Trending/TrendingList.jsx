import React, { useEffect, useState } from "react";
import axios from "axios";
import List from "./List";

const TrendingList = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get(
          //TODO:(Mwala) put this in an env file
          "http://localhost:8000/cuddle/trending/",
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
      <List movies={movies} />
    </div>
  );
};

export default TrendingList;
