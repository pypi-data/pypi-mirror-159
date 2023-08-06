import traceback
import nonebot.adapters.onebot.v11
from loguru import logger
from nonebot import get_bot, on_command, on_message, get_driver
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment,MessageEvent,Bot,ActionFailed,GroupMessageEvent,PrivateMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent
from nonebot.log import logger
from .publicAPI import get_nation_list,get_ship_name,get_ship_byName
from .wws_info import get_AccountInfo
from .wws_recent import get_RecentInfo
from .wws_bind import set_BindInfo,get_BindInfo,change_BindInfo,set_special_BindInfo,delete_BindInfo
from .wws_ship import get_ShipInfo,get_ShipInfoRecent,ShipSecletProcess
from .wws_clan import get_ClanInfo,ClanSecletProcess
from .wws_record import get_record
from .wws_shiprank import get_ShipRank
from .data_source import command_list
from .utils import find_and_replace_keywords,DailyNumberLimiter,FreqLimiter
from nonebot_plugin_htmlrender import text_to_pic
from pathlib import Path
import httpx
import json
import asyncio
import re
import html
from nonebot import require
scheduler = require("nonebot_plugin_apscheduler").scheduler

_max = 100
EXCEED_NOTICE = f'您今天已经冲过{_max}次了，请明早5点后再来！'
_nlmt = DailyNumberLimiter(_max)
_flmt = FreqLimiter(3)
__version__ = '0.3.3.1'
dir_path = Path(__file__).parent
template_path = dir_path / "template"

bot = on_command("wws", block=False, aliases={"WWS"},priority=5)
bot_listen = on_message(priority=5,block=False)
bot_checkversion = on_command("wws 检查更新",priority=5,block=False)
driver = get_driver()

@bot.handle()
async def selet_command(ev:MessageEvent, matchmsg: Message = CommandArg()):
    try:
        server_type = None
        if isinstance(ev, PrivateMessageEvent) and (driver.config.private or str(ev.user_id) in driver.config.superusers):       #私聊事件,superusers默认不受影响
            server_type = 'QQ'
        elif isinstance(ev, GroupMessageEvent) and driver.config.group and ev.group_id not in driver.config.ban_group_list:         #群聊事件
            server_type = 'QQ'
        elif isinstance(ev, GuildMessageEvent) and driver.config.channel:       #频道事件
            if driver.config.all_channel or ev.channel_id in driver.config.channel_list:
                server_type = 'QQ_CHANNEL'
            else:
                return
        else:
            return
        msg = ''
        qqid = ev.user_id
        select_command,replace_name = None,None
        if not _nlmt.check(qqid):
            await bot.send(EXCEED_NOTICE, at_sender=True)
            return
        if not _flmt.check(qqid):
            await bot.send('您冲得太快了，请稍候再冲', at_sender=True)
            return
        _flmt.start_cd(qqid)
        _nlmt.increase(qqid) 
        searchtag = html.unescape(str(matchmsg)).strip()
        if not searchtag:
            await bot.send("请发送wws help查看相关帮助")
            return
        match = re.search(r"(\(|（)(.*?)(\)|）)",searchtag)
        if match:
            replace_name = match.group(2)
            search_list = searchtag.replace(match.group(0),'').split()
        else:
            search_list = searchtag.split()
        select_command,search_list = await find_and_replace_keywords(search_list,command_list)
        if not select_command:
            if replace_name:
                search_list.append(replace_name)
            msg = await get_AccountInfo(server_type,qqid,search_list)
        elif select_command == 'ship':
            select_command = None
            select_command,search_list = await find_and_replace_keywords(search_list,command_list)         #第二次匹配
            if replace_name:
                search_list.append(replace_name)
            if not select_command:
                msg = await get_ShipInfo(server_type,qqid,search_list,bot)
            elif select_command == 'recent':
                msg = await get_ShipInfoRecent(server_type,qqid,search_list,bot)
            else:
                msg = '看不懂指令QAQ'
        elif select_command == 'recent':
            select_command = None
            select_command,search_list = await find_and_replace_keywords(search_list,command_list)             #第二次匹配
            if replace_name:
                search_list.append(replace_name)
            if not select_command:
                msg = await get_RecentInfo(server_type,qqid,search_list)
            elif select_command == 'ship':
                msg = await get_ShipInfoRecent(server_type,qqid,search_list,bot)
            else:
                msg = '看不懂指令QAQ'
        elif select_command == 'clan':
            select_command = None
            select_command,search_list = await find_and_replace_keywords(search_list,command_list) 
            if not select_command:                  #查询公会详情信息
                msg = await get_ClanInfo(server_type,qqid,search_list,bot)
            elif select_command == 'record':        #查询公会历史记录
                msg = await get_record(server_type,qqid,search_list,"clan")
        elif select_command == 'record':
            select_command = None
            select_command,search_list = await find_and_replace_keywords(search_list,command_list) 
            if replace_name:
                search_list.append(replace_name)
            if not select_command:                  #查询个人历史记录
                msg = await get_record(server_type,qqid,search_list,"personal")
            elif select_command == 'clan':          #查询公会历史记录
                msg = await get_record(server_type,qqid,search_list,"clan")
        elif select_command == 'ship_rank':
            msg = await get_ShipRank(qqid,search_list,bot)   
        elif select_command == 'bind':
            if replace_name:
                search_list.append(replace_name)
            msg = await set_BindInfo(server_type,qqid,search_list)
        elif select_command == 'special_bind':
            msg = await set_special_BindInfo(server_type,qqid,search_list)
        elif select_command == 'bindlist':
            msg = await get_BindInfo(server_type,qqid,search_list)
        elif select_command == 'changebind':
            msg = await change_BindInfo(server_type,qqid,search_list)
        elif select_command == 'delete_bind':
            msg = await delete_BindInfo(server_type,qqid,search_list)
        elif select_command == 'searchship':
            msg = await get_ship_name(search_list)
        elif select_command == 'help':
            msg = await send_bot_help()
        else:
            msg = '看不懂指令QAQ'
        if msg:
            if isinstance(msg,str):
                await bot.send(msg)
                return
            else:
                await bot.send(MessageSegment.image(msg))
                return
        else:
            await bot.send('呜呜呜发生了错误，可能是网络问题，如果过段时间不能恢复请联系麻麻哦~')
            return
    except ActionFailed:
        logger.warning(traceback.format_exc())
        try:
            await bot.send('发不出图片，可能被风控了QAQ')
        except Exception:
            pass
        return
    except Exception:
        logger.error(traceback.format_exc())
        await bot.finish('呜呜呜发生了错误，可能是网络问题，如果过段时间不能恢复请联系麻麻哦~')
                
