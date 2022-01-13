from hexlet import fs

tree = fs.mkdir(
    'name_first', [
        fs.mkdir('etc', [
            fs.mkfile('bashrc'),
            fs.mkfile('consul.cfg')
    ]),
    fs.mkfile('hexlet'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])

def dfs(node):
    print(fs.get_name(node))
    if fs.is_file(node) is True:
        return
    children = fs.get_children(node)
    list(map(dfs, children))

# нужно реализовать функцию, которая меняет владельца для всего дерева
def change_owner(node, owner):
    if fs.is_file(node) is True:
        return
    children = fs.get_children(node)