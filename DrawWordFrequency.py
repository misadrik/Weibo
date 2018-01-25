import pygal
from pygal.style import LightSolarizedStyle,DefaultStyle

def draw_world_frequency(chart_title,filename):
    f = open(filename,'r')
    data = f.readlines()
    print(data)
    bar_pic = pygal.Bar(print_values=True,legend_at_bottom=True, legend_at_bottom_columns=13,style = LightSolarizedStyle(
                      value_font_family='googlefont:Raleway',
                      value_font_size=30,
                      value_colors=('white','white','white','white','white','white','white','white','white','white','white','white','white','white')))

    '''2011词频统计统计统计'''
    bar_pic.title = chart_title

    for value in data:
        value = value.strip('\n')
        bar_pic.add(value.split(',')[0],int(value.split(',')[1]))   

    bar_pic.render_to_file( chart_title + '.svg')
    print(chart_title + 'Done!')

if __name__ == '__main__':
    draw_world_frequency('2011词频统计','w2011.txt')