module.exports = {
  purge: [
    './templates/**/*.html',
    './templates/**/**/*.html',
    './templates/**/**/**/*.html',
    './templates/base.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
