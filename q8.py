import re

test = ['<url>https://xcd32112.smart_meter.com</url>',
        '<url>https://tXh67.dia_meter.com</url>',
        '<url>https://yT5495.smart_meter.com</url>',
        '<url>https://ret323_TRu.crown.com</url>',
        '<url>https://luwr3243.celcius.com</url>',
        ]

pure_url = [re.findall('(?<=https://).*[0-9a-zA-Z_.](?=<)', i)[0]
            for i in test]

print(pure_url)

'''
I also found a sql script that works in mysql that matches a regex:

SELECT REGEXP_SUBSTR(column, '(?<=https://).*[0-9a-zA-Z_.](?=<)')
FROM table
'''