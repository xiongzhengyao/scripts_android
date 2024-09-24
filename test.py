import cmd

class MyShell(cmd.Cmd):
    prompt = '(myshell) '

    def do_greet(self, arg):
        """打招呼命令"""
        if arg:
            print(f'你好, {arg}')
        else:
            print('你好!')

    def do_exit(self, arg):
        """退出命令"""
        print('再见!')
        return True  # 返回 True 表示退出命令行

    def default(self, line):
        print(f'未知命令 {line}')

if __name__ == '__main__':
    MyShell().cmdloop()