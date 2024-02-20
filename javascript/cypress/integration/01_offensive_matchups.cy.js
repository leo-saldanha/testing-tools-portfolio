import matchupData from "../../../test_data/type_matchup.json";

const offensiveMatchups = matchupData.Offensive;

describe("Test 01 - Offensive matchups", () => {
  beforeEach(() => {
    cy.visit("/offense");
  });

  ["Fighting", "Fire", "Fairy", "Psychic-Ghost", "Dragon-Steel"].forEach(
    ($type) => {
      it($type, () => {
        let subtypes = $type.split("-");
        subtypes.forEach(($subtype) => {
          cy.getByTestId(`option-${$subtype.toLowerCase()}`).click();
        });
        cy.assertTypeMatchup(offensiveMatchups[$type]);
      });
    }
  );
});
