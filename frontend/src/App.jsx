import React from "react";
import { TrendingList, Spotify, GetGenre } from "./components";
import styles from "./styles";
import {
  BrowserRouter, Route, Routes,
} from 'react-router-dom';

function App() {
  return (
    <div
      className={`${styles.paddingX}bg-background px-[16px] font-satoshi w-full h-screen`}
    >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<TrendingList />} />
          <Route path="/search" element={<GetGenre />} />
          <Route path="/music" element={<Spotify />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
