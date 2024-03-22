import json

class Media:
    def __init__(self, email, cv, github, linkedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.linkedin = linkedin

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
    def __init__(self, icon, title, subtitle, description, date="", certificate="", 
            technologies=[], image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology(**tech) for tech in technologies]
        self.image = image
        self.url = url
        self.github = github

class Other:
    def __init__(self, title, subtitle, image, url):
        self.title = title
        self.subtitle = subtitle
        self.image = image
        self.url = url

class Data:
    def __init__(self, avatar, name, title, location, last_update, media, about, technologies, 
            experiences, projects, training, others):
        self.avatar = avatar
        self.name = name
        self.title = title
        self.location = location
        self.last_update = last_update
        self.media = Media(**media)
        self.about = about
        self.technologies = [Technology(**tech) for tech in technologies]
        self.experiences = [Experience(**experience) for experience in experiences]
        self.projects = [Section(**section) for section in projects]
        self.training = [Section(**section) for section in training]
        self.others = [Other(**other) for other in others]

with open("assets/data.json", encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data)