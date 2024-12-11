from js import Response, fetch
from urllib.parse import urlparse, parse_qs
import markdown

async def on_fetch(request, env):
    # Parse the incoming request URL
    url = urlparse(request.url)
    # Parse the query parameters into a Python dictionary
    params = parse_qs(url.query)

    response = await fetch(params['from'][0])
    return Response.new(markdown.markdown(await response.text()))