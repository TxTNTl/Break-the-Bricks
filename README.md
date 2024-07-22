# 中文版本
## 爱打篮球的坤坤
### 项目介绍
本项目纯纯是用来练手的一个项目，因此在代码规范上、运行效率上都有许多的不足。但是仍然不失为一个有趣的小游戏。
而且就算做的再烂也是我的骨肉啊>_<
### 地图编辑器
先说地图编辑器的部分
#### 基本操作
启动地图编辑器可以设置游戏的地图并保存为txt文件。地图初始将除底面外的四周全部设为屏障，避免了一个个点击的麻烦。
除此之外，对于每一个格子，鼠标左键点击的时候遵循如下的变化：空白（白色）->屏障（灰色）->可消除方块（蓝色），
而右键则是反方向操作。
#### 保存\读入操作
在下方输入框可以输入文件的名称，但省略.txt（即对于2.txt文件只需要输入2即可）
关卡和源程序必须处于同一目录下

点击读取，可以读取已保存好的关卡，这样避免了每次画地图需要重新画的问题。

点击保存，可以将已设计好的地图保存为对应的txt文件，格式要求与读取一样
### 游戏操作
点开游戏映入眼帘的是选择关卡界面，输入关卡名称并打开进入到游戏界面。

基本操作非常简单，使用a、d或者<、>来进行左右移动，基础操作与以往游戏一样，当场上没有球之后游戏结束。
### 后续更新（可优化内容）
以下写的更新不定时才会更新
#### 声音
习惯了电脑静音，所以没配音。
#### 游戏配置文件
将所有的游戏可配置项（格子的数量、篮球的速度、奖品爆率、坤坤速度）放入单独文件中进行修改
#### 性能优化
将屏幕范围拆分为多个子区块，这样避免了每次碰撞检测要把所有的方块都遍历一遍，大大降低复杂度
#### 篮球优化
奖励方块释放出来的篮球很奇怪，但是能跑

# English Version
Advance Notice: You might notice some grammar mistakes or awkward phrasing due to my limited English skills.
However, you may also find that it's not that bad.
That's because I used chatGpt to help me fix my errors.
I hope you can understand me and forgive these small mistakes.
## iKUn who loves to play basketball
### Introduction
This project is made to help me have a better understanding of computing.
Therefore, it may not follow best practices for coding conventions or runtime efficiency.
However, it often makes me feel excited as it was completely made by me.>_<
### Map Creator
Let's talk about map creator first.
#### Basic Operations
Map creator can help design a particular map and save as txt.
Initialization sets the edges (excluding the base) to Block, which avoids the need to click each one individually.
For each paddle, left-clicking changes its state as follows: Blank (white) -> Block (grey) -> Brick (blue),
while right-clicking reverses the change.
#### Save\Load Operations
Enter your file name without the .txt extension.
For example, if you want to open '2.txt', all you have to do is type in '2'.
Ensure that your maps and Python files are in the same directory.

Click 'Load' to retrieve saved game levels, which saves you time for other tasks.

Click 'Save' to store your designed map as a .txt file, with the same formatting requirements.
### Game controls
Game levels choosing interface will be your view of this game.
Typing in the name of games levels and click '打开' will step into the game interface.

Basic controls are straightforward: use 'a', 'd', '<', and '>' to move, similar to other games.
The game ends when there are no balls on the screen.
### Future Updates(Areas for improvement)
Future updates will be infrequent.
#### Sounds
I developed this while the computer was muted, so there is no sound.
#### Game Configuration File
I plan to consolidate all configurable options (such as the number of paddles, basketball speed, bonus opportunities, and iKUn speed) into a single, easily editable file.
#### Performance Optimization
Dividing the screen into multiple subsections helps reduce the number of paddles checked during collision detection.
This will help increase the runtime efficiency.
#### Basketball Optimization
As it follows the game rule, the basketballs which are released by bonuses perform very wired.
