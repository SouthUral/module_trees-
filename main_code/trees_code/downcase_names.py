from compress_images import tree


import copy


from hexlet import fs


def downcase_file_names(node):
    if fs.is_directory(node):
        name = fs.get_name(node)
        meta = copy.deepcopy(fs.get_meta(node))
        children = fs.get_children(node)
        new_children = list(map(downcase_file_names, children))
        return fs.mkdir(name, children, meta)
    else:
        name = fs.get_name(node).lower()
        meta = copy.deepcopy(fs.get_meta(node))
        return fs.mkfile(name, meta)


print(downcase_file_names(tree))