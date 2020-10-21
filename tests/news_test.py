import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):

    '''
    To test the bahaviour of the Article class
    '''

    def setUp(self):
        '''
        SetUp method will run before every test
        '''

        self.new_article = Article('https://checlit.jpg','https://Itdidntgowell/2020/10/10/lifestyle/seethrough','She tried this really hard','Stacy Weru','After many days and many nights of restless sleep it turned out she had no clue of what she was actually doing','2020-10-20T07:43:28Z')


    def test_instance(self):
        '''
        Check the creation of a new article
        '''

        self.assertTrue(isinstance(self.new_article,Article))