from hexlet.fs import mkdir, mkfile, is_file, get_name, get_children


tree = mkdir('/', [
     mkdir('etc', [
         mkdir('apache'),
         mkdir('nginx', [
             mkfile('.nginx.conf', {'size': 800}),
         ]),
         mkdir('.consul', [
             mkfile('.config.json', {'size': 1200}),
             mkfile('data', {'size': 8200}),
             mkfile('raft', {'size': 80}),
         ]),
      ]),
      mkfile('.hosts', {'size': 3500}),
      mkfile('resolve', {'size': 1000}),
 ])


def get_hidden_files_count(node):
    if is_file(node):
        name = get_name(node)
        if name[0] == '.':
            return 1
    else:
        children = get_children(node)
        accum_values = list(map(get_hidden_files_count, children))
        return sum(list(filter(lambda x: isinstance(x, int) ,accum_values)))


print(get_hidden_files_count(tree))