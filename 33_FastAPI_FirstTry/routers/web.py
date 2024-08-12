import os
from fastapi.responses import FileResponse
from fastapi import APIRouter
from starlette.responses import HTMLResponse


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Car Sharing Demo</title>
        </head>
        <body>
            <h1>Welcome to the Car Sharing Service</h1>
            <p>Here is some text for you</p>
        </body>
    </html>
    """

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    '''Serves the favicon.ico file'''
    return FileResponse(os.path.join('static', 'favicon.ico'))
