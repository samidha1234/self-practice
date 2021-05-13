my_string= "sami"
input_string="sfdkhgdsakfadsfsamisfddaf"

for j in range(len(input_string)):
    result= []
    for i in range(len(my_string)):
        if my_string[i] == input_string[j]:
            j = j+1
            result.append(my_string[i])
            print(result)
            continue
        break


    # if my_string[s] in out_dict:
    #     print("Ifffff",out_dict[s])
    #     count = out_dict[my_string[s]] +1
    #     out_dict.update({my_string[s]:count})        
    # else :
    #     print("Else", out_dict[my_string[s])
    #     out_dict.update({my_string[s] :1})
    # print(out_dict)


# A = {1:3,2:4,3:5}
# B = A-----> {1:3,2:4,3:5}
# C = tuple(A.items())---->((1,3),(2,4),(3,5))
# for i,j in C:
# ___B[j] = i 
# print(A)


# my_list = [1,2,3,4]
# print(my_list[::-1]) ---->4,3,2,1 ??
# print(my_list[-1])----> 4,3,2,1
# print(my_list[-10])----> out of index
# print(my_list[:10]) ---> 1,2,3,4
# print(my_list[3:1:-1]) ---> 4,3,2