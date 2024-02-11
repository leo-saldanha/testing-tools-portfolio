
/** Assertions **/

Cypress.Commands.add("assertTypeMatchup", (matchupData) => {
    for (const [effectiveness, types] of Object.entries(matchupData)) {
        for (const type of types) {
            cy.getByTestId(`section-${effectiveness}`)
                .getByTestId(`result-${type.toLowerCase()}`).should("contain", type);
        }
    }
});

/** Common **/

Cypress.Commands.add("getByTestId", (selector, ...args) => {
    return cy.get(`[data-testid="${selector}"]`, ...args);
});

Cypress.Commands.add("forceClick", { prevSubject: "element" }, (subject) => {
    return cy.wrap(subject).click({ force: true });
});

Cypress.Commands.add("clearAndType", { prevSubject: "element" }, (subject, text) => {
    cy.wrap(subject).clear();
    cy.wrap(subject).type(text);
});

Cypress.Commands.add("containsExactly", { prevSubject: "element" }, (subject, pattern) => {
    return cy.wrap(subject).contains(new RegExp(`^${pattern}$`, "g"));
});

