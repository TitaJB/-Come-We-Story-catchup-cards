# Catch-Up Cards

Offline-first conversation-card PWA containing 750 original prompts across 15 decks.

## Run locally

From this directory:

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080`.

Do not open `index.html` directly, because service workers require HTTP or HTTPS.

## iPhone installation

1. Visit the deployed HTTPS URL in Safari.
2. Wait for the first full load.
3. Tap Share.
4. Tap **Add to Home Screen**.
5. Open the installed app once while online.
6. Turn on Airplane Mode, force-close the app, and reopen it.
7. Confirm prompts still advance.

## Files

- `DEVELOPMENT_SPEC.md` — full MVP specification.
- `CODEX_IMPLEMENTATION_PROMPT.md` — ready-to-submit Codex task.
- `data/questions.json` — exactly 750 prompts.
- `index.html`, `styles.css`, `app.js` — application.
- `manifest.webmanifest`, `sw.js` — PWA/offline support.
