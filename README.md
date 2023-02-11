# attendance-using-face-recognition
python project to take attendance in schools and universities  
#--------important-------
to run this project you need to install some python lib's 
1-cmake 2-dlib 3-opencv 4-openpyxl 5-tkinker 6-smtp
you can use this command in terminal to intall any lib   (pip install libraryName ) 

The idea of the system is to read the faces of the students, if system does not read the face of the student, then this means that the student is absent, so the program records his absence on today’s date, and the system sends an email alerting the student that he has been registered as absent in this course and the number of absences that the student has, and the system uploads the absence file to the firebase, and the teacher can follow up Absences through a website of the system connected to FireBase, where the teacher can upload the student names file and download the absences file
