@echo off
cd C:\development\pom_frame_work\ajio_submission
pytest tests/scripts/test_adding_cart.py::Test_cart_validations::test_ajio_logo_test
pytest tests/scripts/test_adding_cart.py::Test_cart_validations::test_cart_item_check_item_and_home_page
pytest tests/scripts/test_adding_cart.py::Test_cart_validations::test_adding_cart_delete
cd C:\development\pom_frame_work
git add .
git commit -m "commit from batch file"
git push origin master
