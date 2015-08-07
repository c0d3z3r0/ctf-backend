from dynamic_preferences.types import StringPreference, LongStringPreference
from dynamic_preferences import global_preferences_registry


@global_preferences_registry.register
class BackendTitle(StringPreference):
    section = 'general'
    name = 'sitename'
    verbose_name = 'Backend Title'
    default = 'CTF@HSO'
    help_text = 'The website title (Default: '+default+')'


@global_preferences_registry.register
class HomeTitle(StringPreference):
    section = 'home'
    name = 'title'
    verbose_name = 'Home Title'
    default = 'Welcome to CTF@HSO ...'
    help_text = 'Home site title (Default: '+default+')'


@global_preferences_registry.register
class HomeLead(LongStringPreference):
    section = 'home'
    name = 'lead'
    verbose_name = 'Home Lead'
    default = '... the Capture the Flag Workshop of the<br>University of ' \
              'Applied Sciences in Offenburg.'
    help_text = 'Home site lead text (Default: '+default+')'
