from bs4 import BeautifulSoup
import requests
from pandas import DataFrame

def get_stat_spec():
    url='http://ecos.bok.or.kr/api/StatisticTableList/MCT6179RW9QG32IKZZU2/xml/kr/1/604/'
    xml=requests.get(url).text
    soup=BeautifulSoup(xml,'xml')

    spec=soup.find_all('row')

    spec_table={'P_STAT_CODE':[], 'STAT_CODE':[], 'STAT_NAME':[], 'CYCLE':[], 'SRCH_YN':[], 'ORG_NAME':[]}

    for i in range(0,len(spec)):
        spec_table['P_STAT_CODE'].append(spec[i].find('P_STAT_CODE').text)
        spec_table['STAT_CODE'].append(spec[i].find('STAT_CODE').text)
        spec_table['STAT_NAME'].append(spec[i].find('STAT_NAME').text)
        spec_table['CYCLE'].append(spec[i].find('CYCLE').text)
        spec_table['SRCH_YN'].append(spec[i].find('SRCH_YN').text)
        spec_table['ORG_NAME'].append(spec[i].find('ORG_NAME').text)

    df=DataFrame(spec_table, columns=['P_STAT_CODE','STAT_CODE','STAT_NAME','CYCLE','SRCH_YN','ORG_NAME'])
    print(df.ix[0])

if __name__=="__main__":
    get_stat_spec()