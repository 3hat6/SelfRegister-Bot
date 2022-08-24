import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Paths



def clickerbyXpath(path):
    ok = True
    x = time.time()
    while ok:
        try:
            x = browser.find_element_by_xpath(path)
            x.click()
            return True
        except:
            time.sleep(0.1)
            y = time.time()


def senderbyXpath(path, text):
    ok = True
    while ok:
        try:
            x = browser.find_element_by_xpath(path)
            x.send_keys(text)
            return True
        except:
            time.sleep(0.1)


def checker(path):
    ok = True
    while ok:
        try:
            x = browser.find_element_by_xpath(path)
            return path
        except:
            time.sleep(0.1)


def login(username, password, gencode):
    senderbyXpath(Paths.login_field, username)
    clickerbyXpath(Paths.next1)  # next
    time.sleep(1)
    senderbyXpath(Paths.password, password)
    senderbyXpath(Paths.identify_code, gencode)
    clickerbyXpath(Paths.login)  # next
    clickerbyXpath(Paths.aycer)  # aycer

    print("login complete")


def add_name():
    redactor = browser.find_element_by_xpath(Paths.name_redactor).click()
    name_field = browser.find_element_by_xpath(Paths.name_field).send_keys('name')
    change = browser.find_element_by_xpath(Paths.name_save).click()


def add_surname():
    redactor = browser.find_element_by_xpath(Paths.surname_redactor).click()
    surname_field = browser.find_element_by_xpath(Paths.surname_field).send_keys('surname')
    change = browser.find_element_by_xpath(Paths.surname_save).click()


def add_phone():
    redactor = browser.find_element_by_xpath(Paths.phone_redactor).click()
    phone_field = browser.find_element_by_xpath(Paths.phone_field).send_keys('010555555')
    change = browser.find_element_by_xpath(Paths.phone_save).click()


def step2():
    global patient
    body = browser.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_UP)
    time.sleep(2)
    hishel = browser.find_element_by_name("visit_save").click()
    clickerbyXpath('/html/body/div[14]/div[3]/div/button')  # ok
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.75)
    clickerbyXpath(Paths.andznakan_tvyalner)  # andznakan tvyalner
    clickerbyXpath(Paths.next)  # next
    clickerbyXpath(Paths.oragir)  # oragir
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    clickerbyXpath(Paths.artaqin_ughegrum)  # artaqin ughegrum
    time.sleep(1)
    senderbyXpath(Paths.bujhastatutyun, 'Նատալի ֆարմ ՍՊԸ Աստղիկ բժշկական կենտրոն')
    try:
        time.sleep(1)
        browser.find_element_by_xpath(Paths.nataly_pharm).click()
    except:
        try:
            time.sleep(1)
            browser.find_element_by_xpath(Paths.nataly_test).click()
        except:
            x = input("nataly pharm error")
    senderbyXpath(Paths.ughordman_tip, 'Լաբորատոր-գործիքային հետազոտություն')
    try:
        time.sleep(1)
        browser.find_element_by_xpath(Paths.laborator_gorciqayin).click()
    except:
        try:
            time.sleep(1)
            browser.find_element_by_xpath(Paths.laborator_gorciqayin_test).click()
        except:
            x = input("laborator gortsiqayin error")

    senderbyXpath(Paths.nmusharman_npatak, 'Այլ')
    try:
        time.sleep(1)
        browser.find_element_by_xpath(Paths.ayl).click()
    except:
        try:
            time.sleep(0.5)
            browser.find_element_by_xpath(Paths.ayl_test).click()
        except:
            ok = input("ayl error")

    clickerbyXpath(Paths.teghakayum)  # teghakayum
    time.sleep(1)
    try:
        time.sleep(1)
        browser.find_element_by_xpath(Paths.ptichka_test).click()
    except:
        try:
            time.sleep(0.5)
            browser.find_element_by_xpath(Paths.ptichka).click()
        except:
            x = input("ptichka error !")
    # clickerbyXpath(Paths.ptichka)#ptichka
    time.sleep(1)
    clickerbyXpath(Paths.manualy)  # manualy
    try:
        browser.find_element_by_css_selector(Paths.location_hastatel).click()
    except:
        try:
            browser.find_element_by_xpath(Paths.location_2).click()
        except:
            ok = input("hastatel error")
    # clickerbyXpath(Paths.location_hastatel) #hastatel
    body.send_keys(Keys.PAGE_DOWN)
    senderbyXpath(Paths.carayutyun, 'nCov-2019 ՌՆԹ-ի հայտնաբերում')
    try:
        time.sleep(0.5)
        browser.find_element_by_xpath(Paths.rnt_haytnaberum).click()
    except:
        try:
            browser.find_element_by_xpath(Paths.rnt_2).click()
        except:
            ok = input("rnt haytnaberman error")
    # clickerbyXpath(Paths.rnt_haytnaberum) #carayutyun
    clickerbyXpath(Paths.finaly_hishel)  # hishel
    try:
        time.sleep(10)
        browser.find_element_by_xpath(Paths.finaly_ok).click()
    except:
        try:
            browser.find_element_by_xpath(Paths.finaly_ok_2).click()
        except:
            ok = input("please click ok ")
    #clickerbyXpath(Paths.finaly_ok) #verjnakan ok
    body.send_keys(Keys.PAGE_UP)
    time.sleep(1)
    clickerbyXpath(Paths.ayceri_avart)  # ayceri ej veradarnal
    browser.refresh()
    time.sleep(2)


