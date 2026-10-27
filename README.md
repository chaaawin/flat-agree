# Flat Agree

Jirapat Chayapong — GUI Design & Web Optimization, Week 4.

A first implemented classroom prototype based on the Week 3 shared-apartment design brief. No earlier implemented v1 was supplied. The Week 3 interview examples are fictional, so this build tests design assumptions rather than claiming validated user research.

## Run

No packages, build step, server account or API keys are required.

    python3 -m http.server 8080 --directory dist

Open http://localhost:8080. Static hosting also works. Use a modern browser.

## Files

- `dist/index.html`: page structure and accessible forms.
- `dist/style.css`: responsive design.
- `dist/app.js`: demo state, proposals, unanimous acceptance, revisions, comments, moving-in checklist and feedback export.
- `dist/prototype.pdf`: four lo-fi screens and design rationale.
- `make_prototype.py`: regenerates the PDF with Python reportlab.

## Core flow

1. Browse agreed and discussing rules. Filter or search.
2. Propose a specific household rule. It starts with the current role's vote.
3. Switch demo roles using the header selector. Each roommate can accept, withdraw, comment or suggest a change.
4. A rule is agreed only when all three accept. Revising clears previous acceptance and starts with the reviser's vote.
5. Use Moving in for a browser-local checklist.
6. Use Test & feedback for three usability tasks, saved notes and a JSON export.

## Prototype boundaries

The three named roommates and initial rules are demo data. The role selector simulates people on one device; it is not authentication. Data uses localStorage in this browser and is not synchronized across devices. It is not ready for real household accounts. The app makes no legal claims about house rules.

## Validation

- JavaScript syntax checked with `node --check dist/app.js`.
- Browser checked: viewing a pending rule, third acceptance changing it to Agreed, revising that rule returning it to Discussing with 1/3 votes.
- The three-page PDF was rendered and visually checked.
- User testing has not been conducted. Collect real observations before describing research findings or comparison results.

## Suggested one-minute introduction

Flat Agree helps people living together make their expectations clear. A new roommate may not know the unwritten rules, and existing roommates may understand those rules differently. The app lets someone propose a rule about cleaning, noise, guests or shared things. Everyone can agree, comment or suggest a change. A rule becomes agreed only when all three roommates accept the same text. If the text changes, everyone needs to respond again. There is also a moving-in checklist to help a new roommate get started. This version is a browser-local classroom demo, and I want to test whether people understand the difference between a proposal and an agreement.
