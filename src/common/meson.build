colorize_dummy_svg = find_program('colorize-dummy-svg.py')
#colorize-dummy-folder-svg = find_program('colorize-dummy-folder-svg.py')
accent_colors_definitions_scss = meson.project_source_root() / '@0@'.format(files('accent-colors.scss.in')[0])
folder_colors_definitions_css = meson.project_source_root() / '@0@'.format(files('folder-colors.css')[0])
yaru_colors_defs_scss = meson.project_source_root() / '@0@'.format(files('yaru-colors-defs.scss')[0])

sass_utils_scss = files([
    'sass-utils.scss',
])

test('sass-utils',
    sassc,
    args: [
        files('test-sass-utils.scss'),
        '/dev/null',
    ])
