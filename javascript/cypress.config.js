const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://127.0.0.1:5173/",
    specPattern: ["cypress/integration/**/*.cy.{js,jsx,ts,tsx}"],
    experimentalRunAllSpecs: true,
  },
  viewportWidth: 1920,
  viewportHeight: 1080,
});
