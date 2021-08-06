from flask import Blueprint, json, render_template, request
from . import web_checkers

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

    check_data = CheckData(url)

    if check_data.error:
        to_return['msg'] = 'Ошибка. Сайт не найден'
        return to_return

    if check_data.is_safe:
        to_return['msg'] = 'Сайт безопасен'
    else:
        to_return['msg'] = 'Есть опасность фишинга'

    to_return['stats'] = check_data.__dict__

    print(to_return)

    return to_return


class CheckData:
    def __init__(self, url: str):
        self.url = url
        self.score = 0
        self.error = False

        try:
            self.ssl_safe = web_checkers.checkSSL(url)[0]
        except:
            self.ssl_safe = False
            self.error = True
            return

        try:
            self.no_redirect, self.redirect_to = web_checkers.testRedirection(
                url)
        except:
            self.no_redirect, self.redirect_to = False, ''

        try:
            self.reg_time_ok, self.reg_time_days = web_checkers.checkValidDate(
                url, 14)
        except:
            self.reg_time_ok, self.reg_time_days = False, 0

        try:
            self.not_in_blacklist = web_checkers.testBlackList(url)[0]
        except:
            self.not_in_blacklist = False

        try:
            self.trustued_site = web_checkers.testSecurity(url)[0]
        except:
            self.trustued_site = False

        try:
            self.not_in_openphish = web_checkers.scanDatabaseOpenphish(url)[0]
        except:
            self.not_in_openphish = False

        try:
            self.domain_low, self.domain_lvl = web_checkers.domain(url)
        except:
            self.domain_low, self.domain_lvl = False, 0

        try:
            self.no_mimic = not web_checkers.findDubl(url)[0]
        except:
            self.no_mimic = False

        if self.ssl_safe:
            self.score += 5
        if self.no_redirect:
            self.score += 1
        if self.reg_time_ok:
            self.score += 5
        if self.not_in_blacklist:
            self.score += 5
        if self.trustued_site:
            self.score += 1
        if self.not_in_openphish:
            self.score += 5
        if self.domain_low:
            self.score += 1
        # if self.no_mimic:
        #     self.score += 5

        if self.score >= 15:
            self.is_safe = True
        else:
            self.is_safe = False
