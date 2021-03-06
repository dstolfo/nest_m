
import os
import tornado.web

#from lib.config import config
from web.nest_m.amiup import AmIUpHandler
from web.nest_m.home import HomeHandler
from web.nest_m.slides import *


class NestMApplication(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r"/amiup", AmIUpHandler),
            (r"/", HomeHandler),
            (r"/slides_1", CourseSlides1Handler),
            (r"/slides_2", CourseSlides2Handler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            #static_path=os.path.join(config['build']['public_dir'])
            static_path="./public_dist"
        )
        tornado.web.Application.__init__(self, handlers, **settings)

