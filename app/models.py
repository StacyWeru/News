class Article:

    '''
    Article class to define article objects
    '''

    def __init__(self,image,url,title,author,description,publishedAt):
        self.image = image
        self.url =image
        self.title = title
        self.author = author
        self.description = description
        self.pulishedAt = publishedAt




class Source:

    '''
    Source class to define source objects
    '''

    def __init__(self ,id, name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url



class Headlines:

    '''
    Headlines class to define the headline object
    '''

    def __init__(self,image,url,title,author,description,publishedAt):
        self.image = image
        self.url =image
        self.title = title
        self.author = author
        self.description = description
        self.pulishedAt = publishedAt
