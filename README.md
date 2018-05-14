

# scrapy_image_downloader

#主题：利用scrapy自带的image pipeline下载文件或者图片：
编写一个下载图片文件的pipeline类，继承ImagePipeline
内置的ImagePipeline会默认读取Item的image_urls字段，并认为该字段是一个列表，他会遍历列表中的url进行图片下载。
为了实现下载，往往我们要重新定义下载的部分逻辑。

#遇到的困难，在用MySql保存数据时，开的Navicat，然后启动爬虫，会报如下错误：
pymysql.err.OperationalError: (1045, "Access denied for user: '@root' (Using password: NO)")
关掉Navicat就没报错了。
