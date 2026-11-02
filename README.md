# Flat Agree — Version 3

Jirapat Chayapong — GUI Design & Web Optimization.

**Working app (GitHub Pages):** https://chaaawin.github.io/flat-agree/  
**Source:** https://github.com/chaaawin/flat-agree  
**V3 testing notes and protocol:** [V3_TESTING_NOTES.md](V3_TESTING_NOTES.md)

A responsive classroom prototype to help roommates propose, discuss and agree on clear shared-home rules.

## What changed for V3

These changes respond to *hypothetical Week 3 interview scenarios*, not validated participant interviews:

1. A clear dashboard summary and **Needs my reply** filter show rules awaiting the selected demo roommate.
2. Each card and rule detail shows who still needs to respond and explains the next step.
3. A short three-stage guide explains when a rule becomes agreed.
4. Editing prompts a warning that previous approvals will be reset.
5. Changed rules include a version number and a view of previous wording.
6. The sample overnight-guests rule recognizes unexpected travel delays.

## How to try it

Open the [live site](https://chaaawin.github.io/flat-agree/) or run:

```bash
python3 -m http.server 8080 --directory dist
```

Then visit http://localhost:8080. Change the demo roommate in the top-right menu to simulate other responses. All three simulated roommates must agree on the same version of a rule.

## Source files

- `dist/index.html`: structure, forms and controls
- `dist/style.css`: responsive visual design
- `dist/app.js`: local demo state and interaction logic
- `V3_TESTING_NOTES.md`: design-to-change mapping and testing protocol
- `dist/prototype.pdf`: earlier low-fidelity concept, not a fresh V3 prototype PDF

## Research and testing integrity

The earlier interview responses were fictional examples. There are **no verified real-user interview results or usability sessions** yet. The testing notes document design hypotheses and a reproducible walkthrough; they do not claim observed participant outcomes. Real observations can be added after testing.

## Technical limits

This is a front-end prototype: data is stored in the browser via localStorage, not a shared server. Switching demo roles does not authenticate or synchronize people. The deployment workflow checks JavaScript syntax; it does not prove usability.
