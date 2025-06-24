# Genesys Intranet Assistant

## Backend

At the root level:

1. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

2. Pull the data from Confluence

   ```bash
   python backend/confluence_pull.py
   ```

3. Ingest the wiki:

   ```bash
   python backend/ingest.py
   ```

4. Run:

   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
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
