# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-25 22:27
# Description: 
# //////////////////////////////////////////////////////////////////#
# /                          _ooOoo_                               /#
# /                         o8888888o                              /#
# /                         88" . "88                              /#
# /                         (| ^_^ |)                              /#
# /                         O\  =  /O                              /#
# /                      ____/`---'\____                           /#
# /                    .'  \\|     |//  `.                         /#
# /                   /  \\|||  :  |||//  \                        /#
# /                  /  _||||| -:- |||||-  \                       /#
# /                  |   | \\\  -  /// |   |                       /#
# /                  | \_|  ''\---/''  |   |                       /#
# /                  \  .-\__  `-`  ___/-. /                       /#
# /                ___`. .'  /--.--\  `. . ___                     /#
# /              ."" '<  `.___\_<|>_/___.'  >'"".                  /#
# /            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 /#
# /            \  \ `-.   \_ __\ /__ _/   .-` /  /                 /#
# /      ========`-.____`-.___\_____/___.-`____.-'========         /#
# /                           `=---='                              /#
# /      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        /#
# /            佛祖保佑       永不宕机     永无BUG                    /#
# //////////////////////////////////////////////////////////////////#

from gateway.server import register, app
from sanic import Blueprint
from . import api_schema
from gettext import gettext as _

user_blue = Blueprint('login', url_prefix='/user')

Blueprint.group(user_blue, url_prefix='/gateway')


@user_blue.route('/login')
@register.route(api_schema.Login, summary=_('提供登录认证'),
                description=_('集中认证服务，允许用户通过用户名，手机号，邮箱登录'),
                )
async def login(request):
    return


app.blueprint(user_blue)

# @user_blue.route('/logout')
# @register.route(api_schema.Login, summary=_('提供登录认证'),
#                 description=_('集中认证服务，允许用户通过用户名，手机号，邮箱登录'),
#                 )
# def logout(request):
#     pass
