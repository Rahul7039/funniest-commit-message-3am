# Candidates — 3 AM Hotfix: The Funniest Commit Message

Judge brief (most important first): (1) a one-line git commit message from a
developer who just fixed production at 3 AM; (2) makes a tired engineer laugh
out loud on a single read, with a real punchline, not a mild pun; (3) true to a
3 AM hotfix, with a specific production detail (rollback, revert, pager,
on-call); (4) sounds like a commit message a developer would actually write,
terse and imperative; (5) wastes no words, lands well under the 180-char limit.

## Candidates (all scored against the brief)

1. `Revert the Friday deploy: prod died at 3 AM and the pager has filed for divorce` (79 chars)
   — CHOSEN. Imperative "Revert"; three concrete details (Friday deploy, prod
   died, 3 AM, pager); the divorce punchline is a real joke that lands alone
   with no explanation; 79 chars is well under the limit.

2. `fix: prod is back, the pager is quiet, and I am never deploying on a Friday again` (81 chars)
   — Strong and true, but a statement of fact rather than an imperative, and
   the punchline ("never deploying on a Friday again") is a familiar trope
   rather than a fresh joke.

3. `fix: rollback the deploy that paged me at 3 AM; it has been demoted to a cron job` (81 chars)
   — Good dry punchline ("demoted to a cron job"), but the joke needs a beat
   of thought to land; the divorce line in #1 lands instantly.

4. `Revert last deploy: it took prod down at 3 AM and the pager woke the whole street` (81 chars)
   — Specific and imperative, but "woke the whole street" is a mild image,
   not a punchline; it reads as a complaint, not a joke.

5. `fix: stop the 3 AM pager screaming by reverting the deploy that woke it` (71 chars)
   — Terse and true, but circular (pager screaming / deploy that woke it) and
   no punchline at all; it describes the fix without being funny.

6. `Revert the deploy that killed prod at 3 AM; the pager and I are done` (68 chars)
   — Shortest and punchy, but "the pager and I are done" is a weaker,
   flatter version of the divorce joke in #1; #1 commits to the bit harder.

## Submitted line

`Revert the Friday deploy: prod died at 3 AM and the pager has filed for divorce`
