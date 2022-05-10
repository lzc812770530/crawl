import pymysql
from itemadapter import ItemAdapter


class MoshouPipeline:
    def open_spider(self,spider):
        self.db = pymysql.connect(user='root',passwd='root',database='game')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        try:
            sql = f'insert into moshou1 values(' \
                  f'"{item["gid"]}", ' \
                  f'"{item["gname"]}", ' \
                  f'"{item["duration_time"]}", ' \
                  f'"{item["proportion1"]}", ' \
                  f'"{item["proportion2"]}", ' \
                  f'"{item["quantity"]}", ' \
                  f'"{item["price_min"]}", ' \
                  f'"{item["price_max"]}") '
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print('error:',e)
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.db.close()
