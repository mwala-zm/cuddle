/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  mode: "jit",
  theme: {
    extend: {
      colors: {
        text: "#1E1E1E",
        background: "#F7F8F7",
        primary: "#A0ACA4",
        secondary: "#DEE3E2",
        accent: "#728380",
      },
      fontFamily: {
        satoshi: ["Satoshi", "sans-serif"],
        cabinet: ["Cabinet Grotesk", "sans-serif"],
      },
    },
    screens: {
      xs: "480px",
      ss: "620px",
      sm: "768px",
      md: "1060px",
      lg: "1200px",
      xl: "1700px",
    },
  },
  plugins: [],
};
