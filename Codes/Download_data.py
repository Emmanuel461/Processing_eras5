import cdsapi

c = cdsapi.Client()

c.retrieve(
    'sis-agrometeorological-indicators',
    {
        'version': '1_1',
        'format': 'zip',
        'variable': '2m_temperature',
        'statistic': 'day_time_mean',
        'year': ['2022','2023', '2024'],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07','08', '09', 
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'area': [
            12.9, -16.8, 10,
            -13.5,
        ],
    }, 'DataIntermediate/2m_temperature.zip')

    