from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: linux
app: Firefox
"""

@ctx.action_class('app')
class AppActions:
    def tab_next():     actions.key('ctrl-pagedown')
    def tab_previous(): actions.key('ctrl-pageup')


@ctx.action_class('browser')
class BrowserActions:
    def bookmarks():
        actions.key('ctrl-shift-o')