#Kingdoms and Emblems Dictonary
kingdoms_and_Emblems_dict = {"LAND" : "PANDA", "AIR" :"OWL", "WATER" : "OCTOPUS","FIRE":"DRAGON","ICE":"MAMMOTH"}

#Message Wheel
wheel = []
for i in range(65 , 91):
    wheel.append(chr(i)) 
message_sended_kingdomes_list = "SPACE " 

#Reading Number of Inputs
number_of_input=[]
while(True):
        try:
            a=input()
        except Exception as e:
            break
        number_of_input.append(a)
if (len(set(number_of_input)) < 3):
    print("NONE")
else:
    #Extract First and Remaining Part
    for each in number_of_input:
        input_list = each.split()
        ruler_list = input_list[0]
        ruler = ruler_list.upper()
        emblem_list = ''
        for word in input_list[1:]:
            emblem_list += word
            emblem = emblem_list.upper()
        decrypt_msg_letter_list = []
        comapre_list = []
        count_original_lett_dict = {}
        count_decrypt_lett_dict = {}
        #Decrypt the Message
        for each in emblem:
           ruler_length = len(kingdoms_and_Emblems_dict[ruler])
           decrypt_msg_letter_list.append(wheel[wheel.index(each) - ruler_length])
        for each in kingdoms_and_Emblems_dict[ruler]:
            count_original_lett_dict[each] = kingdoms_and_Emblems_dict[ruler].count(each)
            count_decrypt_lett_dict[each] = decrypt_msg_letter_list.count(each)
        
        v1_list = list(count_original_lett_dict.values())
        v2_list = list(count_decrypt_lett_dict.values())
        
        #Check Length of original emblem letters in encrypted Message
        for i in range(len(v1_list)):
            if(v2_list[i] < v1_list[i]):
                comapre_list.append('No')
            else:
                comapre_list.append("Yes")
        if ("No" in comapre_list):
            message_sended_kingdomes_list+= ""
        else:
            message_sended_kingdomes_list += ruler + " "
    if (len(message_sended_kingdomes_list) < 3):
        print("NONE")
    else:
        print(message_sended_kingdomes_list)