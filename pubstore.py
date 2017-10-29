#!/usr/bin/env python3
import pubstore_client as psc
from sys import argv

if __name__ == "__main__":
    print(
        psc.post_new_key(argv[1], psc.base_url)
    )
