import requests

from exceptions import HandshakeError


class Status:
    def __init__(self, region: str):
        self.region = region
        
    def request(self) -> dict:
        session = requests.session()
        data = session.get(f"http://valorant.secure.dyn.riotcdn.net/channels/public/x/status/{self.region.casefold()}.json")
        if data.status_code == 200:
            data = data.json()
            return {
                'issue':data['incidents'] or data['maintenances'],
                'incidents':data['incidents'],
                'maintenances':data['maintenances']
                }
        else:
            raise HandshakeError("Some error occured")
   
    def get_status(self):
        status = self.request()
        if status['issue'] != []:
            return True
        else:
            return False
                
    def incident_title(self):
        try:
            return self.request()["incidents"][0]['titles'][0]['content']
        except IndexError:
            return

    def incident_platform(self):
        try:
            return self.request()["incidents"][0]["platforms"]
        except IndexError:
            return
        
    def incident_datetime(self):
        try:
            datetime= self.request()['incidents'][0]['updates'][0]['created_at'][:16]
            date=datetime[:10]
            time=datetime[11:16]
            return [date, time]
        except IndexError:
            return
        
    def incident_reason(self):
        try:
            return self.request()['incidents'][0]['updates'][0]['translations'][0]['content']
        except IndexError:
            return
        
    def maintenance_title(self):
        try:
            return self.request()["maintenances"][0]['titles'][0]['content']
        except IndexError:
            return

    def maintenance_platform(self):
        try:
            return self.request()["maintenances"][0]["platforms"]
        except IndexError:
            return
        
    def maintenance_datetime(self):
        try:
            datetime=self.request()['maintenances'][0]['updates'][0]['created_at'][:16]
            date=datetime[:10]
            time=datetime[11:16]
            return date, time
        except IndexError:
            return
        
    def maintenance_reason(self):
        try:
            return self.request()['maintenances'][0]['updates'][0]['translations'][0]['content']
        except IndexError:
            return
        
    def maintenence_check(self):
        if self.request()['maintenances'] != []:
            return True
        else:
            return False
        
    def incident_check(self):
        if self.request()['incidents'] != []:
            return True
        else:
            return False