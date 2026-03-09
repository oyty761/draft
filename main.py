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
    "恭喜您，获得'最佳妈妈'称号，永久有效！",
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
    "感谢您把我这个'小项目'编译成功！",
    "祝妈妈吃喝喝好，烦恼全跑！",
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
    "代码会过时，但对您的爱永不'折旧'",
    "最好的妈妈，生日快乐！",
    "爱你爱你爱你爱你爱你爱你！",
    "我长高了，您变老了，但爱没变",
    "以前您带我认识世界，现在我想带您看我的世界",
    "I LOVE YOU!",
]

# 莫兰迪色系颜色列表
morandi_colors = [
    "#E9CDD0",  # 粉雾玫瑰
    "#F0D8E1",  # 浅粉紫
    "#E3B4B8",  # 灰调干枯玫瑰
    "#D9C2C7",  # 粉灰
    "#E8D3D1",  # 藕粉
    "#F5E1E0",  # 贝壳粉
    "#B8D4DE",  # 浅灰蓝
    "#C5DDE0",  # 水蓝
    "#D4E2E6",  # 云雾白蓝
    "#AEC9CF",  # 灰青
    "#E0EBEF",  # 淡天蓝
    "#B5C9D6",  # 蓝灰
    "#D8E0C0",  # 灰绿
    "#C5D1B3",  # 茶芽绿
    "#E2E6D1",  # 米白绿
    "#B7C9A1",  # 莫兰迪绿
    "#DEDDC8",  # 浅卡其绿
    "#CBD0B0",  # 橄榄灰绿
    "#D4C2D9",  # 香芋紫
    "#E1D4E6",  # 淡紫灰
    "#C9B1CF",  # 灰紫
    "#E8DDEB",  # 奶紫
    "#D8C8DC",  # 薰衣草灰
    "#BBAEC5",  # 紫灰
    "#E7D4C4",  # 拿铁
    "#D9C8B8",  # 浅驼色
    "#F0E6D8",  # 奶油白
    "#D1B9A3",  # 灰调卡其
    "#E8D8C9",  # 杏仁色
    "#C7B09E",  # 浅陶土
    "#F8F4E1",  # 日光薄纱
    "#F5F0D1",  # 浅稻草黄
    "#EDE9D0",  # 灰调米黄
    "#EAE6C3",  # 淡橄榄黄（带一丝极微的绿调）
    "#E8E4B5",  # 柔光黄
    "#E5DFA1",  # 更明显的暖光黄
]

# 全局变量，用于记录艺术字窗口是否已关闭
art_window_closed = False


def create_safe_windows():
    """安全的单线程窗口创建"""
    windows = []
    window_count = 99  # 窗口数量
    created_count = 0  # 已创建的窗口数量

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

            window.title("你的小猪")
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

            # 更新已创建的窗口数量
            created_count += 1

            # 如果是最后一个窗口，安排显示艺术字
            if created_count == window_count:
                # 在所有弹窗创建完成后，延迟1秒显示艺术字
                root.after(1000, show_birthday_art)

            # 更新GUI并短暂延迟
            window.update()
            time.sleep(0.1)  # 给系统时间处理

        except Exception as e:
            print(f"创建窗口 {i} 失败: {e}")

    return windows


