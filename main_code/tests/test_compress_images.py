from main_code.trees_code.compress_images import compress_images
from hexlet.fs import mkdir, mkfile


def test_compress_images():
    tree = mkdir(
    'my_doc',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150})
    ],
    {'hide': False})
    tree_2 = {
    'name': 'my documents',
    'type': 'directory',
    'children': [
        {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
        {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
    ],
    'meta': {'hide': False},
}
    assert compress_images(tree) == tree_2