
def webomat_audi():

        from selenium import webdriver
        from time import sleep

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://www.google.com/xhtml')

        search_box = driver.find_element_by_name('q')
        search_box.send_keys('abc')
        search_box.submit()
        # driver.execute_script("scrollBy(0,50);")
        # time.sleep(2) # Let the user actually see something!
        # driver.get('http://www.psframe.cz')
        # time.sleep(2) # Let the user actually see something!
        #
        # driver.get('http://www.psframe.cz/kontakt')
        #
        #
        # search_box1 = driver.find_element_by_name('submitted[jmeno]')
        # search_box1.send_keys('David Pflanzer')
        # search_box1.submit()
        #
        # search_box2 = driver.find_element_by_name('submitted[e_mail]')
        # search_box2.send_keys('info@psframe.cz')
        # search_box2.submit()
        #
        # driver.execute_script("scrollBy(0,350);")
        #
        #
        # search_box3 = driver.find_element_by_name('submitted[telefon]')
        # search_box3.send_keys('+420 775 582 626')
        # search_box3.submit()
        #
        # search_box4 = driver.find_element_by_name('submitted[vase_zprava]')
        # search_box4.send_keys('Ahoj Davide, potrebuju pucit leseni, ozvi se :) ja letim ')
        #
        # time.sleep(5) # Let the user actually see something!

        sleep(1)
        driver.quit()


        #jmeno = driver.find_element_by_name('                ')
        #jmeno.send_keys('')
        #heslo = driver.element_by_id('          ')
        #heslo.send_keys('feedhslO')
        #cudlikS = driver.find_element_by_name('          ').click()
        #cudlikO = driver.find_element_by_name('          ').click()


webomat_audi()
