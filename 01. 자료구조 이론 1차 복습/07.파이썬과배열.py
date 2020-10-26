# 1차원 배열
date = [1,2,3,4,5]
# print(date)

# 2차원 배열
date = [[1,2,3], [4,5,6], [7,8,9]]
# print(date)
# print(date[0])
# print(date[0][0])
# print(date[0][1])
# print(date[0][2])
# print(date[1][0])
# print()
# print(date[2][2])
# print(date[2][1])
# print(date[2][0])
# print()

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

# print(dataset)
# print(dataset[0][0])

#
m_count = 0
for s_idx in range(len(dataset)):
    for c_idx in range(len(dataset[s_idx])):
        if dataset[s_idx][c_idx] == 'M':
            m_count += 1
print(m_count)

#
m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1;
print(m_count)
