# Example of Python code
def hello_world():
    print("Hello, world!  hhxx")

hello_world()


        # 个性化配置tmux（在mac环境下）
        # 主要是修改 ~/.tmux.conf 文件，如果该目录下没有该文件，则需要手动创建并编辑该文件
        touch ~/.tmux.conf
        vim ~/.tmux.conf

        # 1.解决会话窗口左下角会话名显示不全的问题

        # status-left-length 控制左侧状态栏（如会话名称显示部分）的最大字符长度。
        set -g status-left-length 40

        # status-right-length 控制右侧状态栏（如时间和日期显示部分）的最大字符长度。
        set -g status-right-length 80

        # 2.简化状态栏内容

        # 设置左侧状态栏显示会话名称，（默认状态下左下角依然会显示当前窗口的索引号，和当前窗格正在运行的shell类型，*表示当前窗格是该窗口中的活跃窗格）
        set -g status-left '#S | '

        # 设置右侧状态栏显示日期和时间
        set -g status-right ' %Y-%m-%d %H:%M:%S'

        # 3.设置状态栏更新频率
        set -g status-interval 1

        # 4.自动调整窗口大小

        # 启用窗口自动重命名
        setw -g automatic-rename on

        # 设置窗口大小为最大可用空间
        setw -g window-size largest

        # 修改并保存 ~/.tmux.conf 配置文件后，重新加载配置以使其生效
        tmux source ~/.tmux.conf

        # 如果重新加载配置后仍然不生效，考虑完全退出 tmux，然后重新启动它。确保关闭所有 tmux 会话，然后重新打开：
        tmux kill-server
        tmux new -s session_name

        # Q:session_name无法自动补全
        # A:解决方案：配置zsh的补全功能，这需要通过在.zshrc中启用补全来实现
        # 打开.zshrc文件
        vim ~/.zshrc
        # 编辑该文件
        autoload -Uz compinit
        compinit
        # 重新加载 Shell 配置:
        source ~/.zshrc

        # Q:如何退出（分离）一个会话
        # A:
        # 在会话内部时,当您处于 tmux 会话内部，并希望退出（分离）会话但不终止会话，可以使用快捷键 Ctrl+B, D（其中 Ctrl+B 是默认的前缀键，D 用于分离）。
        # 这种方式适用于直接操作会话时，快速离开但保持会话在后台运行。
        # 在会话外部时,如果您不在 tmux 会话内部，但需要从会话中分离（例如，您通过另一个终端窗口或 SSH 会话管理 tmux），则可以使用命令 tmux detach -s <session-name>。
        # 这种方法允许您从任何终端或位置控制 tmux 会话的分离，无需首先附加到会话。


