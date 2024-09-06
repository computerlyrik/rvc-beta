import json
import locale
import os

import importlib.resources

def load_language(language):
    try: 
        content = importlib.resources.files('rvc_beta').joinpath(f"i18n/locale/{language}.json").read_text(encoding="utf-8")
    except:
        language = "en_US"
        content = importlib.resources.files('rvc_beta').joinpath(f"i18n/locale/{language}.json").read_text(encoding="utf-8")
    return language, json.loads(content)


class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = locale.getdefaultlocale()[
                0
            ]  # getlocale can't identify the system's language ((None, None))
        
        self.language, self.language_map = load_language(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
