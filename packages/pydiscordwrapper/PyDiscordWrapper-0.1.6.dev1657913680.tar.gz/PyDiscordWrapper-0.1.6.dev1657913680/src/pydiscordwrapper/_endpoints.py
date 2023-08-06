from ._urls import API_BASE_URL

CURRENT_USER = API_BASE_URL + "/users/@me"
CURRENT_USER_GUILDS = API_BASE_URL + "/users/@me/guilds"
CURRENT_USER_GUILD_MEMBER = API_BASE_URL + "/users/@me/guilds/{guild_id}/member"

GUILD = API_BASE_URL + "/guilds/{guild_id}"
GUILD_CHANNELS = GUILD + "/channels"
GUILD_MEMBERS = GUILD + "/members"
GUILD_ROLES = GUILD + "/roles"

CDN_URL = "https://cdn.discordapp.com"
GUILD_ICON_CDN = CDN_URL + "/icons/{guild_id}/{icon_hash}.jpg"
