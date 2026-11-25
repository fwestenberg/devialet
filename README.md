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

## Push notifications

Instead of polling `async_update()`, the state can be kept up to date with push notifications.
`async_listen()` runs until it is cancelled and reconnects automatically.

```python
async def main():
    async with aiohttp.ClientSession() as session:
        client = DevialetApi('192.168.1.10', session)
        await client.async_update()

        def on_update():
            print(client.volume_level, client.playing_state, client.media_title)

        def on_connection_change(connected):
            print("Notifications connected:", connected)

        await client.async_listen(on_update, on_connection_change)
```

### Protocol

Devices running a recent DOS firmware expose a WebSocket at `ws://<host>/ipcontrol/v1/notifications`.
After connecting, the client sends the endpoints it wants to follow:

```json
{
  "messageType": "subscriptionManagement",
  "messageData": {"requiredSubscriptions": ["/systems/current/sources/current/soundControl/volume"]}
}
```

The device confirms with a `subscriptionManagement` message listing `currentSubscriptions` and
`failedSubscriptions`, sends the current state of every subscribed endpoint, and then a message for
every change. The `messageData` has the same content as the response of a `GET` on that endpoint:

```json
{
  "messageType": "notification",
  "subscription": "/systems/current/sources/current/soundControl/volume",
  "messageData": {"volume": 36}
}
```
