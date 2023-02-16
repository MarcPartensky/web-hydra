#!/bin/sh
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
wget https://github.com/jeanphorn/wordlist/blob/master/usernames.txt

python /root/web-hydra
