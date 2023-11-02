import pytest

from practice_desighn_frame_work.POM_pages.login_page import Login

def test_driver_return(setup_test):
    return setup_test

# @pytest.mark.usefixtures('setup_test')
# class   Test_login_logout(Login):
#     u_name = 'Admin'

def test_log_log_out(setup_test):
    obj1 = Login(setup_test)
    obj1.enter_user_name('Admin')
    obj1.enter_pass_word('admin123')
    obj1.click_on_submit_button()
    obj1.click_on_profile()
    obj1.log_out()

# obj1 = Test_login_logout(set)
# obj1.test_log_log_out()