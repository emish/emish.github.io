import personal_site
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('personal_site', 'Templates'))

projects = []    # A list of all the projects to be rendered.
project_nav = [] # The navigation list of projects on the left.

html_out = "./public_html/"
img_dir = "../img/"

class PBar(object):
    """Bootstrap Progress Bar.
    """
    def __init__(self, progress, style="info", striped=True, animate=False):
        """Constructs a new progress bar object with given
        properties.

        Arguments:
        - `progress`: The bar progress out of 100.
        - `style`: The bar color (same as label/button styles).
          Available styles:
            'progress-info' - blue
            'progress-success' - green
            'progress-warning' - yellow
            'progress-danger' - red
        - `striped`: Should the bar be striped?
        - `animate`: Should the bar be animated? Only striped can animate.
        """
        self._progress = progress
        self._style = style
        self._striped = striped
        self._animate = animate

class Label:
    """Labels prefix the project button links in the header.
    Styles are:
    Default - which is just "label" class
    label-success, label-warning, label-important, label-info.
    """
    def __init__(self, text, link='#', style="info"):
        self.style=style
        self.link=link
        self.text=text

class Page(object):
    """
    """

    def __init__(self, title, local_link, summary, links):
        """
        A generic page with just a title, text, and buttons.
        Arguments:
        - `title`:
        - `text1`:
        - `buttons`:
        """
        self.title = title
        self.summary = summary
        self.local_link = local_link
        self.links = links

    def render(self, template):
        """Render this page with a custom template.
        Arguments:
        - `self`:
        - `template`: The template to render this page with. Will expect
           certain variables to be set.
        """
        template = env.get_template(template)
        return template.render(this=self, project_nav=project_nav)


    def render(self):
        template = env.get_template("projects_container.html")
        return template.render(this=self, project_nav=project_nav)

class Project:
    def __init__(self, title, local_link, summary, link1=None, link2=None,
                 picture=None, custom_link=None):
        global projects, project_nav

        self.title = title
        self.local_link = local_link
        self.summary = summary
        self.links = (link1,link2)
        self.description = None
        self.labels = None
        self.picture = picture
        self.custom_link = custom_link
        projects.append(self)
        project_nav.append((title, local_link))

    def setAltDescription(self, heading1, text1, img1,
                          heading2, text2, img2, btn1=None, btn2=None):
        self.description = 'alt'
        self.heading1 = heading1
        self.text1 = text1
        self.img1 = img1
        self.heading2 = heading2
        self.text2 = text2
        self.img2 = img2

    def setScreenshotDescription(self, heading1, text1, img1, imgs):
        self.description = 'scn'
        self.heading1 = heading1
        self.text1 = text1
        self.img1 = img1
        self.imgs = imgs #list

    def render(self):
        if self.description == 'alt':
            template = env.get_template('alt_description.html')
        elif self.description == 'scn':
            template = env.get_template('screens_description.html')
        elif self.description == 'exp':
            template = env.get_template('pbars_description.html')
        else:
            template = env.get_template('projects_container.html')
        return template.render(this=self, project_nav=project_nav)

# Links are (button-text, href) tuples

## Default Values
def_summary = """This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique."""

########
# About
about_summary = """If you haven't already guessed, my name is
Mishal Awadah, and I'm a computer science student at the University of
Pennsylvania. Please feel free to browse through some of my projects
or visit my Github page by navigating on the left. I hope you like
what you see!"""
about_links = [("Resume", "mishal_awadah_resume.pdf"),
               ]
about = Page("Hi there,", "about.html", about_summary, about_links)

####### TODO
# Experience
exp_summary = """This page describes the experience I have with certain tools or technologies in the form of progress bars. Animated bars mean that I'm still working on improving in those areas, while stagnant ones mean I am not actively using those."""
#exp = Page("Experience", "experience.html", exp_summary)
#exp.description = 'exp'
# make the pbars here

################# PROJECTS ################

#########
# DJ FEED
djfeed_summary = """Android app that allows you to influence the party's music by voting for upcoming songs and rating previously played songs."""

djfeed = Project("DJ Feed", 'djfeed.html', djfeed_summary,
                 ('Original Site', 'djfeed/index.html'),
                 ('View on Github', 'https://github.com/emish/DJFeed'))
djfeed.setAltDescription('Android App',
                         """Now Playing let's you see what the DJ is playing right now and rate it. Vote for upcoming songs to get what you want to hear. On auto, DJ Feed will play songs with the highest votes within a playlist. Look back at what was played last night with Previous Tracks.""",
                         'djfeed/imgs/now_playing.png',

                         'PC Client',
                         """Import your current playlist and watch the stats. People's votes get updated in real time, and the top songs pop up. Review what people thought of songs you've already played. You can also choose to take requests from the crowd.""",
                         'djfeed/imgs/playlist.png')
djfeed.labels = [Label("Collab with @patryoon",
                       "https://twitter.com/#!/patryoon"),
                 Label("Hacked @pennapps",
                       "https://twitter.com/#!/PennApps"),
                 ]
djfeed.btn1 = ("More Details", "djfeed/index.html")
djfeed.btn2 = ("More Details", "djfeed/index.html")

##############
# Stella -> Stunable
stella = Project("Stunable", 'stunable.html', def_summary,
                 ("Official Site", 'http://www.stunable.com'),
                 picture=img_dir+'stunable.png')
