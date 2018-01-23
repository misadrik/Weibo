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