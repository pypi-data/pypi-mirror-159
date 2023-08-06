# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mongars']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.0,<4.0.0']

entry_points = \
{'console_scripts': ['mongars = mongars.cli:main']}

setup_kwargs = {
    'name': 'mongars',
    'version': '0.7.1',
    'description': 'Show unread emails in INBOX using Gnome Online Accounts',
    'long_description': '# mongars - count inbox emails\n\ncount inbox emails using Gnome Online Accounts\n\n## Description\n\n`mongars` will take an email account as configured in Gnome Online account (only\noauth based email account is supported) and will output how many unread emails\nyou have in there.\n\nYou just need to specify the email to check as an argument i.e:\n\n```shell\nmongars john.snow@gmail.com\n```\n\nBy default it will output the number of messages from your mailbox with an icon of different\ncolours if there is unreads message or not.\n\nThe `INBOX` folder is the default folder, if you would like to count another folder you can specify the `-m` option to it :\n\n```shell\nmongars -m Label1 john.snow@gmail.com\n```\n\nYou can further customize the colour output which uses lemonbar formatting with :\n\n* `--icon`: the glyph icon default to `\uf2b6`\n* `--icon-color-unreads`: the color when unreads, default to a yellow `#ffd700` set this to empty if you don\'t want any color formatting.\n* `--icon-color-normal`: the normal colors. (no default)\n\nBy default if you have no mail it will output a 0 unless you specify the flag `--no-mail-no-zero`\n\nIf you don\'t want any icons you can simply use the `--no-icon` and it will just output the number.\n\nThis currently only support oauth2 based accounts, imap account with username,\npassword are not currently supported (patch welcome but you probably want to use\nsomething more secure).\n\nI only tested it with Google/Gmail accounts (enteprise and personal) so let me\nknow if it works or not on other oauth2 based email accounts.\n\n## Install\n\n### Arch\n\nYou can install this [from aur](https://aur.archlinux.org/packages/mongars) with your aurhelper, like yay :\n\n```\nyay -S mongars\n```\n\n### pip\n\nWith pip from pypip - https://pypi.org/project/mongars/\n\n```\npip install --user mongars\n```\n\n(make sure $HOME/.local/bin is in your PATH)\n\n### Manual\n\nCheckout this repository, [install poetry](https://python-poetry.org/docs/#installation) and run it with :\n\n```shell\npoetry install mongars\npoetry run mongars\n```\n\n## Running it without Gnome\n\nIf you run this outside of gnome environement (ie: from a windows manager), you have to configure the accounts\nfirst in Gnone Online Account settings from gnome and then you can use it from your windows manager.\n\nFrom your window manager start scripts or [somewhere else](https://wiki.archlinux.org/title/Xinit)  you need to make sure to run the goa-daemon, for example on arch the path is `/usr/lib/goa-daemon` and from your startup script you will do :\n\n```shell\n/usr/lib/goa-daemon --replace &\n```\n\ndifferent distros may have a different path, see also this bugzilla bug\n[#1340203](https://bugzilla.redhat.com/show_bug.cgi?id=1340203))\n\n## Polybar\n\nYou can easily integrate this with [Polybar](https://github.com/polybar/polybar) :\n\n```ini\n[module/email]\ntype = custom/script\nexec = mongars email@gmail.com\ninterval = 30\nclick-left = xdg-open https://mail.google.com/\nexec-if = grep -q email@gmail.com ~/.config/goa-1.0/accounts.conf 2>/dev/null && ping -c1 mail.google.com\n```\n\n\n## Waybar\n```json\n    "custom/email": {\n        "format": "\ufaee {} ",\n        "interval": 15,\n        "exec": "mongars email@gmail.com --no-mail-no-zero --no-icon",\n        "on-click": "xdg-open https://mail.google.com"\n    },\n```\n\nand you can style it in `style.css` file :\n\n```css\n#custom-email {\n\tcolor: #b22222;\n}\n```\n\n## License\n\n[Apache 2.0](./LICENSE)\n\n## Authors\n\n© 2021 Chmouel Boudjnah ([@chmouel](https://twitter.com/chmouel)) - https://chmouel.com\n',
    'author': 'Chmouel Boudjnah',
    'author_email': 'chmouel@chmouel.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chmouel/mongars',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
