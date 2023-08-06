import json

class langtranslator:
    def __init__(self, file, language):
        file = open(file, "r")
        self.translations = json.load(file)
        file.close()
        if language in self.translations["info"]["languages"]:
            self.language = language
        else:
            self.language = self.translations["info"]["languages"][0]
    
    def get(self, key):
        if key in self.translations["translations"]:
            return self.translations["translations"][key][self.language]
        else:
            return "Error"
