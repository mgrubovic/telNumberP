from flask import Flask, render_template, session, request, current_app
from get_numbers import read_short, find_short, read_geo, find_geo

app=Flask(__name__)
app.config['data_geo']=[]
app.secret_key = b'88#y2L-F4Q85522266/'


@app.route('/')
@app.route('/about')
def about_page() -> 'html':
    return render_template('about.html', the_title='About site')


@app.route('/viewshort')
def view_short()-> 'html':

    short_data=[]
    if 'data_short' in session:
        print('session short data is up')
        short_data=session['data_short']
    else:
        print('no session short data')
        short_data=read_short('static/data/short.txt')
        session['data_short'] = short_data
    
    titles =('Operator', 'Short code', 'Purpose',)
    return render_template('shortcodes.html',
                           the_title='View short codes',
                           the_row_titles=titles,
                           the_data=short_data,)

@app.route('/viewgeo')
def view_geo()-> 'html':
    
    geo_data = current_app.config['data_geo']
    if len(geo_data) == 0:
       current_app.config['data_geo']=read_geo('static/data/geonumbers-all.csv')
       #za pythonanywhere.com        
       #/home/mgrubovic/mysite/
       #import os
       #<os.getcwd()> = /home/mgrubovic
       #<project_name> = mysite
       #obavezno dodati home direktrorijum odakle se pokrece numbering4web.py kako bi aplikacija mogla da pronadje fajl
       geo_data = current_app.config['data_geo']
       print('no config data_geo')

    titles =('Operator', 'Area code', 'Start', 'End', 'From', 'To',)
    return render_template('viewnumbers.html',
                           the_title='View geographic ranges',
                           the_row_titles=titles,
                           the_data=geo_data,
                           )


@app.route('/shortsearch', methods=['POST'])
def short_search()-> 'html':
    num = request.form['number']
    title='Check results:'

    short_data=session['data_short']
    results = find_short(num, short_data)

    return render_template('shortresult.html',
                           the_number=num,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/geosearch', methods=['POST'])
def geo_search() -> 'html':
    area = request.form['area']
    num = request.form['number']
    title='Here are your results:'

    geo_data= current_app.config['data_geo']
    results = find_geo(area, num, geo_data)

    return render_template('result.html',
                           area_code=area,
                           the_number=num,
                           the_title=title,
                           the_results=results,
                           )


@app.route('/configuration')
def view_configuration()-> 'html':
    return render_template('configuration.html',
                           the_title='Tools',)


@app.route('/summary')
def view_summary()-> 'html':
    return render_template('summary.html',
                           the_title='Summary',)


if __name__=='__main__':
    app.run(debug=True)
