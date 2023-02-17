from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head>
                <title>Griffel wifi page</title>
            </head>
            <body>
                <h1>Griffel wifi page</h1>
            </body>
        </html>
        """