# Adding rate limits to your API

For more detailed documentation check out [docs.ratelimit.xyz](docs.ratelimit.xyz).

## Quickstart

1. Install the RateLimit CLI.

```bash
pip install ratelimitcli
```

2. Configure the RateLimit CLI and follow the interactive prompts. You won't have an API key yet so you can just press `[ENTER]` when asked for a value.

```bash
ratelimitcli configure
```

3. Request an API key. You'll be asked to enter credit card information.

```bash
ratelimitcli billing configure
```

4. Check to see that the config file has been written to `$HOME/.ratelimit/config`

```bash
cat ~/.ratelimit/config
```

5. Create your first rate limit.

```bash
ratelimitcli limits upsert --throttling-burst-limit 2 --throttling-rate-limit 0
```

Returns

```
Ok: API response ({"limit_id": "a9f9f31b-2c0b-321b-b398-f9d36kd30820"}).
```

6. Test your first rate limit.

```bash
ratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # ok
ratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # ok
ratelimitcli limits record a9f9f31b-2c0b-321b-b398-f9d36kd30820  # error
```

7. Test rate limits in an interpreter shell.

```python
>>> from ratelimitcli.client.client import RatelimitClient
>>> client = RatelimitClient(client_id="<email>", api_key="<api_key>")
>>> client.sync_record_request("a9f9f31b-2c0b-321b-b398-f9d36kd30820")
```

8. Use your rate limit in your code.

```python
from fastapi import FastAPI
from ratelimitcli.client.client import APIRateLimitException, RatelimitClient as ratelimitclient

app = FastAPI()

def on_error_callback(_: APIRateLimitException):
    return "Goodbye, World!"


@app.get("/")
@ratelimitclient(
    id="a9f9f31b-2c0b-321b-b398-f9d36kd30820",
    callback=on_error_callback,
)
async def hello():
    return "Hello, World!"
```
