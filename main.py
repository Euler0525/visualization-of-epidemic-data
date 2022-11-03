import shutil
from charts import *
from pprint import pprint


def main():
    prepare.unZip()
    data = prepare.getData()
    shutil.rmtree("./Data")
    data = sorted(data, key=lambda x: x[1])
    pprint(data)
    charts.Charts(data).genGeo()


if __name__ == "__main__":
    main()
