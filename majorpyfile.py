import smtplib
import os

#file = open('ps-aux.txt', 'a')
os.system("ps aux | grep java > ps-aux.txt")
#file.write(os.system("ps aux|grep java"))
list_for_pid = list()
list_for_CPU = list()
list_for_Memory = list()
list_for_last_5_values_for_CPU = list()
list_for_last_5_values_for_Memory = list()
list_for_sending_last_5_values = list()
message = ""
email = "500053079@stu.upes.ac.in"
threshold = 8
flag = 0
with open("ps-aux.txt") as infile:
    for line in infile:
        list_for_pid.append(line.split()[1])
        list_for_CPU.append(line.split()[2])
        list_for_Memory.append(line.split()[3])
    #print(list_for_CPU)
    #print(list_for_Memory)
    for ele in range(0,len(list_for_pid)):
        list_for_pid[ele] = (int)(list_for_pid[ele])
    for ele in range(0,len(list_for_CPU)):
       list_for_CPU[ele] = (float)(list_for_CPU[ele])  #coz Strings k form meh store horaha list meh and hume integer chahye
       #print(list_for_CPU[ele])
    for ele in range(0, len(list_for_Memory)):
       list_for_Memory[ele] = (float)(list_for_Memory[ele])
       #print(list_for_Memory[ele])
    sum1 = round(sum(list_for_CPU),2)    #for list of CPU
    sum2 = round(sum(list_for_Memory),2)    #list for Memory
    file_for_storing_threshold = open("threshold.txt","a+")
    file_for_storing_threshold.write((str)(sum1))
    file_for_storing_threshold.write("\t")
    file_for_storing_threshold.write((str)(sum2))
    file_for_storing_threshold.write("\n")
    file_for_storing_threshold.close()
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("121827@gmail.com", "mish31")
# message to be sent
if sum1 >= threshold and sum2 <threshold:
    max_consume = max(list_for_CPU)
    index = list_for_CPU.index(max_consume)
    process_id = list_for_pid[index]
    with open("threshold.txt") as infile:
        for line in infile:
            list_for_last_5_values_for_CPU.insert(len(list_for_last_5_values_for_CPU),line.split()[0])  #insert coz order maintain krna h
        list_for_last_5_values_for_CPU.append(sum1)
    #print(len(list_for_last_5_values_for_CPU))
    if len(list_for_last_5_values_for_CPU) >=5:
        #print("True")
        for i in list_for_last_5_values_for_CPU[-5:]:
           #print("juhhhhh",i)
           list_for_sending_last_5_values.append(i)
    elif (len(list_for_last_5_values_for_CPU) >=2) and (len(list_for_last_5_values_for_CPU) <=4):
        list_for_sending_last_5_values.append(list_for_last_5_values_for_CPU)
    else:
        list_for_sending_last_5_values.append("Already exceeding threshold")
    message = f"you are exceeding the CPU threshold and process responsible is {process_id} and the last few values including the current value of CPU usage are{list_for_sending_last_5_values}"
    open('threshold.txt','w').close()
elif sum2 >= threshold and sum1 < threshold:
    max_consume = max(list_for_Memory)
    index = list_for_Memory.index(max_consume)
    process_id = list_for_pid[index]
    with open("threshold.txt") as infile:
        for line in infile:
            list_for_last_5_values_for_Memory.insert(len(list_for_last_5_values_for_Memory),line.split()[1])  #insert coz order maintain krna h
        list_for_last_5_values_for_Memory.append(sum2)
    #print(len(list_for_last_5_values_for_CPU))
    if len(list_for_last_5_values_for_Memory) >=5:
        #print("True")
        for i in list_for_last_5_values_for_Memory[-5:]:
           #print("juhhhhh",i)
           list_for_sending_last_5_values.append(i)
    elif (len(list_for_last_5_values_for_Memory) >=2) and (len(list_for_last_5_values_for_Memory) <=4):
        list_for_sending_last_5_values.append(list_for_last_5_values_for_Memory)
    else:
        list_for_sending_last_5_values.append("Already exceeding threshold")
    print(list_for_last_5_values_for_Memory)
    print(list_for_sending_last_5_values)
    message = f"You are exceeding the Memory threshold and the process consuming most CPU is {process_id} and the last few values including the current value of Memory usage are {list_for_sending_last_5_values}"
    open('threshold.txt', 'w').close()
elif sum1 >= threshold and sum2 >=threshold:     #If both are exceeeding threshold
    list_for_sending_last_5_values_for_CPU = list()
    list_for_sending_last_5_values_for_Memory = list()
    max_consume1 = max(list_for_CPU)
    index1 = list_for_CPU.index(max_consume1)
    process_id1 = list_for_pid[index1]
    with open("threshold.txt") as infile:
        for line in infile:
            list_for_last_5_values_for_CPU.insert(len(list_for_last_5_values_for_CPU),line.split()[0])  #insert coz order maintain krna h
        list_for_last_5_values_for_CPU.append(sum1)
    #print(len(list_for_last_5_values_for_CPU))
    if len(list_for_last_5_values_for_CPU) >=5:
        #print("True")
        for i in list_for_last_5_values_for_CPU[-5:]:
           #print("juhhhhh",i)
           list_for_sending_last_5_values_for_CPU.append(i)
    elif (len(list_for_last_5_values_for_CPU) >=2) and (len(list_for_last_5_values_for_CPU) <=4):
        list_for_sending_last_5_values_for_CPU.append(list_for_last_5_values_for_CPU)
    else:
        list_for_sending_last_5_values_for_CPU.append("Already exceeding threshold")
    max_consume2 = max(list_for_Memory)
    index2 = list_for_Memory.index(max_consume2)
    process_id2 = list_for_pid[index2]
    with open("threshold.txt") as infile:
        for line in infile:
            list_for_last_5_values_for_Memory.insert(len(list_for_last_5_values_for_Memory),line.split()[1])  #insert coz order maintain krna h
        list_for_last_5_values_for_Memory.append(sum2)
    #print(len(list_for_last_5_values_for_CPU))
    if len(list_for_last_5_values_for_Memory) >=5:
        #print("True")
        for i in list_for_last_5_values_for_Memory[-5:]:
           #print("juhhhhh",i)
           list_for_sending_last_5_values_for_Memory.append(i)
    elif (len(list_for_last_5_values_for_Memory) >=2) and (len(list_for_last_5_values_for_Memory) <=4):
        list_for_sending_last_5_values_for_Memory.append(list_for_last_5_values_for_Memory)
    else:
        list_for_sending_last_5_values_for_Memory.append("Already exceeding threshold")
    message = f"You are exceeding the Memory threshold as well CPU threshold and the process consuming most Memory is {process_id2} and the last few values including current value of Memory usage are{list_for_sending_last_5_values_for_Memory} and the process consuming most CPU is {process_id1} and the last few values including the current value of CPU usage are {list_for_sending_last_5_values_for_CPU}"
    open('threshold.txt', 'w').close()
# sending the mail
s.sendmail("121827@gmail.com", email, message)
# terminating the session
s.quit()