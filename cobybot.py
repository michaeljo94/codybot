# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

from core.clients import CodyClient

if __name__ == "__main__":
    load_dotenv()
    client = CodyClient()
    client.run(os.getenv("DISCORD_TOKEN"))
