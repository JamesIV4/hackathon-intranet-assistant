# Genesys Intranet Assistant

## Backend

At the root level, run:

```bash
uvicorn backend.main:app --reload --port 8000
```

## Frontend

To run the development server:

```bash
cd frontend
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

Or use:

```bash
cd frontend
npm run build
npm start
```
