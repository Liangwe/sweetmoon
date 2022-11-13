"""
@Author: Liang
@Time: 2022/11/13 17:24
@Github: https://github.com/Liangwe
@FileName: tools.py
@Desc: xxx
"""
from flask import Blueprint


class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)

        self.record(deferred)
