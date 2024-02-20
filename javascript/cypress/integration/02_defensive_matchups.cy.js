import matchupData from "../../../test_data/type_matchup.json";

const defensiveMatchups = matchupData.Defensive;

describe("Test 02 - Defensive matchups", () => {
  beforeEach(() => {
    cy.visit("/defense");
  });

  ["Poison", "Bug", "Ground-Grass"].forEach(($type) => {
    it($type, () => {
      let subtypes = $type.split("-");
      cy.getByTestId(`radio-${subtypes[0].toLowerCase()}`).first().click();
      if (subtypes.length > 1) {
        cy.getByTestId(`radio-${subtypes[1].toLowerCase()}`).last().click();
      }
      cy.assertTypeMatchup(defensiveMatchups[$type]);
    });
  });
});
