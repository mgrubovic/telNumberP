data=[]
geo_data=[]


##with open('kratkikod.csv') as file:
##    for line in file:
##        data.append([])
##        fields=line.strip().split(';')
##        for item in fields:
##            data[-1].append(item)


def read_geo(file_name: str)-> None:
    with open(file_name) as file:
        for line in file:
           geo_data.append([])
           fields = line.strip().split(';')
           index=0
           for item in fields:
               if index==1:
                   composite = item.split(' ')
                   geo_data[-1].append(composite[0])
                   geo_data[-1].append(composite[1])
               elif index ==2:
                   composite = item.split(' ')
                   geo_data[-1].append(composite[1])            
               else:
                   geo_data[-1].append(item)
               index +=1
           #for start in geo_data[-1]:
            #   print(start[1], '-', start[2])
            

read_geo('geonumbers.csv')
#print(geo_data)

def find_number(find: str) -> str: 
    isFound=False
    answer = 'number exists '
    for line in data:
        if find in line[1]:
            answer +=  line[0]
            return answer
                #print('number exists')
                #isFound=True
                #break
    return 'there is no number'

##this is for standalone use
##find=input('Find number: ')
##print(find_number(find))

## for testing purpose
##for line in data:
##    print('2 index', line[2])
#print(data)