async def send_bot_help():
    try:
        url = 'https://benx1n.oss-cn-beijing.aliyuncs.com/version.json'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10)
            result = json.loads(resp.text)
        latest_version = result['latest_version']
        url = 'https://benx1n.oss-cn-beijing.aliyuncs.com/wws_help.txt'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10)
            result = resp.text
        result = f'''帮助列表                                                当前版本{__version__}  最新版本{latest_version}\n{result}'''
        img = await text_to_pic(text = result,css_path = str(template_path/"text-help.css"), width = 800)
        return img
    except Exception:
        logger.warning(traceback.format_exc())
        return 'wuwuwu出了点问题，请联系麻麻解决'
    
@bot_listen.handle()
async def change_select_state(ev:MessageEvent):
    try:
        msg = str(ev.message)
        qqid = ev.user_id
        if ShipSecletProcess[qqid].SelectList and str(msg).isdigit():
            if int(msg) <= len( ShipSecletProcess[qqid].SelectList):
                ShipSecletProcess[qqid] = ShipSecletProcess[qqid]._replace(state = True)
                ShipSecletProcess[qqid] = ShipSecletProcess[qqid]._replace(SlectIndex = int(msg))
            else:
                await bot.send('请选择列表中的序号哦~')
        if ClanSecletProcess[qqid].SelectList and str(msg).isdigit():
            if int(msg) <= len( ClanSecletProcess[qqid].SelectList):
                ClanSecletProcess[qqid] = ClanSecletProcess[qqid]._replace(state = True)
                ClanSecletProcess[qqid] = ClanSecletProcess[qqid]._replace(SlectIndex = int(msg))
            else:
                await bot.send(ev,'请选择列表中的序号哦~') 
    except Exception:
        logger.warning(traceback.format_exc())
        return

@bot_checkversion.handle()
async def check_version():
    try:
        bot = get_bot()
        url = 'https://benx1n.oss-cn-beijing.aliyuncs.com/version.json'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10)
            result = json.loads(resp.text)
        superid = get_driver().config.superusers
        match,msg = False,f'发现新版本'
        for each in result['data']:
            if each['version'] > __version__:
                match = True
                msg += f"\n{each['date']} v{each['version']}\n"
                for i in each['description']:
                    msg += f"{i}\n"
        if match:
            for each in superid:
                await bot.send_private_msg(user_id=int(each),message=msg)
            try:
                await bot_checkversion.send(msg)
            except Exception:
                return
        return
    except Exception:
        logger.warning(traceback.format_exc())
        return
        
@driver.on_startup
async def startup():
    try:
        loop = asyncio.get_running_loop()
        url = 'https://benx1n.oss-cn-beijing.aliyuncs.com/template_Hikari/template.json'
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=20)
            result = resp.json()
            for each in result:
                for name, url in each.items():
                    async with httpx.AsyncClient() as client:
                        resp = resp = await client.get(url, timeout=20)
                        with open(template_path/name , "wb+") as file:
                            file.write(resp.content)
    except Exception:
        logger.error(traceback.format_exc())
        return    
    
scheduler.add_job(
    check_version,
    "cron",
    hour = 12,
)
scheduler.add_job(
    startup,
    "cron",
    hour = 4
)