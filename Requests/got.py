import mechanize as br


def browser_get_instance():
    br.browser = str[input('email or id: ')]


instance = ['email', 'id']
index = ['tabindex="0"']


def browser_get_pwd(instance):
    br.browser = getattr(instance, 'index')


# noinspection PyRedeclaration
instance = ['txt']
# noinspection PyRedeclaration
index = ['tabindex="0"']

browser_get_pwd(instance)


def grabbing(pwd):
    return None