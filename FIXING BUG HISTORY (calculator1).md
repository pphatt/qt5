-- 1/1/2022 12:51pm --

* fix error integer

* fix all number: 
               

        if len(self.lst) == 0:
            self.ui.displaycalculator.setText("0")
            self.count += 1
            self.lst += "0"

        elif len(self.lst) > 0:
            self.ui.displaycalculator.setText(text + "0")
            self.count += 1
            self.lst += "0"


debug script: 0 (+ / - / * / div) NUMBER AT THE BEGINNING CALCULATION -> 0 + 1 = 1

* 0 + 1 WILL DISPLAY ON DISPLAYCALCULATOR 

debug script: TWO ANS 00 (+ / - / * / div) SOMETHING -> EX: HISTORY WILL DISPLAY 00 + 1 = 1


-- 1/2/2022 12:00pm --

* FIXING DELETE ONE BY ONE ON OPERATOR " + ": IT WILL DELETE ALL THE OPERATOR

* FIXING TWO OPERATOR IN A ROW.
Code: 

        elif self.lst[-2] == "+" or self.lst[-2] == "-" or self.lst[-2] == "*" or self.lst[-2] == "/":
            pass