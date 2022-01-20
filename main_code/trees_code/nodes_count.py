from hexlet.fs import is_directory, is_file, get_children


from compress_images import tree


def get_count_nodes(node):
    if is_file(node):
        return 1
    children = get_children(node)
    descendant_counts = list(map(get_count_nodes, children))
    return 1 + sum(descendant_counts)


print(get_count_nodes(tree))