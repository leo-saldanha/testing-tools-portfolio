import allPokemonData from "../fixtures/pokemons.json";

describe("Test 03 - Search Pokedex", () => {
    beforeEach(() => {
        cy.visit("/pokedex");
    });

    it("Search for Poliwhirl", () => {
        cy.searchPokedex("Poliwhirl");
        cy.assertPokedexResult(allPokemonData.Poliwhirl);
    });

    it("Search for Snorlax", () => {
        cy.searchPokedex("Snorlax");
        cy.assertPokedexResult(allPokemonData.Snorlax);
    });

    it("Search for Magcargo", () => {
        cy.searchPokedex("Magcargo");
        cy.assertPokedexResult(allPokemonData.Magcargo);
    });

    it("Search for Ninjask", () => {
        cy.searchPokedex("Ninjask");
        cy.assertPokedexResult(allPokemonData.Ninjask);
    });

    it("Search for Pachirisu", () => {
        cy.searchPokedex("Pachirisu");
        cy.assertPokedexResult(allPokemonData.Pachirisu);
    });
});
