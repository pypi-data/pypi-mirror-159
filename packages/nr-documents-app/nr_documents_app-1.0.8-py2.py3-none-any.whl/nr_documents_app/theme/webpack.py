# Copyright (c) 2022 CESNET
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""JS/CSS bundles for nr-documents-app.

You include one of the bundles in a page like the example below (using
``base`` bundle as an example):

 .. code-block:: html

    {{ webpack['base.js']}}

"""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                'nr-documents-search': './js/nr_documents_app/search/index.js'
            },
            dependencies={
            },
            aliases={
                '@js/nr_documents_app': 'js/nr_documents_app',
                '@uijs/nr_documents_app': 'js/nr_documents_app/ui_components',
            }
        )
    },
)
