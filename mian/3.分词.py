import jieba
text = '''安德烈：“……”
这人为什么一副受到了夸赞的表情？
安德烈嗤道：“那你是不去要放弃露西的意思吗？”
白柳刚想和安德烈摊牌说他不想去这个作死活动，他胸前的硬币一震动，跳出一个任务提示：
触发支线任务真爱之船，请玩家白柳在离开塞壬镇之前完成赌约，在赌约中赢过安德烈，积分奖励100
白柳：“……..”
积分奖励居然有一百这么多！
对金钱的渴望瞬间战胜了对水的恐惧，白柳冷静地回答：“不，我去，我还一定要赢过你。”'''
seg_list = jieba.cut(text, cut_all=True)
print('全模式：', '/' .join(seg_list))
seg_list = jieba.cut(text, cut_all=False)
print('精确模式：', '/' .join(seg_list))
seg_list = jieba.cut_for_search(text )
print('搜索引擎模式：', '/' .join(seg_list))
