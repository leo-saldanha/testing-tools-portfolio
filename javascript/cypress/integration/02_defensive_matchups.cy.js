import matchupData from "../../../test_data/type_matchup.json";

const defensiveMatchups = matchupData.Defensive;

describe("Test 02 - Defensive matchups", () => {
    beforeEach(() => {
        cy.visit("/defense");
    });

    it("Poison", () => {
        cy.getByTestId("radio-poison").first().forceClick();
        cy.getByTestId("radio-none").last().forceClick();
        cy.assertTypeMatchup(defensiveMatchups.Poison);
    });

    it("Bug", () => {
        cy.getByTestId("radio-bug").first().forceClick();
        cy.getByTestId("radio-none").last().forceClick();
        cy.assertTypeMatchup(defensiveMatchups.Bug);
    });

    it("Ground / Grass", () => {
        cy.getByTestId("radio-ground").first().forceClick();
        cy.getByTestId("radio-grass").last().forceClick();
        cy.assertTypeMatchup(defensiveMatchups.GroundGrass);
    });
});