stella.summary = """Previously Shop with Stella, Stunable is ready to
revolutionize the way women experience fashion. Gone are the days of a
hundred thumbnails per page, replaced instead by a simple and social
recommendation interface."""
stella.labels = [Label("Collab with @stunable",
                       "https://twitter.com/#!/stunable")]

##############
# AOR Project
aor = Project("Art of Recursion", 'aor.html', def_summary,
              ("View on Github", 'https://github.com/ayanonagon/recursionapp'),
              picture=img_dir+"AORArtwork.png",
              custom_link='<a href="https://itunes.apple.com/us/app/art-of-recursion/id592094459?mt=8&uo=4" target="itunes_store"><img src="http://r.mzstatic.com/images/web/linkmaker/badge_appstore-lrg.gif" alt="Art of Recursion - Mishal Awadah" style="border: 0;"/></a>')
aor.summary = """An iPad app to discover the art of recursive drawing through touch. Use a different number of fingers while touching to draw different recursive shapes, and watch them as they animate with pretty colors. Change color themes by double-tapping. The major iOS frameworks used here were Quartz2D and CoreAnimation.
"""
aor.labels = [Label("Collab with @ayanonagon",
                    "https://twitter.com/ayanonagon"),
              Label("Collab with +Elissa Wolf",
                    "https://plus.google.com/109425530595511038219/about")]
aor.setAltDescription('Multi-Finger Touch Responses',
                      """Depending on how many fingers you use to interact with the application, a different recursive drawing will animate itself. Here's an example of using one finger in the middle of the screen to recursively draw these boxes within each other.""",
                      img_dir+"AORLine.png",

                      "Animation, Fade-Out, and Color Themes",
                      """Whenever a drawing is displayed, it draws itself one recursive level at a time, so you can see exactly how the recursion works to form the complete image. Here's an example of using two fingers to draw a Levy.
Also, double-tap to change between a variety of built-in color themes.""",
                      img_dir+"AORLevy.png",
                      )

                      # "Awesome Shapes of all kinds!",
                      # "Here's a screenshot of a rare pentaflake!",
                      # img_dir+"AORPentaflake.jpg")

##############
# OAT Compiler
oat_screens = [img_dir+'bubble_stage.jpg',
               img_dir+'bubble_all.jpg']
oat_summary = """The Objects, Arrays, and Types programming language. Wrote the parser and compiler with a buddy in OCaml, then we showcased it's greatness in a little terminal game."""

oat = Project("OAT Compiler", 'oat.html', oat_summary,
              ("View on Github", 'https://github.com/emish/Bubble-Trouble'))
oat.labels = [Label("Collab with +Stefan",
                    "https://plus.google.com/106540936931903771697/about")]
oat.setScreenshotDescription('Bubble Trouble',
                             """In this early childhood game, you have to pop all the bubbles using a harpoon. Larger bubbles split into more bubbles that you have to take care of too. The drawing is taken care of by ncurses, which is linked to OAT as a C library.""",
                             img_dir+'bubble_start.jpg',
                             oat_screens)

##############
# LC4 Sim
lc4sim = Project("LC4 Simulator", 'lc4sim.html', def_summary,
            ('View on Github', 'https://github.com/emish/lc4sim'))
lc4sim.summary = """An assembly language interpreter created in
Haskell. LC4 is an improved version of the known LC3 (Little Computer
3) language developed at the University of Pennsylvania. We decided to
create this psuedo-debugger as a way for students first learning the
language to debug their assembly code."""
lc4sim.labels = [Label("Collab with @johnpmayer", "https://github.com/johnpmayer")]

##############
# Emacs Club
emacsclub = Project("Emacs Club", 'emacsclub.html', def_summary,
                    ("Visit the Site", 'http://www.emacsclub.com'))
emacsclub.summary = """Rivals of Vim users unite! Just kidding, we
love you guys too. But seriously, Emacs is so awesome how could there
not be a club? This Penn group holds lectures and hack sessions on all topics
emacs."""

##############
# Pandorify
pandorify = Project("Pandorify", 'pandorify.html', def_summary,
                    ("Check it out!",
                     'http://pandorify.us'))
pandorify.summary = """Converts your Pandora Radio stations into Spotify
playlists using your thumbed-up tracks. Still a work in progress.
"""
pandorify.labels = [Label("Hacked @pennapps",
                          "https://twitter.com/#!/PennApps"),
                    Label("Unstable",
                          "",
                          "important")]

##############
# Speech HTM
speech = Project("Speech Recognition and Numenta", 'speech.html', def_summary)
speech.summary = """It's a love and hate relationship with this
one. The idea was solid, but ambitious. HTMs are also pretty cool."""
speech.links = [('Proposal', 'cis400_proposal_final.pdf'),
                ('Research Paper', 'progress_report.pdf')
                ]

##############
# BARD
bard = Project("B.A.R.D.", 'bard.html', def_summary,
               ("Project Report",
                'cis350_report.pdf'),
               #picture=img_dir+"bard_logo.png",
               )
bard.summary = """Botnet Atom Realtime Detector, an active distributed
firewall whose primary purpose is to detect and protect against botnet
attacks and infiltration. This is done by analyzing network flow
information for patterns common to botnet behaviors and attacks, and
uses a particular packet trait known as 'persistence'. This was a
group-based project, and you can find lots more details on the
official site."""

def render_all():
    for proj in projects:
        fp = file(html_out+proj.local_link, 'w')
        print >>fp, proj.render()
        fp.close()
    fp = file(html_out+about.local_link, 'w')
    print >>fp, about.render()
    fp.close()

render_all()
