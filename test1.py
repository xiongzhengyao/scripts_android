
import cmd
# print(dir(cmd.Cmd))

class MyCmd(cmd.Cmd):
    prompt = "(xiongzhengyao) > > > "

MyCmd().cmdloop()