# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ntuee_mailer']

package_data = \
{'': ['*']}

install_requires = \
['Cerberus==1.3.4',
 'PyYAML==6.0',
 'email-validator==1.2.1',
 'rich==12.5.1',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['ntuee-mailer = ntuee_mailer.main:app']}

setup_kwargs = {
    'name': 'ntuee-mailer',
    'version': '2.0.0',
    'description': 'an auto mailer to send emails in batch for you',
    'long_description': "# 學術部寄信程式\n\n## Requirements\n\n- python 3.X 64bit\n- 套件皆有內建，不需額外安裝\n\n## Usage\n\n- **請不要把信件內容push上來**，負責人可以寫完信之後zip好傳給其他人\n- 請複製 letters 資料夾中的 template 來創建新的信件\n- content.html 放信件內文\n  - **記得在內文中加入$recipient**，此處會被替換成收件人，及其稱謂\n- recipients.csv 收件人及信箱名單\n  - 可以用 excel 編輯 csv 檔案，格式詳見 template\n  - **第一欄填收件人姓名，第二欄填收件人信箱**\n  - 如果是臺大的信箱，可以不用填 '@ntu.edu.tw'，會自動加上去\n- config.json 裡面可以修改信件設定\n  - subject 為主旨\n  - from 為寄件人名稱顯示，如果 from 留空白會顯示你原本的名稱\n  - recipientTitle 裡面的 Title 不是空字串則會把這個 title 接到收件人姓名後面\n  - lastNameOnly 如果是 true，使用「姓氏+稱謂」，反之則使用「全名+稱謂」\n- attachments 資料夾裡放要附加的檔案\n  - 執行時使用-a 選項來附加，預設不附加檔案，下面有範例\n  - 如果你很在乎順序的話，取檔名的時候記得要確認順序\n- **account-default.ini的檔名改成account.ini** 裡面放自己的計中帳密\n  - **把檔案寄給別人時這個要改掉，不然大家都知道了**\n\n## Run\n\n    python mailer_invite.py LETTER\n    python3 mailer_invite.py LETTER\n\nLETTER is the name of the folder in the 'letters' folder where your email lives\n\n### Options\n\n    -h, --help    show help message and exit\n    -a, --attach  attach files in 'letters/LETTER/attachments' folder to the email\n    -t, --test    send email in test mode (to yourself)\n\n## Examples\n\n    python3 mailer_invite.py template -t\n    python mailer_invite.py letter1 -a\n",
    'author': 'zhuang-jia-xu',
    'author_email': '76544194+zhuang-jia-xu@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NTUEE-SAAD/mailing',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
