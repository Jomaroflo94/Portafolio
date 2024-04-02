import json

class Profile:
    def __init__(self, name, position, location, last_update, avatar):
        self.name = name
        self.position = position
        self.location = location
        self.last_update = last_update
        self.avatar = avatar

class Media:
    def __init__(self, icon, url, is_primary=True, text=""):
        self.icon = icon
        self.url = url
        self.is_primary = is_primary
        self.text = text

class Technology:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

class Experience:
    def __init__(self, name, image, sections):
        self.name = name
        self.image = image
        self.sections = [Section(**section) for section in sections]

class Section:
    def __init__(self, title, subtitle, date="", icon="", image_icon="",
            image="", description=[], technologies=[], media=[]):
        self.title = title
        self.subtitle = subtitle
        self.description = [str(item) for item in description]
        self.date = date
        self.icon = icon
        self.image_icon = image_icon
        self.technologies = [Technology(**item) for item in technologies]
        self.image = image
        self.media = [Media(**item) for item in media]

class Other:
    def __init__(self, title, subtitle, image, url):
        self.title = title
        self.subtitle = subtitle
        self.image = image
        self.url = url

class Data:
    def __init__(self, profile, media, technologies, experiences,
            projects, training, others, about=[]):
        self.profile = Profile(**profile)
        self.media = [Media(**item) for item in media]
        self.technologies = [Technology(**item) for item in technologies]
        self.experiences = [Experience(**item) for item in experiences]
        self.projects = [Section(**item) for item in projects]
        self.training = [Section(**item) for item in training]
        self.others = [Other(**item) for item in others]
        self.about = [str(item) for item in about]

with open("portafolio/services/data.json", encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data)