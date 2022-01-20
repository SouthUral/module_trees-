from hexlet.fs import get_meta, get_children, get_name, is_directory, flatten, mkdir, mkfile


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf'),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkdir('data'),
        ]),
    ]),
    mkdir('logs'),
    mkfile('hosts'),
])


def find_empty_dir_path(node):
    name = get_name(node)
    children = get_children(node)
    if len(children) == 0:
        return name
    dir_names = filter(lambda x: is_directory(x), children)
    emty_dir_names = map(lambda x: find_empty_dir_path(x), dir_names)
    return flatten(emty_dir_names)


def find_empty_dir_path_v2(tree):

    def walk(node, depth):
        name = get_name(node)
        children = get_children(node)
        if len(children) == 0:
            return name
        if depth == 2:
            return []
        dir_path = filter(lambda x: is_directory(x), children)
        output = map(lambda child: walk(child, depth + 1), dir_path)
        return flatten(output)

    return walk(tree, 0)

print(find_empty_dir_path_v2(tree))