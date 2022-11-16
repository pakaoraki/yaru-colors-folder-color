project('Yaru',
        version: '22.10.3',
        meson_version: '>= 0.59',
        license : ['GPL3', 'CC BY-SA 4.0'],
        default_options: ['prefix=/usr'])

fs = import('fs')
gnome = import('gnome')

python = find_program('python3')
sassc = find_program('sassc')

subdir('common')

components = [
  'gtk',
  'icons',
]

enabled_accent_colors = get_option('accent-colors')
enabled_folder_colors = get_option('folder-colors')

foreach component: components
  if not get_option(component)
    message('skip component ' + component)
    continue
  endif

  message('build component ' + component)
  subdir(component)

endforeach
