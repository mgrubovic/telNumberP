def read_geo(file_name: str)-> list:
    geo_data=[]
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
    geo_data.pop(0)
    return geo_data


def read_short(file_name: str)-> list:
    short_data=[]
    with open(file_name, encoding='utf-8') as file:
            for line in file:
                short_data.append([])
                fields=line.strip().split('	')
                for item in fields:
                    short_data[-1].append(item)
    short_data.pop(0)
    return short_data


def find_geo(area: str, num: str, geo_data: []) -> str:
    answer="Number doesn't exist"
    answer_not_number="You must enter the number"
    num_i = 0
    if num.isdigit():
        num_i = int(num)
    else:
        return answer_not_number

    for row in geo_data:
        if area == row[1]:
            if num_i >= int(row[2]) and num_i <= int(row[3]):
                return 'Number is assigned to: ' + row[0]
    return answer


def find_short(find: str, short_data: []) -> str:

    for line in short_data:
        if find == line[1]:
            answer = 'Short number is assigned to: ' + line[0]
            return answer

    return 'Short number is not assigned'
