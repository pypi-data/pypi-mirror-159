# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spotify_to_musi', 'spotify_to_musi.typings']

package_data = \
{'': ['*']}

install_requires = \
['requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.28.1,<3.0.0',
 'rich-click>=1.5.1,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'spotipy>=2.20.0,<3.0.0',
 'ytmusicapi>=0.22.0,<0.23.0']

entry_points = \
{'console_scripts': ['spotify-to-musi = spotify_to_musi.__main__:cli']}

setup_kwargs = {
    'name': 'spotify-to-musi',
    'version': '1.0.0',
    'description': 'Transfer Spotify playlists to Musi.',
    'long_description': "# spotify-to-musi\n\n> Transfer your [Spotify](https://spotify.com) playlists to [Musi](https://feelthemusi.com).\n\n![banner](./.github/assets/banner.png)\n\n# Why Musi?\n\nMusi allows you to listen to any song (video) from YouTube without being interrupted with ads like with Spotify.\nAs someone who doesn't have a music streaming subscription I prefer to use Spotify on Desktop and Musi on mobile,\nso I created this app to transfer songs between the two.\n\n# Spotify API\n\n1. Go to https://developer.spotify.com/dashboard/ \\\n   ![Dashboard](./.github/assets/dashboard.png)\n2. Choose an app name and accept the terms and conditions. \\\n   ![CREATE AN APP](./.github/assets/create-an-app.png)\n3. Set callback to https://example.com/callback/ \\\n   ![Set Callback](./.github/assets/set-callback.png)\n4. View Client ID and Client Secret \\\n   ![SHOW CLIENT SECRET](./.github/assets/show-client-secret.png)\n5. Rename .env.example to .env and set secrets \\\n   ![.env file](./.github/assets/dotenv-file.png)\n6. Upon running the script for the first time, you will be prompted with something that looks like this: \\\n   ![first time setup](./.github/assets/first-time-setup.png)\n7. Click the URL, Sign In if you need to and proceed until you see a page that looks like this: \\\n   ![img.png](.github/assets/example.com.png)\n8. Copy the URL of the page you were redirected to and paste it into the console of the program and enter\n\n# PyCharm Usage\n\nIf you're running pycharm, make sure `emulate terminal in output console` is enabled<br>\n\nreferences:\n\n- https://youtrack.jetbrains.com/issue/PY-43860\n- https://rich.readthedocs.io/en/latest/introductin.html\n",
    'author': 'Hexiro',
    'author_email': 'mail@hexiro.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hexiro/spotify-to-musi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
