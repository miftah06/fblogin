import mechanize as br

import btn


def browser_get_instance():
    br.browser = str[input('email or id: ')]


instance = ['email', 'id']
btn.index = ['tabindex="0"']


def browser_get_pwd(instance):
    br.browser = getattr(instance, 'index')


# noinspection PyRedeclaration
instance = ['txt']
btn.index = ['tabindex="0"']

browser_get_pwd(instance)
