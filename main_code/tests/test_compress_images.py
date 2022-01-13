from main_code.trees_code.compress_images import compress_images
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile
import copy


def test_compress_images_simple():
    tree = mkdir(
    'my_doc',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150})
    ],
    {'hide': False})
    tree_2 = {
    'name': 'my_doc',
    'type': 'directory',
    'children': [
        {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
        {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
    ],
    'meta': {'hide': False},
}
    assert compress_images(tree) == tree_2


def test_compress_images():
    tree = mkdir(
        'my documents',
        [
            mkdir('documents.jpg'),
            mkfile('avatar.jpg', {'size': 100}),
            mkfile('passport.jpg', {'size': 200}),
            mkfile('family.jpg', {'size': 150}),
            mkfile('addresses', {'size': 125}),
            mkdir('assets'),
        ],
        {'test': 'haha'},
    )

    expectation = {
        'name': 'my documents',
        'children': [
            {
                'name': 'documents.jpg',
                'children': [],
                'meta': {},
                'type': 'directory',
            },
            {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
            {'name': 'passport.jpg', 'meta': {'size': 100}, 'type': 'file'},
            {'name': 'family.jpg', 'meta': {'size': 75}, 'type': 'file'},
            {'name': 'addresses', 'meta': {'size': 125}, 'type': 'file'},
            {
                'name': 'assets',
                'children': [],
                'meta': {},
                'type': 'directory',
            },
        ],
        'meta': {'test': 'haha'},
        'type': 'directory',
    }
    assert compress_images(tree) == expectation


def test_deep_clone():
    tree = mkdir('my documents', [
        mkfile(
            'avatar.jpg',
            {'size': 100, 'attributes': {'hide': False, 'read_only': True}},
        ),
        mkdir('presentations'),
    ])
    new_tree = compress_images(tree)
    new_file = get_children(new_tree)[0]
    new_file_meta = get_meta(new_file)
    new_file_meta['attributes']['hide'] = True
    old_file = get_children(tree)[0]
    assert not get_meta(old_file)['attributes']['hide']


def test_compress_images_no_change():
    tree = mkdir('documents', [
        mkdir('presentations'),
    ])
    expected = {
        'name': 'documents',
        'type': 'directory',
        'meta': {},
        'children': [
            {
                'name': 'presentations',
                'type': 'directory',
                'meta': {},
                'children': [],
            },
        ],
    }
    assert compress_images(tree) == expected