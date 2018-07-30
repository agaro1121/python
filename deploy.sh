#!/usr/bin/env bash

# cp ~/gitext/python/Github.py /home/hierro/.local/share/albert/org.albert.extension.python/modules/
rm -rf $HOME/.local/share/albert/org.albert.extension.python/modules/Github
cp -rf ~/gitext/python/Github/ $HOME/.local/share/albert/org.albert.extension.python/modules/
