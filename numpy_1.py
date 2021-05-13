# def string_splosion(str):
#     new_str=''
#     for s in range (1,len(str)+1):
#         for i in range(s):
#             new_str= new_str+str[i]
#     print (new_str)
        
# in_str= input("enter your string : ")
# string_splosion(in_str)

# def array_count9(nums):
#     count= 0
#     for i in range(0,len(nums)):
#         # print(nums[i])
#         if nums[i] == 9:
#             count += 1
#     return count

# a=array_count9([1,2,9,4,9])
# print(a)

# def array123(nums):
#     s=[1,2,3]
#     for i in range(len(nums)):
#         for j in range(len(s)):
#             if s[j] == nums[i]:
#                 i=i+1
#                 continue
#             else:
#                 break
#             print(s[j])
#         return s[j]
            

# a= array123([1,4,3,1,3,7,8])
# print(a)

# nums = [1,4,3,1,2,3,7,8]
# s = [1,2,3]
# for i in range(len(nums)):
#     for j in range(len(s)):
#         if s[j] == nums[i]:
#             i=i+1
#             print(s[j]);
#             continue
#         else:
#             break
string= 'wgrefgdjfwdgvfgwvfwbvfwfvwvfbuw'
my_dic={}
count= 0
for i in string:
    if i in my_dic:
        my_dic[i] = count
    else:
        my_dic[i] = 1
    
print(my_dic)