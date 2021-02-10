#Sample code for a graph widget

def get(event, context):
    return {
        'type': 'graph',
        'version': 0.1,
        'config':{
            'chart': {
                'type': 'line'
            },
            'xAxis': {
                'categories': ['January', 'February', 'March']
            },
            'series':  [{
                'name':'blue',
                'color': '#0000FF',
                'data': [5,5,7]
            }, {
                'name':'green',
                'color': '#00FF00',
                'data':  [2,7,8]
            }, {
                'name':'red',
                'color': '#FF0000',
                'data': [3,4,3]
            }]
        }
    };