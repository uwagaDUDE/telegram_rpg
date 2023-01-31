import json


class ItemLoader:
    def start_items(self):
        self.items = open('items.json', 'rt', encoding='UTF-8')
        items = json.load(self.items)
        self.items.close()
        arr = items['start_items']
        return [arr["wooden_sword"],arr["wooden_staff"]]
