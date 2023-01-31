import json


class ItemLoader:
    def start_items(self):
        self.items = open('items.json', 'rt', encoding='UTF-8')
        items = json.load(self.items)
        self.items.close()
        return items['start_items']

    def start_items_massive(self):
        id_list = ["0", "1"]
        massive_with_code_name = []
        massive_with_id = []
        # x = dict(zip(e2f.values(), e2f.keys()))
        for i in self.start_items():
            massive_with_code_name.append(i)
            for b in self.start_items()[i]:
                if self.start_items()[i][b] in id_list:
                    massive_with_id.append(self.start_items()[i][b])
        return f'Массив с названиями обьектов: {massive_with_code_name},\n' \
               f'массив с ID предметов {massive_with_id}'

print(ItemLoader().start_items_massive())
