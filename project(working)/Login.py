import face_recognition # type: ignore
import cv2
import numpy as np
import os
import xlwt # type: ignore
from xlwt import Workbook # type: ignore
from datetime import date
import xlrd, xlwt # type: ignore
from xlutils.copy import copy as xl_copy # type: ignore
from datetime import datetime

c_time = datetime.now()

f_time = c_time.strftime('%I:%M:%S %p')
CurrentFolder = os.getcwd() 
image = CurrentFolder+'\\shaik.png'
image2 = CurrentFolder+'\\ameen.png'



video_capture = cv2.VideoCapture(0)

person1_name = "Sahil"
person1_image = face_recognition.load_image_file(image)
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

person2_name = "Ameen"
person2_image = face_recognition.load_image_file(image2)
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

known_face_encodings = [
    person1_face_encoding,
    person2_face_encoding
]
known_face_names = [
    person1_name,
    person2_name
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True) 
wb = xl_copy(rb)
inp = input('Please give current subject lecture name')
sheet1 = wb.add_sheet(inp)
sheet1.write(0, 0, 'Name')
sheet1.write(0, 1, str(date.today()))
sheet1.write(0, 2,"Time")
row=1
col=0
already_attendence_taken = ""
while True:
            ret, frame = video_capture.read()

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                    if((already_attendence_taken != name) and (name != "Unknown")):
                        sheet1.write(row+1, 0, name )
                        sheet1.write(row+1, 1, "Present" )
                        print("attendence taken")
                        sheet1.write(row+1,2,f_time)
                        wb.save('attendence_excel.xls')
                        already_attendence_taken = name
                    else:
                        print("NEXT STUDENT")
                        break
                        
            process_this_frame = not process_this_frame


            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            k = cv2.waitKey(1)
            if k%256 == 27:   
                print("data save")
                break

video_capture.release()
cv2.destroyAllWindows()