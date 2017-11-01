#Sandra Dögg Kristmundsdóttir

from tkinter import *
import re
import time
#global apples
#global gold
#gold = 0
#apples = 0
#valmynd
val = 0
while val != "11":
    print ("1. Kennitala")
    print ("2. Index" )
    print ("3. Match Month")
    print ("4. liður 4")
    print ("5. Svör")
    print ("6. Konni")
    print ("7. Útskýring")
    print ("8. Konni2")
    print ("9. Forrit")
    print ("10. Eplaleikur")
    print ("11. Hætta" )
    val = input ("Veldu lið ")


#liður1
    if val == "1":
        print("\nKennitala")
        str = input("Skrifaðu Kennitölu: ")
        result = re.match("^(0[1-9]|[12][0-9]|3[01]){1}(0[1-9]|1[0-2]){1}[0-9]{5}[89]{1}", str)
        print(result)


#liður 2
    if val == "2":
        print("\nIndex")
        stafir_og_tolur = "abc 123 def 456 ghjk 7890 lm 12 nop 345 q 6 rstuv 78901 xyz 234"
        for m in re.finditer ( "\d+", stafir_og_tolur ):
            print (m.group (0))
            print ("start index:", m.start())



#liður 3
    if val == "3":
         print("\nMatchMonth")
         my_regex = 'April|May|June|Dec*'
         matches = re.findall (my_regex, "March, April 29, May 5, June 15, August, Dec 8")
         for match in matches:
             print ("Match month: %s" % (match))


#liður 4
    if val == "4":
         print("\nliður 4")
         list = [ "March", "April 29", "May 5", "June 15", "August", "Dec 8" ]
         for element in list:
            m = re.match ('April|May|June|Dec*', element)
             # See if success.
            if m:
                print (m)

#liður 5

    if val == "5":
        print("\nSvör")
        print("Svörin eru geymd í txt document.")
#liður 6
    if val == "6":
        print("\nKonni")
        def Fall_1():
            konni = 20
            def Fall_2():
                konni = 30
                print("konni =",konni)
            Fall_2()
            print("konni =",konni)
        konni = 10
        Fall_1()
        print("konni =",konni)

#Liður 7
    if val == "7":
        print("Viltu vita hvernig python geymir gogn? ")
        svar = input("veldu J/N")
        if "J":
            ellefu = 11
            tolf = 12
            threttan = 13

            print (id(ellefu))
            print (id(tolf))
            print (id(threttan))
            print("Python geymir hluti í minni id functionið er notað til að sjá hvar í minninu python geymir hlutin.")
        else:
            print("okei, bæ bæ")



#liður 8
    if val == "8":
        print("\nKonni2")
        konni = 40
        def Fall_1():
            global konni
            konni = 20
            def Fall_2():
                global konni
                konni = 30
                print("konni =",konni)
            Fall_2()
            print("konni =",konni)
        Fall_1()
        print("konni =",konni)






#liður 9
    if val == "9":
        def printname():
            texti = entry_1.get ()
            texti2 = entry_2.get ()
            utkoma = float ( texti ) + float ( texti2 )
            label_4.configure ( text=utkoma )
            print ( "útkoman er ", utkoma )


        root = Tk ()
        label_1 = Label ( root, text="sláðu inn tölu eitt " )
        label_2 = Label ( root, text="sláðu inn tölu tvö" )
        label_3 = Label ( root, text="Tölurnar Lagðar Saman " )
        texti = StringVar ()
        texti2 = StringVar ()
        entry_1 = Entry ( root, textvariable=texti )
        entry_2 = Entry ( root, textvariable=texti2 )
        texti = entry_1.get ()
        label_4 = Label ( root, text="" )
        label_1.grid ( row=0, sticky=E )
        label_2.grid ( row=1, sticky=E )
        label_3.grid ( row=3, sticky=E )
        entry_1.grid ( row=0, column=1 )
        entry_2.grid ( row=1, column=1 )
        label_4.grid ( row=3, column=1 )

        button_1 = Button ( root, text=" Leggja Saman ", command=printname )
        button_1.grid ( columnspan=2 )
        root.mainloop ()

#Liður 10
#    if val == ("10"): #virkar ekki veit ekki afhverju..
#        def start():
#            print("Hæ og Velkomin/nn!")
#            nafn = input ("Hvað er nafnið þitt?:")
#            print("Velkomin/nn, ", nafn, "!")
#            print("Það sem þessi leikur snýst um er að safna eplum.")
#            print("Eftir að hafa safnað nokkrum eplum getiru selt þau")
#           choice = input("Viltu spila leikinn Y/N?")
#            if choice == "Y":
#                begin()
#            if choice == "N":
#                print("okei, bæ...")
#        def begin():
#            global apples
#            global gold
#            print("Nú skulum við byrja!")
#            if gold > 99:
#                print("Þú Hefur unnið leikinn!")
#                play = input("Viltu spila leikinn aftur? Y/N")
#                if play == ("Y"):
#                    begin()
#                if play == ("N"):
#                    print("Tilhamingju aftur!")
#            pick = input("Viltu týna upp eplið Y/N")
#            if pick == ("Y"):
#                time.sleep(1)
#                print("Þú týndir upp epli.")
#                apples=apples+1
#                print("Þú ert núna með, ", apples, " epli")
#                begin()
#            if pick == ("N"):
#                sell = input("Viltu selja eplinn þín Y/N?")
#                if sell == ("Y"):
#                    global gold
#                    global apples
#                    print("Þú ert eins og er með, ", apples, "epli.")
#                    print("Þú hefur selt eplin þín.")
#                    gold=apples*10
#                    apples=0
#                    print("Þú ert núna með svona mikið gull:", gold)

