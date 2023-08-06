Run commands in environments, with a focus on prefix commands

`prefix` is a Python package for working with prefix commands and "command environments" and related concepts

Documentation: [doc.md](./doc.md).

The concept is taken from Mark Seaborn's `cmd_env.py`.  The actual code I think
I rewrote from memory several times a long time ago, but it's simple so probably
byte-for-byte the same as `cmd_env.py` in places.  The most notable difference
is that there is explicit support for splitting commands that only have side
effects from those that only have return values (i.e. output to stderr/stdout),
so that it's possible for programs using `prefix` to work fully in dry-run mode.

Right now things may change, because I haven't used it in this precise form yet.
