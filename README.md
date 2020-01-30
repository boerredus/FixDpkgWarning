# FixDpkgWarning

Python script to fix "dpkg: warning: files list file for package 'xyz' missing;"

## Usage

* Copy all the errors (e.g __dpkg: warning: files list file for package 'libxcb-xkb1:amd64' missing; assuming package has no files currently installed__) to the `packages` file (separated by a linebreak).

* Execute `python app.py`, on Terminal.

* Run `chmod +x fix_script.sh` and `./fix_script.sh` on Terminal.


The Terminal will, then, reinstall all packages. That's it. Enjoy!!

**Based on [this](https://stackoverflow.com/a/47117845) answer.**