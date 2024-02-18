import matchupData from "../../../test_data/type_matchup.json";

const offensiveMatchups = matchupData.Offensive;

describe("Test 01 - Offensive matchups", () => {
    const typesArray = [
        "Fighting",
        "Fire",
        "Fairy",
        "Psychic-Ghost",
        "Dragon-Steel"
    ];

    beforeEach(() => {
        cy.visit("/offense");
    });

    typesArray.forEach(($type) => {
        it($type, () => {
            let subtypes = $type.split("-");
            subtypes.forEach(($subtype) => {
                cy.getByTestId(`option-${$subtype.toLowerCase()}`).click();
            });
            cy.assertTypeMatchup(offensiveMatchups[$type]);
        });
    });
});
