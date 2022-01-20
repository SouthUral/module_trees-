from hexlet.fs import get_meta, get_name, is_file, get_children

from hidden_files_count import tree

def size_file(node):
    name = get_name(node)
    if is_file(node):
        size = get_meta(node).get('size')
        return name, size
    children = get_children(node)
    children_size = list(map(size_file, children))
    size_dir = sum([n_s[1] for n_s in children_size])
    return name, size_dir


def du(node):
    result = []
    children = get_children(node)
    for child in children:
        name = get_name(child)
        if is_file(child):
            size = get_meta(child).get('size')
            result.append((name, size))
        else:
            result.append(size_file(child))
    result.sort(reverse=True, key=lambda x: x[1])
    return result



print(du(tree))



