#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def main():
    f = open("fix_script.sh", "w+")
    for line in open("packages"):
        pkg = re.match(
            re.compile("""dpkg: warning: files list file for package '(.+)' """), line
        )
        if pkg:
            cmd = "sudo apt-get install --reinstall " + pkg.group(1)
            f.write(cmd + "\n")


if __name__ == "__main__":
    main()
