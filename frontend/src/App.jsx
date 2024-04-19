import React from "react";
import { TrendingList, Spotify } from "./components";
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
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
