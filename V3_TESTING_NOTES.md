# Flat Agree — V3 prototype testing notes

Date: 2 November 2026  
Course: GUI Design & Web Optimization  
Prototype: https://chaaawin.github.io/flat-agree/

## Evidence and limitations

The Week 3 interview answers were illustrative (fictional) scenarios, not recorded interviews with real users. No independent human usability sessions have been conducted or verified for V3. Do **not** treat the scenarios, potential problems, or code inspection below as participant quotations or measured testing outcomes.

## Scenarios driving changes

| Earlier scenario / design assumption | Risk being tested | Change made in V3 |
| --- | --- | --- |
| New roommate does not know unwritten rules | They cannot tell what requires action | Dashboard "needs your response" summary; short three-step explanation |
| Housemates may understand a rule differently | Unsure who agreed and who remains | Per-rule waiting-for names, vote counts and clearer detail explanation |
| A roommate proposes different wording later | Old approvals could be mistaken for approval of new text | Confirmation before updating wording; old votes cleared; version label and previous wording history |
| Overnight guests can involve unexpected delays | Wording may be too rigid | Example guest proposal explicitly asks for prompt notice in unexpected situations |
| A newcomer wants to find what needs attention | Pending rules may be hard to discover | "Needs my reply" filter based on selected demo role |

## Developer walkthrough / test protocol (not participant testing)

1. Open the app and identify the two already-agreed rules and two discussing rules. Observe whether "Agreed" and "Discussing" are visibly distinct.
2. As Jirapat, select "Needs my reply". Check whether the two sample proposals appear. Change role to Alex and repeat.
3. Open the guests proposal and inspect exact wording, number of approvals, and which roommates still need to respond.
4. Simulate approvals by switching roles. Ensure a proposal becomes agreed only after all three accept the same wording.
5. Suggest a change to an agreed rule. Cancel the confirmation: nothing should change. Confirm it: version should increment, earlier wording should remain visible, and only the reviser's vote should remain.
6. Test search/filter combinations on narrow/mobile and desktop screens, and try keyboard Tab / Escape in dialog workflows.
7. Reset the sample data when finished.

## Findings status

- **Code reviewed:** V3 UI logic now includes a pending-response filter, version history and warning before resetting agreement. Changes were made to the HTML/CSS/JS repository files.
- **Automated deployment:** GitHub Actions checks JavaScript syntax on deployment. A successful deployment is separate from participant usability testing.
- **Human testing:** Not conducted / no real observations supplied. Task-completion rates, timings, quotes, and participant counts are intentionally blank.

## Field note template for real testing

| Test person / date | Task | What they tried or said (exact observation) | Difficulty / result | Follow-up change |
| --- | --- | --- | --- | --- |
| [to fill] | Find a rule awaiting your response | [to fill] | [to fill] | [to fill] |
| [to fill] | Explain who has agreed to a guest rule | [to fill] | [to fill] | [to fill] |
| [to fill] | Change an agreed rule and explain what happened | [to fill] | [to fill] | [to fill] |

### Suggested short post-test questions

- What did you expect the "Needs my reply" tab to show?
- Before editing a rule, what did you think would happen to other roommates' approval?
- What one thing would make this app easier to use?

## Prototype limitations

This is a single-browser classroom demo using localStorage. Changing the selected roommate simulates another person; it is not login, identity verification or live syncing. Results should not be represented as production-ready collaboration.
