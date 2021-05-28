module.exports = {
  purge: {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    options: {
      safelist: {
        deep: [/explanation-container/],
      },
    },
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      primary: ['"Oswald"', "sans-serif"],
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
