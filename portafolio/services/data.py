import json

class Profile:
    def __init__(self, name: str, position: str, location: str, last_update: str, 
        avatar: str):
        self.name = name
        self.position = position
        self.location = location
        self.last_update = last_update
        self.avatar = avatar

    def to_dict(self):
        return self.__dict__

class Media:
    def __init__(self, icon: str, url: str, is_primary=True, text=""):
        self.icon = icon
        self.url = url
        self.is_primary = is_primary
        self.text = text

    def to_dict(self):
        return self.__dict__

class Technology:
    def __init__(self, icon: str, name: str):
        self.icon = icon
        self.name = name

    def to_dict(self):
        return self.__dict__

class Section:
    def __init__(self, title: str, subtitle: str, date="", icon="", image_icon="",
        image="", description: list[str] = [], technologies: list[Technology] = [], 
        media: list[Media] = []):
        self.title = title
        self.subtitle = subtitle
        self.description = [str(item) for item in description]
        self.date = date
        self.icon = icon
        self.image_icon = image_icon
        self.technologies = [Technology(**item) if isinstance(item, dict) else item for item in technologies]
        self.image = image
        self.media = [Media(**item) if isinstance(item, dict) else item for item in media]

    def to_dict(self):
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "date": self.date,
            "icon": self.icon,
            "image_icon": self.image_icon,
            "image": self.image,
            "technologies": [tech.to_dict() for tech in self.technologies],
            "media": [m.to_dict() for m in self.media],
        }

class Experience:
    def __init__(self, name: str, image: str, lineHeight: str, sections: list[Section]):
        self.name = name
        self.image = image
        self.lineHeight = lineHeight
        self.sections = [Section(**section) if isinstance(section, dict) else section for section in sections]
    
    def to_dict(self):
        return {
            "name": self.name,
            "image": self.image,
            "lineHeight": self.lineHeight,
            "sections": [section.to_dict() for section in self.sections],
        }

class Other:
    def __init__(self, title: str, subtitle: str, image: str, url: str):
        self.title = title
        self.subtitle = subtitle
        self.image = image
        self.url = url
    
    def to_dict(self):
        return self.__dict__

class Data:
    def __init__(self, profile, media: list[Media], technologies: list[Technology], 
        experiences: list[Experience], projects: list[Section], training: list[Section], 
        others: list[Other], about=[]):
        self.profile = Profile(**profile)
        self.media = [Media(**item) for item in media]
        self.technologies = [Technology(**item) for item in technologies]
        self.experiences = [Experience(**item) for item in experiences]
        self.projects = [Section(**item) for item in projects]
        self.training = [Section(**item) for item in training]
        self.others = [Other(**item) for item in others]
        self.about = [str(item) for item in about]

    def to_dict(self):
        return {
            "profile": self.profile.to_dict(),
            "media": [m.to_dict() for m in self.media],
            "technologies": [tech.to_dict() for tech in self.technologies],
            "experiences": [exp.to_dict() for exp in self.experiences],
            "projects": [proj.to_dict() for proj in self.projects],
            "training": [train.to_dict() for train in self.training],
            "others": [other.to_dict() for other in self.others],
            "about": self.about,
        }

with open("portafolio/services/data.json", encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data).to_dict()