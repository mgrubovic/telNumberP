from flask import Flask, render_template, session, request, escape
from get_numbers import find_number, data

app=Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

data=[]



@app.route('/search4', methods=['POST'])
def do_search()-> 'html':
    area = request.form['area']
    num = request.form['number']
    title='Here are your results:'
    results = find_number(area)

    return render_template('result.html',
                           area_code=area,
                           the_number=num,
                           the_title=title,
                           the_results=results,
                           )



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Find number')


@app.route('/about')
def about_page() -> 'html':
    return render_template('about.html', the_title='About site')


@app.route('/viewshort')
def view_short()-> 'html':
    if 'data_short' not in session:
        print('short codes are not here')
	
        with open('kratkikod.csv') as file:
            for line in file:
                data.append([])
                fields=line.strip().split(';')
                for item in fields:
                    data[-1].append(item)
        data.pop(0)
        session['data_short'] = data
	
    titles =('Operator', 'Short code', 'Purpose',)
    return render_template('viewnumbers.html',
                           the_title='View short codes',
                           the_row_titles=titles,
                           the_data=data,)

@app.route('/geo')
def view_geo()-> 'html':
    geo_data=[]
    with open('geonumbers.csv') as file:
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


    titles =('Operator', 'Area code', 'Start', 'End', 'From', 'To',)
    return render_template('viewnumbers.html',
                           the_title='View geographic ranges',
                           the_row_titles=titles,
                           the_data=geo_data,)

@app.route('/configuration')
def view_configuration()-> 'html':
    return render_template('configuration.html',
                           the_title='Tools',)

@app.route('/summary')
def view_summary()-> 'html':
    return render_template('summary.html',
                           the_title='Summary',)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch_log.txt', 'a') as log:
        print(req.form, req.user_agent, req.remote_addr, res, file=log, sep='|')
        #print(req.user_agent, file=log)
        #print(res, file=log)

if __name__=='__main__':
    app.run(debug=True)