def show_birthday_art():
    """在屏幕中央显示彩色艺术字'生日快乐！'"""
    global art_window_closed

    try:
        # 创建一个新的顶级窗口用于显示艺术字
        art_window = tk.Toplevel()
        art_window.title("生日快乐")

        # 获取屏幕尺寸
        screen_width = art_window.winfo_screenwidth()
        screen_height = art_window.winfo_screenheight()

        # 设置窗口为全屏
        art_window.attributes('-fullscreen', True)

        # 设置窗口背景为透明黑色
        art_window.configure(bg='black')

        # 移除窗口边框
        art_window.overrideredirect(True)

        # 创建一个Canvas用于绘制彩色艺术字
        canvas = tk.Canvas(art_window, bg='black', highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        # 定义彩色渐变颜色
        colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0', '#118AB2', '#EF476F']

        # 绘制"生日快乐！"艺术字
        text = "生日快乐！"
        font_size = 120  # 稍微减小字号，为增加间距留出空间

        # 计算字符间距 - 增加间距因子
        spacing_factor = 1.6  # 增加间距因子，使字符之间更分散

        # 计算总文本宽度
        char_count = len(text)
        total_text_width = char_count * font_size * spacing_factor

        # 计算起始x坐标，使文本居中
        start_x = (screen_width - total_text_width) / 2 + font_size * spacing_factor / 2

        # 创建艺术字效果：彩色描边文字
        for i in range(5):
            # 为每个字符创建渐变颜色
            for j, char in enumerate(text):
                # 计算字符位置 - 使用增加间距后的位置
                x_pos = start_x + j * font_size * spacing_factor
                y_pos = screen_height // 2

                # 创建带有偏移的多个文字层，形成立体/描边效果
                offsets = [(-2, -2), (2, -2), (-2, 2), (2, 2)]
                for dx, dy in offsets:
                    canvas.create_text(
                        x_pos + dx, y_pos + dy,
                        text=char,
                        font=("Arial", font_size, "bold"),
                        fill='black',
                        anchor="center"
                    )

                # 创建主文字层
                color_idx = (j + i) % len(colors)
                canvas.create_text(
                    x_pos, y_pos,
                    text=char,
                    font=("Arial", font_size, "bold"),
                    fill=colors[color_idx],
                    anchor="center"
                )

        # 添加闪烁效果
        def twinkle():
            for _ in range(3):  # 闪烁3次
                for item in canvas.find_all():
                    if canvas.type(item) == "text":
                        # 随机改变一些文字的颜色
                        if random.random() > 0.7:
                            current_fill = canvas.itemcget(item, "fill")
                            if current_fill != 'black':  # 不要改变黑色描边
                                new_color = random.choice(colors)
                                canvas.itemconfig(item, fill=new_color)
                art_window.update()
                time.sleep(0.3)

        # 启动闪烁效果
        art_window.after(100, twinkle)

        # 3秒后关闭艺术字窗口，并显示退出提示
        def close_art_and_show_exit():
            art_window.destroy()
            art_window_closed = True
            show_exit_prompt()

        art_window.after(3000, close_art_and_show_exit)

    except Exception as e:
        print(f"创建艺术字窗口失败: {e}")
        # 如果艺术字窗口创建失败，也显示退出提示
        show_exit_prompt()


def show_exit_prompt():
    """显示退出提示窗口"""
    try:
        # 创建退出提示窗口
        exit_window = tk.Toplevel()
        exit_window.title("程序结束")

        # 设置窗口大小和位置
        window_width = 400
        window_height = 200
        screen_width = exit_window.winfo_screenwidth()
        screen_height = exit_window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        exit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        exit_window.resizable(False, False)

        # 设置窗口始终在最前面
        exit_window.attributes('-topmost', True)

        # 添加内容
        tk.Label(
            exit_window,
            text="祝福已全部送达！",
            font=("微软雅黑", 20, "bold"),
            fg="#FF6B6B"
        ).pack(pady=20)

        tk.Label(
            exit_window,
            text="点击下方按钮关闭程序",
            font=("微软雅黑", 12)
        ).pack(pady=10)

        # 添加关闭按钮
        close_button = tk.Button(
            exit_window,
            text="关闭程序",
            font=("微软雅黑", 14, "bold"),
            bg="#4ECDC4",
            fg="white",
            padx=30,
            pady=10,
            command=lambda: close_all_windows(root, exit_window)
        )
        close_button.pack(pady=20)

        # 绑定回车键也关闭程序
        exit_window.bind('<Return>', lambda e: close_all_windows(root, exit_window))

        # 设置窗口关闭按钮也关闭程序
        exit_window.protocol("WM_DELETE_WINDOW", lambda: close_all_windows(root, exit_window))

    except Exception as e:
        print(f"创建退出提示窗口失败: {e}")


def close_all_windows(main_root, exit_win):
    """关闭所有窗口并结束程序"""
    try:
        # 先销毁退出提示窗口
        if exit_win:
            exit_win.destroy()

        # 结束主循环
        main_root.quit()
        main_root.destroy()

    except Exception as e:
        print(f"关闭窗口时出错: {e}")


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