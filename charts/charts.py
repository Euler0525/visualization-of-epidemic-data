import os
from pyecharts.charts import Geo
from pyecharts import options as opts


class Charts(object):
    def __init__(self, data):
        self.data = data

    def genGeo(self):
        geo = Geo()
        geo.add_schema(maptype="china", itemstyle_opts=opts.ItemStyleOpts(color='#EEEEEE', border_color='#999999'))
        geo.add("", self.data)
        geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # Hide data
        geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=[
            {'min': 1, 'max': 10, 'label': "1 - 10", 'color': 'purple'},
            {'min': 11, 'max': 50, 'label': "11 - 50", 'color': 'cyan'},
            {'min': 51, 'max': 100, 'label': "51 - 100", 'color': 'blue'},
            {'min': 101, 'max': 500, 'label': "101 - 500", 'color': 'green'},
            {'min': 501, 'max': 1000, 'label': "501 - 1000", 'color': 'yellow'},
            {'min': 1001, 'max': 5000, 'label': "1001 - 5000", 'color': 'orange'},
            {'min': 5001, 'label': "> 5001", 'color': 'red'}
        ]), title_opts=opts.TitleOpts(
            title="2021年新冠累计确诊数据地图",
            subtitle="数据来源：icode123.cn",
            pos_right="center",
            pos_top="5%"))
        if not os.path.isdir("web"):
            os.mkdir("web")
        geo.render("web/geo.html")
