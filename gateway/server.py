# -*- coding: utf-8 -*
# Author: weijia shan
# Email: wjshan@goodoss.com
# Time: 2020-07-24 15:05
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

import os

from sanic.log import logger
from sanic.response import json
from base_plate import get_app

from base_plate import Config
from base_plate.tools import cpu_count

config = Config()
app, register = get_app(config)



def run():
    from . import controllers
    app.run('0.0.0.0', 8000, workers=config.get('works') or cpu_count())


if __name__ == "__main__":
    run()
