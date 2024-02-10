import React from "react";
import { MovieList, Spotify } from "./components";
import styles from "./styles";

function App() {
  return (
    <div
      className={`${styles.paddingX}bg-background px-[16px] overflow-hidden font-satoshi w-full h-screen`}
    >
      <div className={`${styles.padding}`}>
        <h2 className={`${styles.heading2}`}>Quotes</h2>
        <ul>
          <li>In the Air</li>
        </ul>
      </div>
      <div>
        <MovieList />
      </div>
    </div>
  );
}

export default App;
