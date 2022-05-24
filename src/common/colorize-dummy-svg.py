#!/usr/bin/env python3
# Copyright © 2022, Canonical Ltd
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.
# Authors:
#       Marco Trevisan <marco.trevisan@canonical.com>

import argparse
import fnmatch
import os
import sys
import cssutils

from glob import glob

# Keep this in sync with yaru-colors-defs.scss, or the input CSS in use.
DUMMY_COLORS = {
    'accent-bg-color': '#00ff01',
    'accent-active-color': '#00ff02',
    'accent-border-color': '#ff0001',
    'accent-focused-color': '#0101ff',
    'bg-color': '#ffff00',
    'border-color': '#ff00ff',
    'disabled-bg-color': '#ffff02',
    'switch-bg-color': '#ffff01',
    'check-bg-color': '#ffff03',
}

FOLDER_COLORS = {
    'folder-bg-color': '#0001ff',
}

# ---------------------------------    
    
def read_colors_replacements(css_file):
    colors_replacements = {}

    for l in css_file.readlines():
        for line in l.split('//')[0].split(';'):
            if '-yaru-' not in line:
                continue

            [named_color, color] = line.split('-yaru-', 1)[-1].split(': ')
            colors_replacements[DUMMY_COLORS[named_color]] = color
            print(named_color, color, f'(replaces {DUMMY_COLORS[named_color]})')

    return colors_replacements

def read_folder_colors_replacements(css_file, color_name):
    colors_replacements = {}

    css = cssutils.parseString(css_file.read())  
    for rule in css:
        if rule.selectorText == color_name:
            style = rule.selectorText
            for item in rule.style:
                if item.name == '-yaru-folder-bg-color':
                    key_color = item.name.split('-yaru-', 1)[-1]
                    color = item.value
                    colors_replacements[FOLDER_COLORS[key_color]] = color
                    print(color_name, color, f'(replaces color folder: {FOLDER_COLORS[key_color]})')

    return colors_replacements
    
    
def read_svg_file(svg):
    with open(svg, 'r') as f:
        contents = f.read()        
    return contents
    
    
def replace_color_name(contents, replacements, color_name):

    #contents = contents.replace('#0001ff', color)
    contents = contents.replace('folder-color', 'folder-' + color_name)
    contents = contents.replace('folders-color', 'folder-' + color_name)
    contents = contents.replace('insync-folder-color', 'insync-folder-' + color_name)
    contents = contents.replace('user-home-color', 'user-home-' + color_name)       
    
    for dummy, color in replacements.items():
        contents = contents.replace(dummy, color)
        
    return contents
        
#def replace_colors(svg, replacements, output_folder, variant):
def replace_colors(contents, replacements):

    for dummy, color in replacements.items():
        contents = contents.replace(dummy, color)

    return contents
        
def write_output(svg, output_folder, replaced_contents, variant):
    output_folder = os.path.abspath(output_folder)
    basename = os.path.basename(svg).rsplit('.', 1)[0]
    finalname = f'{basename}-{variant}.svg' if variant else f'{basename}.svg'
    output_path = os.path.join(output_folder, finalname)
    print(f'Processing {os.path.basename(svg)} => {output_path}')

    os.makedirs(output_folder, exist_ok=True)
    with open(output_path, 'w') as out:
        out.write(replaced_contents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
#    parser.add_argument('yaru_colors_defs_scss', type=argparse.FileType('r'), default=None)
    parser.add_argument('--input-scss', type=argparse.FileType('r'))
    parser.add_argument('--input-folder-css', type=argparse.FileType('r'))
    parser.add_argument('--input-file', default=None)
    parser.add_argument('--assets-path', default='.')
    parser.add_argument('--output-folder', default='.')
    parser.add_argument('--variant', default=None)
    parser.add_argument('--filter', action='append', default=[])
    parser.add_argument('--exclude', action='append', default=[])
    parser.add_argument('--no-accent', default=False)
    parser.add_argument('--folder-color', default=None)
         
    args = parser.parse_args()
    if args.input_scss:
        replacements = read_colors_replacements(args.input_scss)
    if args.input_folder_css:
        folder_replacements = read_folder_colors_replacements(args.input_folder_css, args.folder_color)
    variant = None if args.variant == 'default' else args.variant

    
    print(f'DEBUG: COLORIZED: {args.input_file} => {args.output_folder}')
    
    if args.input_file:
        file = read_svg_file(args.input_file)
        
        if args.folder_color:
            file = replace_color_name(file, folder_replacements, args.folder_color)
        
        if not args.input_scss:
            write_output(args.input_file, args.output_folder, file, variant)
            sys.exit()
        
        file = replace_colors(file, replacements)
        write_output(args.input_file, args.output_folder, file, variant)
    else:
        for svg in glob(os.path.join(os.path.abspath(args.assets_path), '*.svg')):
            if [fl for fl in args.exclude if fnmatch.fnmatch(svg, fl)]:
                continue

            if args.filter and not [fl for fl in args.filter if fnmatch.fnmatch(svg, fl)]:
                continue
            file = read_svg_file(svg)
            if args.folder_color:
                file =  replace_color_name(file, folder_replacements, args.folder_color)
            if not args.input_scss:
                write_output(args.input_file, args.output_folder, file, variant)
                break
            file = replace_colors(file, replacements, args.output_folder, variant)
            write_output(svg, args.output_folder, file, variant)
            
