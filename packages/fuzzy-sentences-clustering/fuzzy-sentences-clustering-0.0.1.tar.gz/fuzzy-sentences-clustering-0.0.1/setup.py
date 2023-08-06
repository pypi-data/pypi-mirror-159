# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fuzzy_sentences_clustering']

package_data = \
{'': ['*']}

install_requires = \
['fuzzywuzzy==0.18.0', 'nltk==3.7', 'python-Levenshtein-wheels==0.13.2']

setup_kwargs = {
    'name': 'fuzzy-sentences-clustering',
    'version': '0.0.1',
    'description': 'Clustering similar sentences based on their fuzzy similarity.',
    'long_description': 'fuzzy-sentences-clustering\n==========================\n\nClustering similar sentences based on their fuzzy similarity.\n\nPurpose of the Package\n----------------------\n\nThere are some popular algorithms on the market for mining topics in a\ntextual set, such as\n`LDA <https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation>`__, but\nthey don’t work very well for a small set of data, let’s say a thousand\nsentences for example.\n\nThis package tries to solve this for a small dataset by making the\nfollowing naive assumption:\n\n   *If I remove all\n   the*\\ `stopwords <https://en.wikipedia.org/wiki/Stop_word>`__\\ *between\n   two sentences, extract\n   the*\\ `stems <https://en.wikipedia.org/wiki/Stemming>`__\\ *of their\n   words, sort their words and after that find similar phrases\n   (intersection) between these two sentences, they are probably talking\n   about the same, or similar, subject.*\n\nThe goal here is to form clusters/groups with at least two similar\nsentences, isolated sentences (sentences that don’t look like any other\nin the total set) will not generate a cluster just for them. For these\ncases, the sentence will receive the *-1* tag.\n\nFor while it works just for **portuguese** language.\n\nInstallation\n------------\n\nYou can install it using pip:\n\n.. code:: bash\n\n   pip3 install fuzzy-sentences-clustering\n\nUsage\n-----\n\n.. code:: python\n\n   >>> from fuzzy_sentences_clustering import look_for_clusters\n   >>> sentences = ["morava em florianópolis", "comprar um carro", "compra de um carro", "em florianópolis eu moro", "gosto de samba", "quero comer tapioca"]\n   >>> res = look_for_clusters(sentences=sentences, similarity_threshold=90)\n   >>> print(res)\n   output: [1, 2, 2, 1, -1, -1]\n\nContribution\n------------\n\nContributions are welcome.\n\nIf you find a bug, please let me know.\n\nAuthor\n------\n\n`Cloves Paiva <https://www.linkedin.com/in/cloves-paiva-02b449124/>`__.\n',
    'author': 'Cloves Paiva',
    'author_email': 'clovesgtx@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SClovesgtx/fuzzy-sentences-clustering',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
