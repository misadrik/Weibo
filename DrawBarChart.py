import pygal
from pygal.style import LightSolarizedStyle

# values = [21,16,34,19,12,8,19,7,8,20,3,51]
'''2017年月动态统计'''
'''2017年微博平均字数统计'''
'''2017年含图微博统计'''
'''2017年评论统计'''
'''2017年点赞统计'''
def one_year_bar_chart(chart_title,values):
    chart_legends = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    bar_pic= pygal.Bar(print_values=True,legend_at_bottom=True, legend_at_bottom_columns=12,style = LightSolarizedStyle(
                  value_font_family='googlefont:Lora',
                  value_font_size=30,
                  value_colors=('white','white','white','white','white','white','white','white','white','white','white','white')))
    bar_pic.title = chart_title

    for char_legend,value in zip(chart_legends,values):
        bar_pic.add(char_legend,value)

    bar_pic.render_to_file(chart_title +'.svg')

    print(chart_title + ' Done!')

# one_year_bar_chart('2017年月动态统计',values)


# values = [183,736,116,71,231,488,252,33]
'''年度动态统计'''
'''年评论统计'''
'''年平均评论统计'''
'''年点赞统计'''
'''年平均点赞统计'''
'''年转发微博统计'''
def year_bar_chart(chart_title,values,start,end):
    bar_pic = pygal.Bar(print_values=True,legend_at_bottom=True, legend_at_bottom_columns=8,style = LightSolarizedStyle(
                      value_font_family='googlefont:Raleway',
                      value_font_size=30,
                      value_colors=('white','white','white','white','white','white','white','white','white','white')))

    bar_pic.title = chart_title

    for year, value in zip(range(start,end +1), values):
        bar_pic.add(str(year),value)

    bar_pic.render_to_file(chart_title + '.svg')

    print(chart_title + ' Done!')

# year_bar_chart('年度动态统计',values,2011,2018)

'''年转发微博占比统计'''
# x1 = round(83/183*100,0)
# x2 = round(272/736*100,0)
# x3 = round(107/116*100,0)
# x4 = round(54/71*100,0)
# x5 = round(162/231*100,0)
# x6 = round(50/488*100,0)
# x7 = round(49/252*100,0)
# x8 = round(2/33*100,0)
# dict_values = [[{'value':100-x1,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x2,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x3,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x4,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x5,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x6,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x7,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x8,'color': 'rgba(0, 210, 235, .7)'}],
#     [{'value':x1,'color': 'rgba(255, 45, 20, .6)'},{'value':x2,'color': 'rgba(255, 45, 20, .6)'},{'value':x3,'color': 'rgba(255, 45, 20, .6)'},{'value':x4,'color': 'rgba(255, 45, 20, .6)'},{'value':x5,'color': 'rgba(255, 45, 20, .6)'},{'value':x6,'color': 'rgba(255, 45, 20, .6)'},{'value':x7,'color': 'rgba(255, 45, 20, .6)'},{'value':x8,'color': 'rgba(255, 45, 20, .6)'}],
# ]

def draw_stackedbar_chart(chart_title,dict_values,start,end):
    stackedbar_pic = pygal.StackedBar(print_values=True,style = LightSolarizedStyle(
                    value_font_family='googlefont:Raleway',
                    value_font_size=30,
                    value_colors=('white','white','white','white','white','white','white','white','white')))

    stackedbar_pic.title = chart_title
    stackedbar_pic.x_labels = map(str, range(start, end + 1))

    stackedbar_pic.add('原创占比', dict_values[0],formatter = lambda x:  '%s%%' % x)
    stackedbar_pic.add('转发占比', dict_values[1],formatter = lambda x:  '%s%%' % x)

    # stackedbar_pic.add('原创占比',[{'value':100-x1,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x2,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x3,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x4,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x5,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x6,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x7,'color': 'rgba(0, 210, 235, .7)'},{'value':100-x8,'color': 'rgba(0, 210, 235, .7)'}],formatter = lambda x:  '%s%%' % x)
    # stackedbar_pic.add('转发占比',[{'value':x1,'color': 'rgba(255, 45, 20, .6)'},{'value':x2,'color': 'rgba(255, 45, 20, .6)'},{'value':x3,'color': 'rgba(255, 45, 20, .6)'},{'value':x4,'color': 'rgba(255, 45, 20, .6)'},{'value':x5,'color': 'rgba(255, 45, 20, .6)'},{'value':x6,'color': 'rgba(255, 45, 20, .6)'},{'value':x7,'color': 'rgba(255, 45, 20, .6)'},{'value':x8,'color': 'rgba(255, 45, 20, .6)'}],formatter = lambda x:  '%s%%' % x)
    stackedbar_pic.render_to_file(chart_title + '.svg')

    print(chart_title + ' Done!')

# draw_stackedbar_chart('年转发微博占比统计',dict_values,2011,2018)

'''发博终端统计'''
# dict_values = {'iPhone':941,'weibo.com':704,'Kjava':225,'其他':121}
def draw_bar_pic(chart_title, dict_values):
    bar_pic = pygal.Bar(print_values=True,legend_at_bottom=True, legend_at_bottom_columns=8,style = LightSolarizedStyle(
                      value_font_family='googlefont:Raleway',
                      value_font_size=30,
                      value_colors=('white','white','white','white','white','white','white')))

    bar_pic.title = chart_title

    for key,value in dict_values.items():
        bar_pic.add(key, value)

    bar_pic.render_to_file(chart_title + '.svg')

    print(chart_title + ' Done!')

# draw_bar_pic('发博终端统计',dict_values)