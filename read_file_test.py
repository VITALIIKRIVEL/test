##f = open("C:/Automation_test/Python_progs.txt")
##f.read()

import pyautogui
import time

with open('/home/compacs/Cmp7Data/Automation_test/Python_progs.txt', 'r', encoding='utf-8') as f:
    lst = f.read().splitlines()
    print(lst)

# удаляем лишние строки MoveEvent . Если до и после записи существует пять таких же MoveEvent, тогда удаляем элемент

lstTmp = []

# удаляем лишние MoveEvent
for n in range(6, len(lst) - 6):
    if(lst[n-5].__contains__('MoveEvent')
            and lst[n+5].__contains__('MoveEvent')
            and lst[n-4].__contains__('MoveEvent')
            and lst[n+4].__contains__('MoveEvent')
            and lst[n-3].__contains__('MoveEvent')
            and lst[n+3].__contains__('MoveEvent')
            and lst[n-2].__contains__('MoveEvent')
            and lst[n+2].__contains__('MoveEvent')
            and lst[n-1].__contains__('MoveEvent')
            and lst[n+1].__contains__('MoveEvent')
            and lst[n].__contains__('MoveEvent')):

        lstTmp.append(lst[n])

for m in range(0, len(lstTmp)):
    lst.remove(lstTmp[m])

# удаляем лишние MoveEvent/

 #   print(len(lst))

#цикл разобра записей по типам событий
#time.sleep(5) #пауза, чтобы успеть перевести фокус ввода в нужное приложение

listAllEvents =[]

for i in range(0, len(lst)):

      rawTimeEvent = lst[i].split('time=')[1]
      rawTimeEvent = rawTimeEvent.replace(")", '')
    #  print('timeEvent ' + rawTimeEvent)

      floatTimeEvent = float(rawTimeEvent)
   #   print('floatTimeEvent ' + str(floatTimeEvent))

      rawTimeEventPrevious = lst[i - i].split('time=')[1]
      rawTimeEventPrevious = rawTimeEventPrevious.replace(")", '')

      if(i==0):
         rawTimeEventPrevious = rawTimeEvent

      floatTimeEventPrevious = float(rawTimeEvent)

      if(lst[i].__contains__('KeyboardEvent') and lst[i].__contains__('up')):   #('KeyboardEvent(n, up, ', 'time=1611207358.3693032')
          lstTmp1 = lst[i].split('time=')
          lstTmp1[1] = lstTmp1[1].replace(')', '')
      #    print(lstTmp1)

          rawTmpFirstElem = lstTmp1[0]
          rawTmpFirstElem = rawTmpFirstElem.replace("KeyboardEvent(", '')
       #   print(rawTmpFirstElem)

          listRawTmpFirstElem = rawTmpFirstElem.split(',')
       #   print(listRawTmpFirstElem[0])

          listAllEvents.append(['KeyboardEvent', listRawTmpFirstElem[0], float(lstTmp1[1])])
          #нажимаем клавишу
          # pyautogui.press(listRawTmpFirstElem[0])
          # time.sleep(0.5)



      if(lst[i].__contains__('MoveEvent')):  #('MoveEvent(x=985, y=883, ', 'time=1611207360.9328158')
          lstTmp2 = lst[i].split('time=')
          lstTmp2[1] = lstTmp2[1].replace(')', '')

          rawTmpFirstElemMove = lstTmp2[0]
          rawTmpFirstElemMove = rawTmpFirstElemMove.replace("MoveEvent(", '')

          listRawTmpMoveFirstElem = rawTmpFirstElemMove.split(',')

         # print(listRawTmpMoveFirstElem)

          raw_x = listRawTmpMoveFirstElem[0].replace('x=', '')
          raw_y = listRawTmpMoveFirstElem[1].replace(' y=', '')

          listAllEvents.append(['MoveEvent', int(raw_x), int(raw_y), float(lstTmp2[1])])
 #         pyautogui.moveTo(int(raw_x), int(raw_y))
 #         #двигаем курсор

      if(lst[i].__contains__('ButtonEvent') and lst[i].__contains__('up')): #("ButtonEvent(event_type='up', button='right', ", 'time=1611223260.7421203')
                                              #("ButtonEvent(event_type='up', button='left', ", 'time=1611223266.18212')
          lstTmp3 = lst[i].split('time=')
          lstTmp3[1] = lstTmp3[1].replace(')', '')

          rawTmpFirstElemButton = lstTmp3[0]
          rawTmpFirstElemButton = rawTmpFirstElemButton.replace("(\"ButtonEvent(", '')

          listRawTmpButtonFirstElem = rawTmpFirstElemButton.split(',')

      #    print(listRawTmpButtonFirstElem)

          buttonType = listRawTmpButtonFirstElem[1]

          print(buttonType)

          if(buttonType.__contains__('right')):
              listAllEvents.append(['ButtonEvent', 'right', float(lstTmp3[1]) ])
              #нажимаем правую клавишу мыши
 #             pyautogui.click(button='right')

          if(buttonType.__contains__('left')):
              listAllEvents.append(['ButtonEvent', 'left', float(lstTmp3[1])])
              #нажимаем левую клавишу мыши
  #            pyautogui.click(button='left')


for i in range(0, len(listAllEvents)):

          if (listAllEvents[i][0].__contains__('KeyboardEvent')):
          # нажимаем клавишу
            pyautogui.press(listAllEvents[i][1])

          if (listAllEvents[i][0].__contains__('MoveEvent')):
          # двигаем курсор
            pyautogui.moveTo(listAllEvents[i][1], listAllEvents[i][2])

          if (listAllEvents[i][0].__contains__('ButtonEvent')):
          #нажимаем правую клавишу мыши
              if (listAllEvents[1].__contains__('left')):
                   pyautogui.click(button='right')
              else:
                   pyautogui.click(button='left')

              time.sleep(1)

#         нажимаем левую клавишу мыши
#         pyautogui.click(button='left')