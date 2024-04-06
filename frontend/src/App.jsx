import React from "react";
import { TrendingList, Spotify } from "./components";
import styles from "./styles";

function App() {
  return (
    <div
      className={`${styles.paddingX}bg-background px-[16px] font-satoshi w-full h-screen`}
    >
      <div>
        <TrendingList />
      </div>
    </div>
  );
}

export default App;
