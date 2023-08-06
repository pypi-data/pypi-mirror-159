# Scribus

A simple script formatting binary data for paper storage.

[paperkey](https://www.jabberwocky.com/software/paperkey/) is great but when working with private keys on elliptic curves it doesn't gain much by striping extra data. In the other hand, recovering keys from paper storage generally means the situation is critical and there's no time to waste pulling back together missing pieces.

## Install

```
$ pip install scribus
```

## Run

```
```

## Test

Tested on linux:
```
$ cat tests/data | scribus --encode - | scribus --decode - > tests/data2
$ md5sum tests/*
d5658770e0ecb36e5785cccd51852df5  tests/data
d5658770e0ecb36e5785cccd51852df5  tests/data2
```

