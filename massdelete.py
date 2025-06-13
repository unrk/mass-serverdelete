# pip install requests
import requests

#------------------------------------------
"""

it does not bypass ratelimit so sometimes you need to wait like 10s
and run the code again, use this code if you got nuked or 
if you got a lot of server with the same name

"""
#------------------------------------------

def delete_guilds(token, guild_name):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
    if resp.status_code != 200:
        print(f"Failed to fetch guilds: {resp.status_code} {resp.text}")
        return
    guilds = resp.json()
    found = False
    for guild in guilds:
        if isinstance(guild, dict) and guild.get('name') == guild_name:
            found = True
            guild_id = guild['id']
            del_resp = requests.delete(f"https://discord.com/api/v10/guilds/{guild_id}", headers=headers)
            if del_resp.status_code == 204:
                print(f"Deleted guild {guild_name} ({guild_id})")
            else:
                print(f"Failed to delete guild {guild_name} ({guild_id}): {del_resp.status_code} {del_resp.text}")
    if not found:
        print(f"No guilds found with the name '{guild_name}'.")

#------------------------------------------
delete_guilds("TOKEN_HERE", "SERVER_NAME_HERE")