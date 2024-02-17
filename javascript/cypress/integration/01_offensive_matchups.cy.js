import matchupData from "../../../test_data/type_matchup.json";

const offensiveMatchups = matchupData.Offensive;

describe("Test 01 - Offensive matchups", () => {
    beforeEach(() => {
        cy.visit("/offense");
    });

    it("Fighting", () => {
        cy.getByTestId("option-fighting").click();
        cy.assertTypeMatchup(offensiveMatchups.Fighting);
    });

    it("Fire", () => {
        cy.getByTestId("option-fire").click();
        cy.assertTypeMatchup(offensiveMatchups.Fire);
    });

    it("Fairy", () => {
        cy.getByTestId("option-fairy").click();
        cy.assertTypeMatchup(offensiveMatchups.Fairy);
    });

    it("Psychic / Ghost", () => {
        cy.getByTestId("option-psychic").click();
        cy.getByTestId("option-ghost").click();
        cy.assertTypeMatchup(offensiveMatchups.PsychicGhost);
    });

    it("Dragon / Steel", () => {
        cy.getByTestId("option-dragon").click();
        cy.getByTestId("option-steel").click();
        cy.assertTypeMatchup(offensiveMatchups.DragonSteel);
    });
});
