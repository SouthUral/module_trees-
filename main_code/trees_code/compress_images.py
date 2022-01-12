import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


tree = mkdir(
    'my_doc',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
        mkdir('new_dir'),
        mkfile('new_photo', {'size': 500})
    
    ],
    {'hide': False})


def compress_images(directory):
    # возвращает строку
    name_new = get_name(directory)
    # возвращает словарь
    meta_new = copy.deepcopy(get_meta(directory))
    # возвращает список
    children = get_children(directory)
    new_children = []
    for child in children:
        if is_file(child) == True:
            name_file = get_name(child)
            meta = copy.deepcopy(get_meta(child))
            meta['size'] = meta['size'] // 2
            new_children.append(mkfile(name_file, meta))
        else:
            name_dir = get_name(child)
            meta_dir = copy.deepcopy(get_meta(child))
            new_children.append(mkdir(name_dir, [], meta_dir))

    directory_new = mkdir(name_new, new_children, meta_new)
    return directory_new


    return children_is_file

print(compress_images(tree))

