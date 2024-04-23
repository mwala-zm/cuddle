import React from "react";

const GenreList = ({ movies }) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div className="uppercase text-4xl font-bold">
        <h1>Search For you mood</h1>
      </div>
      {movies.map((movie, index) => (
        <div
          key={index}
          className="bg-white p-4 rounded-md shadow-md hover:shadow-lg"
        >
          <img
            className="w-full h-auto rounded-md mb-4"
            src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
            alt={movie.title}
          />
          <div>
            <p className="text-lg font-semibold mb-2">{movie.title}</p>
            <p className="text-gray-700">Release Date: {movie.release_date}</p>
            <p className="text-gray-700">Overview: {movie.overview}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default GenreList;
