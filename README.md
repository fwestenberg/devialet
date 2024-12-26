# Devialet
Devialet Python package

Please find the documentation Home Assistant documentation [here:](https://www.home-assistant.io/integrations/devialet)

**Example:**

```python
import asyncio
import aiohttp

from devialet import DevialetApi


async def main():
    session = async with aiohttp.ClientSession() as session:
        client = DevialetApi('192.168.1.10', session)
        await client.async_update()
        await client.async_set_volume_level(20)
        await client.async_media_next_track()
        await client.async_turn_off()

asyncio.run(main())

```