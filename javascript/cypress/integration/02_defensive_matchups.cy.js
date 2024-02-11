import matchupData from "../fixtures/type_matchup.json";

const defensiveMatchups = matchupData.Defensive;

describe("Test 02 - Defensive matchups", () => {
    beforeEach(() => {
        cy.visit("/defense");
    });

    it("Poison", () => {
        cy.getByTestId("radio-poison").first().click();
        cy.getByTestId("radio-none").last().click();
        cy.assertTypeMatchup(defensiveMatchups.Poison);
    });
});
