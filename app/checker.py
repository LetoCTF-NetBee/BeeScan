from flask import Blueprint, json, render_template, request

check = Blueprint('check', __name__)


@check.route('/check', methods=['POST'])
def check_url():
    print(request.form)

    to_return = {
        'msg': '???',
        'stats': {}
    }

    if 'url' not in request.form or len(request.form['url']) == 0:
        to_return['msg'] = 'Не указан URL сайта'
        return to_return

    url = request.form['url']

    # 1) впихнуть всякие магические штучки *poofff*
    # 2) ????
    # 3) запихать данные в CheckData
    # 4) profit
    # is_safe, ssl_ok, ... = magic_stuff(url)

    check_data = CheckData(url, False)

    if check_data.is_safe:
        to_return['msg'] = 'Сайт безопасен'
    else:
        to_return['msg'] = 'Сайт возможно является фишинговым'

    to_return['stats'] = check_data.__dict__

    print(to_return)

    return to_return


class CheckData:
    def __init__(self, url: str, is_safe: bool):
        self.url = url
        self.is_safe = is_safe
        self.ssl_safe = True
        self.reg_safe = False
        self.test1 = False
        self.test2 = True
