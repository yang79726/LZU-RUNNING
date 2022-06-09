import requests as r
import random
import string
import json
import time


url_record = "http://202.201.13.66/app_running/api//record"
url_initiation = "http://202.201.13.66/app_running/api//initiation"
url_add = "http://202.201.13.66/app_running/api//add"


def post(url, data, headers=None):
    return r.post(url, data=data, headers=headers)


def record(student_id, headers=None):
    data = {
        "cardId": student_id,
        "year": "2022"
    }
    return post(url_record, data, headers=headers)


def initiation(student_id, headers=None):
    data = {
        "cardId": student_id
    }
    return post(url_initiation, data, headers=headers)


def add(student_id, trid, distance, run_time, headers=None):
    start_time = time.time()
    time.sleep(run_time*60)
    run_time *= 60
    run_min, run_sec = run_time//60, run_time % 60
    ps = run_time/distance
    ps_min, ps_sec = ps//60, ps % 60
    data = {}
    data["kh"] = student_id
    data["pbsj"] = time.strftime("%Y-%m-%d", time.localtime())
    data["kssj"] = time.strftime("%H:%M", time.localtime(start_time))
    data["jssj"] = time.strftime("%H:%M", time.localtime(start_time+run_time))
    data["pbsc"] = "%d.%02d" % (run_min, run_sec)
    data["trid"] = trid
    data["pjps"] = "%d.%02d" % (ps_min, ps_sec)
    data["lc"] = "%.2f" % distance
    return post(url_add, data, headers=headers)


def run(student_id, distance, run_time):

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; CMR-W09 Build/HUAWEICMR-W09)'
    }
    Authorization = "ST-"
    Authorization += str(random.randint(1, 65535))
    Authorization += "-"
    Authorization += ''.join(random.sample(string.ascii_letters +
                                           string.digits, 20))
    Authorization += "-cas01.example.org"
    headers["Authorization"] = Authorization
    record(student_id, headers=headers)
    r = initiation(student_id, headers=headers)
    r = json.loads(r.text)
    trid = r["data"]["trid"]
    print(r['msg'])
    r = add(student_id, trid, distance, run_time, headers=headers)
    print(json.loads(r.text)['msg'])
