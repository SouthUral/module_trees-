from demo_depth_first_search import tree


from hexlet import fs


import copy

def new_meta(node, value, value_txt):
    meta = copy.deepcopy(fs.get_meta(node))
    meta[value_txt] = value
    return meta


def file_owner(node, owner):
    name = fs.get_name(node)
    meta = new_meta(node, owner, 'owner')
    return fs.mkfile(name, meta)


def dir_owner(dir, children, owner):
    dir_name = fs.get_name(dir)
    dir_meta = new_meta(dir, owner, 'owner')
    return fs.mkdir(dir_name, children, dir_meta)


def change_owner(node, owner):
    if fs.is_directory(node):
        children = fs.get_children(node)
        new_children = list(map(lambda x: change_owner(x, owner), children))
        return dir_owner(node, new_children, owner)
    else:
        return file_owner(node, owner)

print(change_owner(tree, 'vova'))