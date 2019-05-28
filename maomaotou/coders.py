#!/usr/bin/env python
# *-* coding:utf8 *-*
import datetime


weeks = ["日", "一", "二", "三", "四", "五", "六"]
directions = ["北方", "东北方", "东方", "东南方", "南方", "西南方", "西方", "西北方"]
drinks = ["水", "茶", "红茶", "绿茶", "咖啡", "奶茶", "可乐", "鲜奶", "豆奶", "果汁", "果味汽水", "苏打水", "运动饮料", "酸奶", "酒"]
tools = ["Eclipse写程序", "MSOffice写文档", "记事本写程序", "Windows8", "Linux", "MacOS", "IE", "Android设备", "iOS设备"]
var_names = ["jieguo", "huodong", "pay", "expire", "zhangdan", "every", "free", "i1", "a", "virtual", "ad", "spider", "mima", "pass", "ui"]
activities = [
    {"name": "写单元测试", "good": "写单元测试将减少出错", "bad": "写单元测试会降低你的开发效率"},
    {"name": "洗澡", "good": "你几天没洗澡了？", "bad": "会把设计方面的灵感洗掉", "weekend": True},
    {"name": "锻炼一下身体", "good": "", "bad": "能量没消耗多少，吃得却更多", "weekend": True},
    {"name": "抽烟", "good": "抽烟有利于提神，增加思维敏捷", "bad": "除非你活够了，死得早点没关系", "weekend": True},
    {"name": "白天上线", "good": "今天白天上线是安全的", "bad": "可能导致灾难性后果"},
    {"name": "重构", "good": "代码质量得到提高", "bad": "你很有可能会陷入泥潭"},
    {"name": "使用%t", "good": "你看起来更有品位", "bad": "别人会觉得你在装逼"},
    {"name": "跳槽", "good": "该放手时就放手", "bad": "鉴于当前的经济形势，你的下一份工作未必比现在强"},
    {"name": "招人", "good": "你面前这位有成为牛人的潜质", "bad": "这人会写程序吗？"},
    {"name": "面试", "good": "面试官今天心情很好", "bad": "面试官不爽，会拿你出气"},
    {"name": "提交辞职申请", "good": "公司找到了一个比你更能干更便宜的家伙，巴不得你赶快滚蛋", "bad": "鉴于当前的经济形势，你的下一份工作未必比现在强"},
    {"name": "申请加薪", "good": "老板今天心情很好", "bad": "公司正在考虑裁员"},
    {"name": "晚上加班", "good": "晚上是程序员精神最好的时候", "bad": "", "weekend": True},
    {"name": "在妹子面前吹牛", "good": "改善你矮穷挫的形象", "bad": "会被识破", "weekend": True},
    {"name": "撸管", "good": "避免缓冲区溢出", "bad": "强撸灰飞烟灭", "weekend": True},
    {"name": "浏览成人网站", "good": "重拾对生活的信心", "bad": "你会心神不宁", "weekend": True},
    {"name": "命名变量\"%v\"", "good": "", "bad": ""},
    {"name": "写超过%l行的方法", "good": "你的代码组织的很好，长一点没关系", "bad": "你的代码将混乱不堪，你自己都看不懂"},
    {"name": "提交代码", "good": "遇到冲突的几率是最低的", "bad": "你遇到的一大堆冲突会让你觉得自己是不是时间穿越了"},
    {"name": "代码复审", "good": "发现重要问题的几率大大增加", "bad": "你什么问题都发现不了，白白浪费时间"},
    {"name": "开会", "good": "写代码之余放松一下打个盹，有益健康", "bad": "小心被扣屎盆子背黑锅"},
    {"name": "打DOTA", "good": "你将有如神助", "bad": "你会被虐的很惨", "weekend": True},
    {"name": "晚上上线", "good": "晚上是程序员精神最好的时候", "bad": "你白天已经筋疲力尽了"},
    {"name": "修复BUG", "good": "你今天对BUG的嗅觉大大提高", "bad": "新产生的BUG将比修复的更多"},
    {"name": "设计评审", "good": "设计评审会议将变成头脑风暴", "bad": "人人筋疲力尽，评审就这么过了"},
    {"name": "需求评审", "good": "", "bad": ""},
    {"name": "上微博", "good": "今天发生的事不能错过", "bad": "今天的微博充满负能量", "weekend": True},
    {"name": "上AB站", "good": "还需要理由吗？", "bad": "满屏兄贵亮瞎你的眼", "weekend": True},
    {"name": "搞数据分析", "good": "今天库很快任何代码都能跑出来", "bad": "错误百出，数对不上", "weekend": True}
]
specials = [
    {"date": 20200214, "name":"待在男（女）友身边", "bad":"脱团火葬场，入团保平安。"}
]


def random(dayseed, indexseed):
    '''本程序中的“随机”都是伪随机概念，以当前的天为种子'''
    n = dayseed % 11117
    for x in range(100 + indexseed):
        n = n * n
        n = n % 11117  # 11117 是个质数
    return n


def get_today_string(today):
    return "今天是%d年%d月%d日 星期%s" % (today.year, today.month, today.day, weeks[(today.weekday()+1) % 7])

def star(num):
    return "★" * num +"☆" * (5 - num)

def is_weekend(today):
    return today.weekday() == 5 or today.weekday() == 6


def today_activity(today, actions):
    '''周末的话，只留下 weekend = true 的事件'''
    if is_weekend(today):
        return [x for x in actions if x.get('weekend')]
    return actions


def pick_todays_luck(today, iday):
    good = []
    bad = []
    _activities = today_activity(today, activities)
    num_good = random(iday, 98) % 3 + 2
    num_bad = random(iday, 87) % 3 + 2
    event_list = pick_random(_activities, num_good + num_bad, iday)
    for i in range(num_good):
        event = parse(event_list[i], iday)
        good.append('%s %s' % (event['name'], event['good']))
    for i in range(num_bad):
        event = parse(event_list[num_good + i], iday)
        bad.append('%s %s' % (event['name'], event['bad']))
    for event in specials:
        if iday == event['date']:
            if event.get('good'):
                good.append('%s %s' % (event['name'], event['good']))
            if event.get('bad'):
                bad.append('%s %s' % (event['name'], event['bad']))
    return good, bad


def pick_random(action, size, iday):
    result = action.copy()
    for j in range(len(action) - size):
        index = random(iday, j) % len(result)
        del result[index]
    return result


def parse(event, iday):
    result = event.copy()
    if result['name'].find('%v') != -1:
        result['name'] = result['name'].replace('%v', var_names[random(iday, 12) % len(var_names)])
    if result['name'].find('%t') != -1:
        result['name'] = result['name'].replace('%t', tools[random(iday, 11) % len(tools)])
    if result['name'].find('%l') != -1:
        result['name'] = result['name'].replace('%l', str(random(iday, 12) % 247 + 30))
    return result


def today_luck():
    today = datetime.date.today()
    iday = today.year * 10000 + today.month * 100 + today.day
    today_string = get_today_string(today)
    good, bad = pick_todays_luck(today, iday)
    good_string = '宜：\n' + '\n'.join(good)
    bad_string = '不宜：\n' + '\n'.join(bad)
    direction = '座位朝向：面向%s写程序，BUG 最少。' % directions[random(iday, 2) % len(directions)]
    drink = '今日宜饮：%s' % '，'.join(pick_random(drinks, 2, iday))
    goddes = '女神亲近指数：%s' % star(random(iday, 6) % 5 + 1)
    return '\n'.join([today_string, good_string, bad_string, direction, drink, goddes])


if __name__ == '__main__':
    print(today_luck())
