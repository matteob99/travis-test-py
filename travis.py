import os

import botogram

bot = botogram.create(os.environ['TELEGRAM_TOKEN'])

success = True if os.environ['TRAVIS_TEST_RESULT'] == '0' else False

if os.environ['TRAVIS_PULL_REQUEST'] != 'false':
    branch = '🔌 <b>Pull request</b> #{pr} from <code>{slug}</code>'.format(
        pr=os.environ['TRAVIS_PULL_REQUEST'],
        slug=os.environ['TRAVIS_PULL_REQUEST_SLUG']
    )
else:
    branch = '🛤 <b>Branch</b> {branch}'.format(branch=os.environ['TRAVIS_BRANCH'])

text = (
    '{emoji} <b>Travis build {status}</b> (<a href="{link}">link</a>)'
    '\n{branch}'
    '\nCommit {commit}'
    ''.format(
        emoji='✅' if success else '❌',
        status='passed' if success else 'failed',
        link=os.environ['TRAVIS_BUILD_WEB_URL'],
        branch=branch,
        commit=os.environ['TRAVIS_COMMIT']
    )
)
btns = botogram.Buttons()
btns[0].url("Open in Travis", os.environ['TRAVIS_BUILD_WEB_URL'])

bot.chat(os.environ['TELEGRAM_CHAT_ID']).send(text, attach=btns)