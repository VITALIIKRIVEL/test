import threading
import pynput
import mouse
import keyboard

mouse_events = []

# mouse_events = mouse.record('rigth','down')

mouse.hook(mouse_events.append)
keyboard.start_recording()

keyboard.wait("esc")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()

# mouse.click('right')
# mouse_events =

file_event = open("/home/compacs/Cmp7Data/Automation_test/Python_progs.txt", "w")

# Keyboard threadings:
# k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
# k_thread.start()

# Mouse threadings:

#m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
#m_thread.start()
#waiting for both threadings to be completed

#mouse.ButtonEvent

#k_thread.join() 
#m_thread.join()

listKeyboardEvent = []
listMouseEvent = []
for i in range(0, len(keyboard_events)):
     if keyboard_events[i].event_type == "up":
          listKeyboardEvent.append("KeyboardEvent(" +
              keyboard_events[i].name + ', ' +
              keyboard_events[i].event_type + ', ' + 'time=' +
              str(keyboard_events[i].time) + ')')
         
     
   
for i in range(0, len(mouse_events)):
##          print(str(mouse_events[i]))
          listMouseEvent.append(str(mouse_events[i]))

sorted_list_keyboard = []
sorted_list_mouse = []

#получается уже пригодный, отсортированный по времени
common_events_list = listKeyboardEvent + listMouseEvent

# collectionEvent = {}  #набор для событий. ключ - время события
#
# listTmp2 = []
#
# for i in range(0, len(common_events_list)):
# #     file_event.write(str(common_events_list[i]) + '\n')
#      listOfCurString = common_events_list[i].split('time=')
#      firstElemOfList = listOfCurString[0]
#      secondElemOfList = listOfCurString[1]
#      secondElemOfList = secondElemOfList.replace(')', '')
#
#      collectionEvent[firstElemOfList] = 'time=' + secondElemOfList   #ПРОПАДАЮТ ЭЛЕМЕНТЫ СПИСКА!!!
#      #listTmp2.append()
#     # listTmp = list(collectionEvent.items())
#    #  listTmp.sort(key=lambda i: i[1])
#
#      print("listOfCurString: " + listOfCurString[0] + listOfCurString[1])
#      print("firstElemOfList: " + firstElemOfList)
#      print("secondElemOfList: " + secondElemOfList)
#
# #  collectionEvent[] =
#      print(str(common_events_list[i]) + '\n')
#
# listTmp = list(collectionEvent.items())

#сортировка списка по времени
# listTmp.sort(key=lambda i: i[1])
#
# for i in range(0, len(listTmp)):
#    file_event.write(str(listTmp[i]) + '\n')

# listUnsorted = {}
#
# common_events_list.sort(key=lambda i: i[1])

common_events_list_splitted = []

for i in range(0, len(common_events_list)):
    curStrList = common_events_list[i].split('time=')
    curStrList[1].replace(')', '')
    common_events_list_splitted.append([curStrList[0], curStrList[1]])

def custom_key(list):
    return list[1]

common_events_list_splitted.sort(key=custom_key)

for i in range(0, len(common_events_list_splitted)):
    common_events_list_splitted[i] = str(common_events_list_splitted[i][0]) + 'time=' + str(common_events_list_splitted[i][1])

for i in range(0, len(common_events_list)):
    file_event.write(str(common_events_list_splitted[i]) + '\n')





file_event.close()



##   if mouse_events[i] == mouse.ButtonEvent:
##          print("Mouse_Event",
##           str(mouse_events[i]),
##           "null",
##           "null",
##           mouse_events[i].time)

##   if mouse_events[i] == mouse.MoveEvent:
##     print("Mouse_Event",
##           str(mouse_events[i]),
##           mouse_events[i].x,
##           mouse_events[i].y,
##           mouse_events[i].time)
