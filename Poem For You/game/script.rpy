# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳",color='#fccc00')
define m = Character("慕尧",color="#00c0ff")
define nvlm = Character(color="#c8ffc8",kind=nvl,size=30)
default love = False
# 游戏在此开始。
style big_red:
    size 40
    color "#f00"

image big hello world = Text("Hello,world!",size=40,style='big_red')


label start:
    
    play music "bg1.mp3" fadein 1.0 fadeout 1.0

    #scene big hello world

    # nvlm "曾经我很苦恼。。。"
    # nvlm "到底是选清华，还是选北大，两个好像都还不错！"
    # nvlm "后来才知道，原来，我不用烦恼这么多"
    # nvlm "再后来，需要烦恼的事情，越来越少。。。"

    # nvl clear
    # nvl show dissolve
    # nvlm "于是，一个平凡的我，过着平凡又平淡的生活，玩着乏味又无聊的游戏."
    # nvlm "听着烂大街但是着实不太喜欢的音乐，吃着口味平淡但是可以帮我活下去的食物."
    # nvlm "甚至，有时候竟会考虑，这么无聊的人生，不如就此告辞."
    # nvlm "可恨的是，连选择离开这种不平凡的选择，似乎都无法做到."
    # nvlm "啊，那就让我这样腐烂下去吧，在这个本来就已经腐烂的世界."

    # nvl clear


    scene bg title
    with fade

   

    m "不久之后，我们就抵达了牧场，也是我们俩人出生的地方。"

    e "我就是在这样的风景环绕之中成长起来的。这里的秋天格外秀美。"

    e "童年时，我们经常在牧场里玩耍，所以这里满满充斥着回忆。"

    m "嗨……唔……"

    play music "bg2.mp3" fadein 1.5

    scene bg empty
    with fade

    show girl1 at right
    with dissolve



    e "她把脸转向我，上面挂着微笑。她看起来兴致高昂。我觉得自己刚才的紧张情绪已经消散。"

    e "我得问问她！"

    show boy1 at left

    m "嗯呣……你是否可以……"

    m "你是否可以做我的视觉小说画师？"

    m "当然，不过，什么是\"视觉小说\"？"

menu:

    "是一种视频游戏。":
        jump game

    "是一种互动小说。":
        jump book

label game:

    m "是一种可以在电脑和主机上玩的视频游戏。"

    jump marry

label book:
    
    $ love = True

    m "就像一种可以在电脑和主机上阅读的互动式图书。"

    e "这很美，很像你！"

    jump marry

label marry:

    m "这很好！"

    if love:

        m "我们结婚吧"

    else:

        m "滚蛋！"

        e "好的！"
