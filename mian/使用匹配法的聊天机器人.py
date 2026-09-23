import re
import random
from datetime import datetime

# 定义聊天机器人的响应规则
RESPONSE_RULES = {
    r'你好|嗨|hello|hi': [
        "你好！我是聊天机器人小智，有什么可以帮您的吗？",
        "嗨！很高兴见到你！",
        "你好呀！今天过得怎么样？"
    ],
    r'再见|拜拜|exit|quit|停止': [
        "再见！期待下次聊天！",
        "拜拜，祝你有个愉快的一天！",
        "下次再聊哦！"
    ],
    r'谢谢|感谢|thx|thanks': [
        "不客气！随时为您服务！",
        "很高兴能帮到您！",
        "这是我的荣幸！"
    ],
    r'名字|称呼|你叫': [
        "我是聊天机器人小智！",
        "大家都叫我小智，你也可以这样叫我哦！",
        "我是智能聊天助手小智，很高兴认识你！"
    ],
    r'时间|几点|日期|今天': [
        "让我看看时间...",
        "稍等，我看下时钟..."
    ],
    r'天气|气温|温度|下雨|晴天': [
        "抱歉，我暂时无法获取实时天气数据。",
        "你可以告诉我你所在的城市，我帮你查查天气？",
        "我还没有连接天气服务哦。"
    ],
    r'笑话|讲个笑话|搞笑': [
        "为什么程序员分不清万圣节和圣诞节？\n因为 Oct 31 == Dec 25！",
        "程序员最讨厌的动物是什么？\nBug！",
        "我有个关于栈的笑话...\n算了，可能太深奥了。"
    ],
    r'你.*(会|能)': [
        "我可以陪你聊天、回答简单问题和讲笑话！",
        "我的能力包括：回答问题、讲笑话、聊日常话题",
        "目前我还在学习阶段，会的东西不多，但我会努力的！"
    ],
    r'.*': [  # 默认响应
        "听起来很有趣，能多说点吗？",
        "我不是很明白，能换种方式说吗？",
        "这个话题我不太熟悉，我们可以聊点别的吗？",
        "嗯... 然后呢？"
    ]
}


class SimpleChatbot:
    def __init__(self, name="小智"):
        self.name = name
        self.responses = RESPONSE_RULES

    def get_response(self, user_input):
        """根据用户输入获取响应"""
        user_input = user_input.lower().strip()

        # 特殊处理时间查询
        if re.search(r'时间|几点|日期|今天', user_input):
            now = datetime.now()
            return f"现在是 {now.strftime('%Y年%m月%d日 %H:%M:%S')}"

        # 检查所有规则
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)

        # 理论上不会执行到这里，因为有默认规则
        return random.choice(self.responses[r'.*'])

    def start_chat(self):
        """启动聊天会话"""
        print(f"{self.name}: 你好！我是聊天机器人{self.name}，输入'退出'可以随时结束聊天。")

        while True:
            user_input = input("你: ")

            if re.search(r'退出|再见|拜拜|exit|quit', user_input):
                print(f"{self.name}: {random.choice(self.responses[r'再见|拜拜|exit|quit|停止'])}")
                break

            response = self.get_response(user_input)
            print(f"{self.name}: {response}")


# 创建并启动聊天机器人
if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.start_chat()