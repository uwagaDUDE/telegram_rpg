import json


class ItemLoader:
    def items_data(self):
        self.items = open('items.json', 'rt', encoding='UTF-8')
        items = json.load(self.items)
        self.items.close()
        return items['start_items']

print(ItemLoader().items_data())
