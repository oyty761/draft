import tkinter as tk
import random
import time
import platform

# 弹窗文字列表
messages = [
    "妈！这是我写的程序，牛不牛",
    "本程序由您最爱的女儿（用AI)独家编码！",
    "身体健康最重要！",
    "事事顺心，万事如意",
    "岁岁无忧，喜乐常伴",
    "生日快乐！！！",
    "心宽体健，万事无忧",
    "永远爱你",
    "时光温柔，万事胜意",
    "快乐每一天！",
    "能吃能睡，快乐翻倍",
    "工作轻松不加班！",
    "永远年轻，永远快乐",
    "是谁的妈妈在过生日？哦，是我的！",
    "恭喜您，获得“最佳妈妈”称号，永久有效！",
    "本程序由您最爱的女儿（用AI)独家编码！",
    "下辈子，还要当你的小孩",
    "你是我的榜样！",
    "正在加载10000000%的爱……",
    "走过路过，妈妈的生日不能错过！",
    "对着蜡烛许个愿吧！",
    "Hello!大寿星！",
    "马到成功，马上暴富！",
    "叮！您的生日限定款祝福上线啦！",
    "母爱无BUG，运行永不报错！",
    "感谢您把我这个‘小项目’编译成功！",
    "祝妈妈吃好喝好，烦恼全跑！",
    "正在为您加载1000000%的幸福……",
    "生日蛋糕留一口给我哦",
    "您负责快乐健康，我负责……帮你吃蛋糕",
    "我长高了，您变老了，但爱没变",
    "以前您带我认识世界，现在我想带您看我的世界",
    "I LOVE YOU!",
    "爱你一万年",
    "妈妈妈妈妈妈",
    "别问，问就是爱你",
    "妈妈，我爱你，略略略~",
    "嘿嘿我马上就回家",
    "I LOVE YOU!",
    "代码会过时，但对您的爱永不‘折旧’",
    "最好的妈妈，生日快乐！",
    "爱你爱你爱你爱你爱你爱你！",
    "我长高了，您变老了，但爱没变",
    "以前您带我认识世界，现在我想带您看我的世界",
    "I LOVE YOU!",
]

# 莫兰迪色系颜色列表
morandi_colors = [
    "#E9CDD0", # 粉雾玫瑰
    "#F0D8E1", # 浅粉紫
    "#E3B4B8", # 灰调干枯玫瑰
    "#D9C2C7", # 粉灰
    "#E8D3D1", # 藕粉
    "#F5E1E0", # 贝壳粉
    "#B8D4DE", # 浅灰蓝
    "#C5DDE0", # 水蓝
    "#D4E2E6", # 云雾白蓝
    "#AEC9CF", # 灰青
    "#E0EBEF", # 淡天蓝
    "#B5C9D6", # 蓝灰
    "#D8E0C0",  # 灰绿
    "#C5D1B3",  # 茶芽绿
    "#E2E6D1",  # 米白绿
    "#B7C9A1",  # 莫兰迪绿
    "#DEDDC8",  # 浅卡其绿
    "#CBD0B0",  # 橄榄灰绿
    "#D4C2D9", # 香芋紫
    "#E1D4E6", # 淡紫灰
    "#C9B1CF", # 灰紫
    "#E8DDEB", # 奶紫
    "#D8C8DC", # 薰衣草灰
    "#BBAEC5", # 紫灰
    "#E7D4C4", # 拿铁
    "#D9C8B8", # 浅驼色
    "#F0E6D8", # 奶油白
    "#D1B9A3", # 灰调卡其
    "#E8D8C9", # 杏仁色
    "#C7B09E", # 浅陶土
    "#F8F4E1", # 日光薄纱
    "#F5F0D1", # 浅稻草黄
    "#EDE9D0", # 灰调米黄
    "#EAE6C3", # 淡橄榄黄（带一丝极微的绿调）
    "#E8E4B5", # 柔光黄
    "#E5DFA1", # 更明显的暖光黄
]


def create_safe_windows():
    """安全的单线程窗口创建"""
    windows = []
    window_count = 99  # 窗口数量

    for i in range(window_count):
        try:
            window = tk.Toplevel()  # 使用Toplevel而不是Tk
            # 获取屏幕尺寸
            width = window.winfo_screenwidth()
            height = window.winfo_screenheight()

            # 生成横向长方形的尺寸(宽度>高度)
            win_width = random.randint(200, 400)  # 宽度范围200-400
            win_height = random.randint(80, 150)  # 高度范围80-150，确保小于宽度

            # 确保窗口不会超出屏幕
            x = random.randrange(0, width - win_width)
            y = random.randrange(0, height - win_height)

            window.title("亲爱的")
            window.geometry(f"{win_width}x{win_height}+{x}+{y}")

            # 随机选择莫兰迪色系背景
            bg_color = random.choice(morandi_colors)
            msg = random.choice(messages)

            # 根据操作系统选择合适的字体
            system = platform.system()
            if system == "Darwin":  # macOS
                chinese_font = "STXingkai"
            elif system == "Windows":
                chinese_font = "行楷"  # Windows行楷
            else:  # Linux或其他
                chinese_font = "WenQuanYi Zen Hei"  # 文泉驿正黑

            # 动态调整字体大小，基于窗口尺寸
            # 使用窗口宽度和高度的较小值来计算基础字体大小
            base_size = min(win_width, win_height)
            # 字体大小随窗口尺寸变化，但保持在合理范围内
            font_size = max(20, min(30, base_size // 20))

            label = tk.Label(window,
                             text=msg,
                             bg=bg_color,  # 随机莫兰迪色背景
                             fg="black",  # 黑色文字
                             font=(chinese_font, font_size),  # 动态字体大小
                             wraplength=win_width - 20,  # 自动换行，适应横向窗口
                             justify="center"  # 文字居中
                             )
            label.pack(fill="both", expand=True)

            # 设置窗口在10-30秒后自动关闭
            window.after(random.randint(10000, 30000), window.destroy)
            windows.append(window)

            # 更新GUI并短暂延迟
            window.update()
            time.sleep(0.1)  # 给系统时间处理

        except Exception as e:
            print(f"创建窗口 {i} 失败: {e}")

    return windows


# 创建主窗口但不显示
root = tk.Tk()
root.withdraw()

# 创建窗口
windows = create_safe_windows()

# 启动主循环
try:
    root.mainloop()
except Exception as e:
    print(f"主循环错误: {e}")