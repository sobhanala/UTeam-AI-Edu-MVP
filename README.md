# UTeam AI Education MVP

An educational chatbot prototype with a Next.js frontend and FastAPI backend. The backend supports Gemini and DeepSeek adapters and keeps conversation history in memory.

## Structure

- `Client/uteam-mvp-next/`: Next.js 15, React 19, TypeScript, and Sass client.
- `backend/main.py`: chat, health, and session HTTP endpoints.
- `backend/agent/`: provider adapters.
- `backend/config.py`: provider and application settings.
- `backend/memory.py`: in-memory conversation storage.

## Backend setup

Create a Python environment, install the supplied dependencies and Uvicorn, then set `GEMINI_API_KEY` or `DEEPSEEK_API_KEY` in your environment.

```sh
python -m pip install -r backend/requirements.txt
python -m pip install uvicorn
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Run from the repository root so `backend` imports resolve. Select `gemini` or `deepseek` with the `AGENT` environment variable. The public copy loads credentials and model overrides from environment variables.

Open `http://127.0.0.1:8000/docs`; `GET /health` reports the selected provider. The session endpoints and `POST /chat` are defined in `backend/main.py`.

## Frontend setup

The source includes a Yarn lockfile:

```sh
cd Client/uteam-mvp-next
yarn install
yarn dev
```

Alternatively, install dependencies with npm and use `npm run dev`. Review the client's backend URL before use.

Provider access and model availability must be configured separately. Conversation storage is in memory and is cleared on restart. A full provider-backed chat session was not run during this publication update.

## Credits and source

This is a public portfolio copy of the shared project [UTeam-400/UTeam-AI-Edu-MVP](https://github.com/UTeam-400/UTeam-AI-Edu-MVP), prepared for Sobhan Alaeddini's account. Original authorship and existing license notices are retained. See [SOURCE.md](SOURCE.md) for the source revision and publication notes.
