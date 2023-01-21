from datetime import date
import allure
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby

practice_form = PracticePage()


@allure.title("Successful fill form")
def test_registration():
    student = Student(
        first_name='Alexander',
        last_name='Santalov',
        email='asantalov@bolid.ru',
        phone='8916777665',
        address='Zelenograd',
        birthday=date(1986, 8, 3),
        gender='Male',
        subject='Chemistry',
        hobby=[Hobby.Music, Hobby.Sports],
        image='Toolsqa.jpg',
        state='Haryana',
        city='Panipat')

    with allure.step("Open registrations form"):
        practice_form.open()
    with allure.step("Fill form"):
        practice_form.fill(student).submit()
    with allure.step("Check form results"):
        practice_form.assert_results_registration(student)
