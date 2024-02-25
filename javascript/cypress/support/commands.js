/** Actions **/

Cypress.Commands.add("searchPokedex", (pokemonName) => {
  cy.getByTestId("page-pokedex").within(() => {
    cy.getByTestId("search-bar").clearAndType(pokemonName);
    cy.getByTestId(`title-${pokemonName.toLowerCase()}`).should(
      "contain",
      pokemonName
    );
  });
});

/** Assertions **/

Cypress.Commands.add("assertTypeMatchup", (matchupData) => {
  for (const [effectiveness, types] of Object.entries(matchupData)) {
    cy.getByTestId(`section-${effectiveness}`).within(() => {
      for (const type of types) {
        cy.getByTestId(`result-${type.toLowerCase()}`).should("contain", type);
      }
    });
  }
});

Cypress.Commands.add("assertPokedexResult", (pokemonData) => {
  let summedStats = 0;

  cy.getByTestId(`entry-${pokemonData.id}`).within(() => {
    if (Array.isArray(pokemonData.type)) {
      for (const type of pokemonData.type) {
        cy.assertPokedexTypeTag(type);
      }
    } else {
      cy.assertPokedexTypeTag(pokemonData.type);
    }

    for (const [stat, value] of Object.entries(pokemonData.stats)) {
      cy.getByTestId(`text-${String(stat).toLowerCase()}`).should(
        "contain",
        value
      );
      summedStats += parseInt(value);
    }

    cy.getByTestId("text-total").should("contain", summedStats);
  });
});

Cypress.Commands.add("assertPokedexTypeTag", (type) => {
  cy.getByTestId(`tag-${String(type).toLowerCase()}`).should("contain", type);
});

/** Common **/

Cypress.Commands.add("getByTestId", (selector, ...args) => {
  return cy.get(`[data-testid="${selector}"]`, ...args);
});

Cypress.Commands.add(
  "clearAndType",
  { prevSubject: "element" },
  (subject, text) => {
    cy.wrap(subject).clear();
    cy.wrap(subject).type(text);
  }
);
