// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './theme/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'nimverta-teal': '#2E9A8E', // primary color
        'nimverta-dark': '#333333', // primary text color
        'nimverta-light-gray': '#F8F8F8', // background color
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
