import React from "react";
import { MovieList } from "./components";

function App() {
  return (
    <div className="bg-background px-[16px] overflow-hidden font-satoshi">
      <div>
        <MovieList />
      </div>
    </div>
  );
}

export default App;
