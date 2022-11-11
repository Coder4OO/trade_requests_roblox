import roblox
import json
from statistics import median


async def get_inbound_trades(client):
    trades = await client.requests.get("https://trades.roblox.com/v1/trades/Inbound?sortOrder=Asc&limit=10")
    return json.loads(trades.content.decode())["data"]

async def get_trade_information(client, tradeid):
    information = await client.requests.get("https://trades.roblox.com/v1/trades/"+str(tradeid))
    return json.loads(information.content.decode())

async def accept_trade(client, tradeid):
    await client.requests.post("https://trades.roblox.com/v1/trades/"+str(tradeid)+"/accept")

async def decline_trade(client, tradeid):
    await client.requests.post("https://trades.roblox.com/v1/trades/"+str(tradeid)+"/decline")

async def calculate_item_MAP(client, itemid):
    asset = roblox.BaseAsset(client._shared, asset_id=itemid)
    data = await asset.get_resale_data()
    resale_data = data.price_data_points
    values = []
    for stamp in resale_data:
        values.append(stamp['value'])
    return median(values)


