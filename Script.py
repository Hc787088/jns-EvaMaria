class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {}  🙋🏻🙋🏻‍♀️
I CAN PROVIDE MOVIES IN GROUP AS WELL AS THE PERSONAL CHAT, FOR GTOUP JUST ADD ME TO GROUP AND ENJOY,
TO GET MOVIES PERSONAL TAP ON BELOW 🔎 SEARCH BUTTON.

also you can use me as file store bot, send me <code> /batch https://t.me/jns_bots/20 https://t.me/jns_bots/30 </code> . i will generate and send you special link.
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥
"""
    HELP_TXT = """𝙷𝙴𝚈  {}  🙋🏻🙋🏻‍♀️
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: <a href=https://t.me/JNS_BOTS>{}</a> 
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/jns_bots>ＪƝ⟆ ᗷ〇Ƭ⟆</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    SOURCE_TXT = """
<b>DEVS:</b>
- <a href=https://t.me/JNS_BOTS>ＪƝ⟆ ᗷ〇Ƭ⟆</a>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and I will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
 ❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    BATCHMODE1_TXT = """Help: <b>Batch mode</b>

1
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱 
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
❤️‍🔥ＪƝ⟆ ᗷ〇Ƭ⟆❤️‍🔥
"""
