from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder

# --NO COMPILA - però sintàcticament està bé

screen_helper = """
Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:

            ContentNavigationDrawer:

"""

class ContentNavigationDrawer(BoxLayout):
    pass


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)


TestNavigationDrawer().run()