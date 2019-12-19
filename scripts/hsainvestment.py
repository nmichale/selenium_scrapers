import click
import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = 'http://hsainvestment.com/'
TRANSFER_URL = 'https://hsainvestment.com/Participant/aspx/authenticated/CustomLink.aspx?' \
               'link=secureFileHandler.ashx%3ffileName%3dwebpages%2fp%2ftbh%2fmmwidget.html'

def transfer(username, password, amount):
    with browser.Browser(implicit_wait=30) as b:
        b.get(URL)
        b.find_element_by_id('loginControl_UserName').send_keys(username)
        b.find_element_by_id('loginControl_Password').send_keys(password)

        b.find_element_by_id('loginControl_LoginButton').click()

        move_money = b.find_element_by_id('x:1096785038.11:adr:2')
        hover = ActionChains(b).move_to_element(move_money)
        hover.perform()

        b.find_element_by_id('x:1096785038.13:adr:2.1').click()

        # b.get(TRANSFER_URL)
        b.find_element_by_name('amount').send_keys(amount)
        b.find_element_by_css_selector('.btn[value="Submit"]').click()

        print(b.find_element_by_tag_name('p').get_attribute('innerHTML'))


@click.command()
@click.option('-a', '--amount', type=click.FLOAT, help='Amount to transfer to hsainvestments')
@click.option('-u', '--username', type=click.STRING, help='Username for hsainvestments.com')
@click.option('-p', '--password', prompt=True, hide_input=True, confirmation_prompt=True,
              help='Password for hsainvestments.com')
def main(username, password, amount):
    transfer(**locals())

if __name__ == '__main__':
    main()