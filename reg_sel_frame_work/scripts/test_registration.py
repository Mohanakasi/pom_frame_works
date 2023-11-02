from reg_sel_frame_work.pom_classes.test_reg_pom_cl import pm_cl

def test_reg(_driver):
    r = pm_cl(_driver)
    r.click_reg_link()
    r.click_gender_male()
    r.enter_first_name()
    r.enter_last_name()
    r.enter_mail()
    r.enter_password()
    r.enter_comfirm_password()
    r.click_reg_button()
    r.take_screen_shot_success_reg()








