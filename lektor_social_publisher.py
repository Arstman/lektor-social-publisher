# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class SocialPublisherPlugin(Plugin):
    name = 'lektor-social-publisher'
    description = u'A plugin of Lektor CMS to publisher newest post to social networks like Facebook, twitter.'

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function
