import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # To-do 리스트를 위한 웹 사이트 접속
        self.browser.get('http://localhost:8000')
        # 웹 사이트 타이틀과 헤더가 'To-do'를 표시
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')


        # 리스트 추가
        # 공작깃털 사기라고 텍스트 상자에 입력

        # 엔터키를 치면 페이지가 갱식되고 작업 목록에
        # '1: 공작깃털 사기' 아이템 추가

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 있다.
        # 다시 '공작 깃털을 이용해서 그물 만들기' 라고 입력

        # 페이지는 다시 갱신되고, 두개의 아이템 목록이 보인다.
        # 에디스는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 그녀를 위한 특정 url 을 생성
        # 이 url에 대한 설명도 함께 제공

        # 해당 URL에 접소하면 그녀가 만든 작업 목록이 있는 것을 확인 할 수 있다.

        #  만족하고 잠자리에 든다.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

