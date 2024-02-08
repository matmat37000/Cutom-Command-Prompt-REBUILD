from uuid import UUID, uuid4

import yaml

class command():
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.path: str = ""
        self.ID: UUID = uuid4()
        
    def save(self):
        with open("TEST_APP/{self.name}.yml", "x") as file:
            ...