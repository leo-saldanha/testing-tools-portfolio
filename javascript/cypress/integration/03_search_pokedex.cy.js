import allPokemonData from "../../../test_data/pokemons.json";

describe("Test 03 - Search Pokedex", () => {
  beforeEach(() => {
    cy.visit("/pokedex");
  });

  ["Poliwhirl", "Snorlax", "Magcargo", "Ninjask", "Pachirisu"].forEach(
    ($pokemon) => {
      it(`Search for ${$pokemon}`, () => {
        cy.searchPokedex($pokemon);
        cy.assertPokedexResult(allPokemonData[$pokemon]);
      });
    }
  );
});