def step1():
    name_path = checker(Paths.name_path)
    latin_name = browser.find_element_by_xpath(name_path).text
    if len(latin_name[18:]) < 3:
        add_name()
    surname_path = checker(Paths.surname_path)
    latin_surname = browser.find_element_by_xpath(surname_path).text
    if len(latin_surname[22:]) < 4:
        add_surname()
    try:
        browser.find_element_by_xpath(Paths.inqnamekusacum_ok).click()
    except Exception:
        pass
    phone_path = checker(Paths.phone_path)
    phone = browser.find_element_by_xpath(phone_path).text
    if len(phone[9:]) < 3:
        add_phone()
    clickerbyXpath(Paths.depqi_tesak)  # depqi tesak
    time.sleep(0.5)
    clickerbyXpath(Paths.ambulator)  # ambulator
    try:
        browser.find_element_by_xpath(Paths.inqnamekusacum_ok).click()
    except Exception:
        pass
    clickerbyXpath(Paths.npatak)  # npatak
    clickerbyXpath(Paths.hivandutyun)  # hivandutyun
    num = (random.randint(1000000000, 99999999990))
    senderbyXpath(Paths.depqi_hamar, num)  # depqi Hamar
    clickerbyXpath(Paths.finans_aghbyur)  # finans axbyur
    clickerbyXpath(Paths.vcharovi)  # vcharovi
    body = browser.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    clickerbyXpath(Paths.akhtoroshum)  # akhtoroshum
    clickerbyXpath(Paths.bjishkner)  # bjishkner
    clickerbyXpath(Paths.ughekcox)  # ughekcox
    senderbyXpath(Paths.covid_field, "[B97.2] Կորոնավիրուսներ")
    clickerbyXpath(Paths.corona)  # corona
    clickerbyXpath(Paths.covid_hastatum)  # hastatel
    time.sleep(0.5)
    try:
        ok = browser.find_element_by_xpath(Paths.covid_ok).is_displayed()
        clickerbyXpath(Paths.covid_ok)  # ok
        clickerbyXpath(Paths.cheghyal)
        clickerbyXpath(Paths.arka)  # arka
        senderbyXpath(Paths.arka_corona, 'B97.2 Կորոնավիրուսներ')
        try:
            time.sleep(0.5)
            browser.find_element_by_xpath('/html/body/div[24]/div[2]/div').click()
        except:
            covid = browser.find_elements_by_xpath('/html/body/div[24]/div[2]')  # corona
            time.sleep(1)
            covid.__getitem__(0).click()
        clickerbyXpath(Paths.corona_click)
    except Exception as E:
        print(E.__context__)
    clickerbyXpath(Paths.add_doctor)  # avelacnel bjishk
    senderbyXpath(Paths.doctor_field, "Նազելի Աղաբեկյան Բժիշկ-բջջաբան")
    clickerbyXpath(Paths.doctor)  # bjishk
    time.sleep(0.5)
    clickerbyXpath(Paths.doctor_hastatum)  # hastatum
    step2()


def finduser(info):
    clickerbyXpath(Paths.add_patient)
    senderbyXpath(Paths.info_field, info)
    time.sleep(1)
    man = browser.find_elements_by_xpath(Paths.patients)
    try:
        time.sleep(0.8)
        man.__getitem__(0).click()
    except:
        try:
            time.sleep(0.5)
            browser.find_element_by_xpath('/html/body/div[8]/div[1]/div/div').click()
        except:
            print("please click on the patient ")
    id_path = checker(Paths.patient_id)
    id = browser.find_element_by_xpath(id_path).text
    global user_id
    user_id = id[5:15]
    step1()

browser = webdriver.Chrome()
browser.get("https://www.armed.am/am")
id = input('enter verification code:\n')
login('HovhannisyanAnul@mail.ru', 'hanul123456', id)
i = 1
with open('Patients.txt') as f:
    patients = f.read().split('\n')
    print(patients)


def start_text_file():
    for i in range(len(patients)):
        if len(patients) < 1:
            return True
        try:
            browser.find_element_by_css_selector(Paths.partq_ok).click()
        except:
            pass
        finduser(patients[i])
        print(patients[i], " added successfully")
    print("list added successfully aper jan :)")


def start_only_user():
    while True:
        info = input("input info about user\n")
        try:
            browser.find_element_by_css_selector(Paths.partq_ok).click()
        except:
            pass
        finduser(info)
        if info == "esc":
            break

start_only_user()
