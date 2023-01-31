import json
import random

class ItemLoader:
    def start_items(self):
        self.items = open('items.json', 'rt', encoding='UTF-8')
        items = json.load(self.items)
        self.items.close()
        return items['start_items']

    def start_items_massive(self):
        items = []
        # massive_with_id = []
        # x = dict(zip(e2f.values(), e2f.keys()))
        for i in self.start_items():
            items.append(i)
            x = random.choice(items)
        return x

print(ItemLoader().start_items()[ItemLoader().start_items_massive()])
